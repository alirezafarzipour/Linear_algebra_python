import numpy as np
from scipy.spatial import distance

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
x = np.array([[1, 2, 4], [4, 2, 6], [7, 3, 9]])

print("L¹ norm: ")
print(np.linalg.norm(a, 1))

print("L² norm: ")
print(np.linalg.norm(a, 2))

print("Squared L² norm (Euclidean): ")
print(np.linalg.norm(a.T.dot(a)) ** 2)

print("Max norm: ")
print(np.linalg.norm(a, np.inf))

print("Euclidean distance: ")
print(distance.euclidean(a, b))

print("Frobenius norm: \n", np.linalg.norm(x, 'fro'))
print("condition number: \n", np.linalg.cond(x, 'fro'))
