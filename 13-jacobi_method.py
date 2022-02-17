import numpy as np


# implementation 1:
def jacobi_1(A, b, tolerance=1e-10, max_iterations=20):
    x = np.zeros_like(b, dtype=np.double)
    T = A - np.diag(np.diagonal(A))

    for k in range(max_iterations):
        x_old = x.copy()
        x[:] = (b - np.dot(T, x)) / np.diagonal(A)
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break
    return x


# implementation 2:
def jacobi_2(A, b, tolerance=1e-10):
    x = np.zeros_like(b)
    for it_count in range(20):
        print("Current solution:", x)
        x_new = np.zeros_like(x)

        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        if np.allclose(x, x_new, atol=tolerance, rtol=0.):
            break
        x = x_new
    return x


A1 = np.array([[5, 2, -1],
               [1, 6, -3],
               [2, 1, 4]])

b1 = np.array([6, 4, 7])


# implementation 1:
print("implementation 1: ", jacobi_1(A1, b1, 0.005))


# implementation 2:
print("\nimplementation 2: ")
x = jacobi_2(A1, b1, 0.005)
print("solution:", x)
error = np.dot(A1, x) - b1
print("Error:")
print(error)
