import numpy as np


def gauss_seidel(A, b, tolerance=1e-10, max_iterations=10000):
    x = np.zeros_like(b, dtype=np.double)

    for k in range(max_iterations):
        x_old = x.copy()
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, (i + 1):], x_old[(i + 1):])) / A[i, i]

        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break

    return x


A1 = np.array([[5, 2, -1],
               [1, 6, -3],
               [2, 1, 4]])

b1 = np.array([6, 4, 7])

print(gauss_seidel(A1, b1))
