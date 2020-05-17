import networkx as nx
from scipy import sparse 
from pagerank import pagerank
from pagerank2 import pagerank2
from pagerank3 import pagerank3

import numpy as np
# sample graph
G=nx.barabasi_albert_graph(60,41)
# prebuilt function using graphs
pr=nx.pagerank(G,0.4)
#convert to array
pr_array = pr.items()
expectedR = [0] * len(pr_array)

for (key, value) in pr_array:
    expectedR[key] = value

#get adjaceny matrix

A = nx.to_numpy_matrix(G)
# A = A.transpose()
print(A)
# A = np.asmatrix([[0,0,1],[0,0,1], [0,0,0]])

print(A)

print(A[3,:])
print(A[4,:])
#pass to custom page rank function
R = pagerank2(A)
R1 = pagerank3(A)


print('expected',expectedR)
print('R',R)
print('R1',R1)

print('expectedargs',np.argsort(expectedR))
print('Rargs',np.argsort(R))
print('R1args',np.argsort(R1))

print('custom1 - expected',np.argsort(R) - np.argsort(expectedR))
print('custom2 - expected',np.argsort(R1) - np.argsort(expectedR))
print('difference of customs', np.argsort(R1) - np.argsort(R))

print('norm of custom1 - expected',np.linalg.norm(np.argsort(R) - np.argsort(expectedR)))
print('norm of custom2 - expected',np.linalg.norm(np.argsort(R1) - np.argsort(expectedR)))
print('norm of difference of customs', np.linalg.norm(np.argsort(R1) - np.argsort(R)))

print(np.sum(expectedR))
print(np.sum(R))
print(np.sum(R1))
# print(R1[0:10])


