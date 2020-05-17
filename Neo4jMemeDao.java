
package dao;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;

import org.neo4j.driver.Session;

import exception.DaoException;
import model.Meme;
import model.User;
import graph.MemeGraph;
import graph.PipeGraph;
import graph.UserGraph;
import graph.WellManager;
import graph.GraphMaster;
import graph.MemeSimilarity;

public class Neo4jMemeDao implements MemeDao {

    private GraphMaster graph;
    private static final double SIMILARITY_BENCHMARK = 0.96;

    public Neo4jMemeDao(GraphMaster graph) {
        this.graph = graph;
        // THIS IS FOR DEBUGGING. NOTE: ALTHOUGH CONFUSING, IT IS RE-ADD - NOT A TYPO.
        if (graph.shouldReadd()) {
            this.readdMemes();
        }
    }


    public void memeRank(int userId) {
        Session session = graph.getSession();
        List<Meme> memes = MemeGraph.getMemes(session);
        Map<Integer, Double> userScores = new HashMap<Integer, Double>();
        Map<Integer, Double> memeScores = new HashMap<Integer, Double>((memes.size()));
        Map<Integer, Integer> memeLikes = new HashMap<Integer, Integer>((memes.size()));
        // GIVE EACH MEME A SCORE
        for (Meme meme : memes) {
            double memeScore = 0;
            List<User> usersThatLikedMeme = MemeGraph.getUsersThatLikedMeme(session, meme.getId());
            memeLikes.put(meme.getId(), usersThatLikedMeme.size());
            for (User userThatLikedMeme : usersThatLikedMeme) {
                // FOR EACH USER THAT LIKE THE MEME
                if (userThatLikedMeme.getId() != userId) {
                    // BESIDES THIS USER
                    if (!userScores.containsKey(userThatLikedMeme.getId())) {
                        // IF WE DONT HAVE THE USER SIMILARITY SCORE, COMPUTE IT
                        Set<Integer> user1LikedMemeIds = new HashSet<>(
                                UserGraph.getLikedMemeIdsByUserId(session, userId));
                        Set<Integer> user2LikedMemeIds = new HashSet<>(
                                UserGraph.getLikedMemeIdsByUserId(session, userThatLikedMeme.getId()));
                        Set<Integer> intersection = new HashSet<>(user1LikedMemeIds);
                        Set<Integer> union = new HashSet<>(user1LikedMemeIds);
                        intersection.retainAll(user2LikedMemeIds);
                        union.addAll(user2LikedMemeIds);
                        double top = 0;
                        double bottom = 0;
                        for (int memeId : union) {
                            if (!memeLikes.containsKey(memeId)) {
                                memeLikes.put(memeId, MemeGraph.getUsersThatLikedMeme(session, memeId).size());
                            }
                            double memeImportance = (1.0) / (memeLikes.get(memeId));
                            bottom += memeImportance;
                            if (intersection.contains(memeId)) {
                                top += memeImportance;
                            }
                        }
                        double userSimilarityScore = top / bottom;
                        userScores.put(userThatLikedMeme.getId(), userSimilarityScore);
                    }
                    memeScore += userScores.get(userThatLikedMeme.getId());
                }
            }
            memeScores.put(meme.getId(), memeScore);
        }
        // return memeScores;
        Set<Entry<Integer, Double>> memeRank = memeScores.entrySet();
        for (Entry<Integer, Double> e : memeRank) {
            int memeId = e.getKey();
            double memeScore = e.getValue();
            if (memeScore > 0.0) {
                System.out.println("Meme " + memeId + " has score " + memeScore);
            }
        }
    }
}
