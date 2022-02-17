import numpy as np

A = np.array([[2, -1, 5, 1], [3, 2, 2, -6], [1, 3, 3, -1], [5, -2, -3, 3]])
B = np.array([-3, -32, -47, 49])  # Matrix of coefficients
C = A.copy()
X = []

for i in range(0, len(B)):
    for j in range(0, len(B)):
        C[j][i] = B[j]
        if i > 0:
            C[j][i - 1] = A[j][i - 1]
    X.append(round(np.linalg.det(C) / np.linalg.det(A), 1))

print('w=', X[0], '   x=', X[1], '   y=' ,X[2], '   z=', X[3])
