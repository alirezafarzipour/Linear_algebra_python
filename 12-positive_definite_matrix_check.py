import numpy as np


def is_pos_def(A):
    if np.array_equal(A, A.T):
        try:
            np.linalg.cholesky(A)  # Cholesky decomposition fails for matrices that are NOT positive definite!
            return True
        except np.linalg.LinAlgError:
            return False
    else:
        return False


x = np.array([[2, 1],
              [1, 5]])
print(is_pos_def(x))

print("with numpy: ", np.all(np.linalg.eigvals(x) > 0))
