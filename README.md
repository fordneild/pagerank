# PageRank
This is my final project for Mathematical and Compuational Foundations of Data Science

## Components
In my quest to implement PageRank I discovered many different solutions. 

pagerank.py was pulled from GeeksForGeeks.com and uses the pagerank implementation used in the networkx python library.

pagerank2.py was my first attempt at implementing PageRank following the matematical steps laid out on the wikipedia page for PageRank.

pagerank3.py was my second attempt. Instead of applying the dampening factor on each iteration of the power iteration method, I applied it to the enitre normalized adjacency matrix just once.

run.py runs all three pagerank algorithms on a barabasi-albert graph generates graphs by favorably adding edges to higher degree nodes. It compares the results of the page rank algorithm. There are some stranges differecnes in the results where it seems like rank of two nodes has been swapped. I have been unable to find a satisfying answer to why these difference sin the results arise.

web-Google.txt This is a massive file posted by the google team for a public competition to rank pages.

# MemeRank
After implementing pageRank I wanted to build something to help rank memes in a web app I have been building. Attached is the file Neo4jMemeDao.java. This is the data-access-object we use to work with memes in our Neo4j graph. I removed most functions and just left in the memerank function. Obviously you cannot run it here, but I thought it might be intresting to include my implemenation.