import numpy as np
from scipy import sparse 

def pagerank2(A, d=0.85, r0=0, iterations=13):
    n = A.shape[0]
    if(r0 == 0):
        R = sparse.csr_matrix(np.full((n,1), 1/n))
    else:
        R = r0
    K = np.zeros(A.shape)
    for i, row in enumerate(A):
        outgoing = np.sum(row)
        # print('outgoing',outgoing)
        K[i,i] = outgoing

    M = np.transpose(np.matmul(np.linalg.inv(K),A))
    M = M.transpose()
    for i, col in enumerate(M):
        # print('col sum', np.sum(col))
        if(np.count_nonzero(col) == 0):
            M[i] = R
            # print("after",M)
    M = M.transpose()
    # print('M',M)
    M = sparse.csr_matrix(M)
    iterations = 50
    D = sparse.csr_matrix(np.full((n,1),(1-d)/n))
    for i in range(iterations):
        R = M*R + D

    R = R.todense()
    R = R.flatten()
    return R
