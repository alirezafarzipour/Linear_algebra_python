import numpy as np


def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = householder(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A


def householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H


x = np.array([[2, 1, 3],
              [-1, 0, 7],
              [0, -1, -1]])

q, r = qr(x)
print('Q:\n', q.round(8))
print('R:\n', r.round(8))

print("with numpy:")
q, r = np.linalg.qr(x)
print('Q:\n', q)
print('R:\n', r)