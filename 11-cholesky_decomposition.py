import numpy as np


def cholesky(A):
    n = A.shape[0]

    L = np.zeros((n, n), dtype=np.double)

    for k in range(n):
        L[k, k] = np.sqrt(A[k, k] - np.sum(L[k, :] ** 2))

        L[(k + 1):, k] = (A[(k + 1):, k] - L[(k + 1):, :] @ L[:, k]) / L[k, k]

    return L


y = np.array([[2, -1, 0], [-1, 2, -1.], [0, -1, 2.]])

print("cholesky:\n", cholesky(y))

print("cholesky with numpy: \n", np.linalg.cholesky(y))
