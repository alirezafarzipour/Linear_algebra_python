import numpy as np


def lu_decomposition(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)

    for i in range(n):
        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]
    return L, U


def plu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)

    number_of_permutations = 0

    for i in range(n):
        for k in range(i, n):
            if ~np.isclose(U[i, i], 0.0):
                break
            U[[k, k + 1]] = U[[k + 1, k]]
            P[[k, k + 1]] = P[[k + 1, k]]
            number_of_permutations += 1

        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]
    return U, number_of_permutations


def lu_det(A):
    L, U = lu_decomposition(A)
    det_l = np.linalg.det(L)
    det_u = np.linalg.det(U)
    return det_u * det_l


def plu_det(A):
    U, number_of_permutations = plu(A)

    if number_of_permutations % 2 == 0:
        return np.diagonal(U).prod()
    else:
        return -np.diagonal(U).prod()


A = np.array([[6, 2, 3],
              [1, 1, 1],
              [0, 4, 9.0]])

print("with LU: ", lu_det(A))
print("with PLU: ", plu_det(A))
