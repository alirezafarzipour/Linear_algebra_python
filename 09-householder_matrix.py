import numpy as np


def make_householder(A):
    n = A.shape[0]
    I = np.eye(n, dtype=np.double)
    wwt = np.dot(A, A.T)
    wtw = np.dot(A.T, A)[0][0]

    H = I - (2 / wtw) * (wwt)

    return H


x = np.array([[1], [0], [2]], dtype=float)
print(make_householder(x))
