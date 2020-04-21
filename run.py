import networkx as nx
from scipy import sparse 
import numpy as np
G=nx.barabasi_albert_graph(60,41)
A = nx.to_numpy_matrix(G)
print(A) 
pr=nx.pagerank(G,0.4)
K = np.zeros(A.shape)
n = A.shape[0]
for i, row in enumerate(A):
    outgoing = np.sum(row)
    # print('outgoing',outgoing)
    K[i,i] = outgoing
print(K)

M = np.transpose(np.matmul(np.linalg.inv(K),A))
M = sparse.csr_matrix(M)
print(M)
d = 1
iterations = 1
R = sparse.csr_matrix(np.full((n,1), 1/n))
D = sparse.csr_matrix(np.full((n,1),(1-d)/n))
for i in range(iterations):

    R = M*R + D

R = R.todense()
R = R.flatten()
expectedR = [0] * n
for (key, value) in pr.items():
    expectedR[key] = value
# print(R[0])
# print(expectedR)
# print(R-expectedR)
print(np.argsort(R))
print(np.argsort(expectedR))
print(np.argsort(R) - np.argsort(expectedR))
# print(total)

