import numpy as np

# We have two matrices 3*3
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([[7, 8, 9], [10, 11, 12], [1, 2, 3]])

# Operations
print("Addition: ")
print(np.add(x, y))

print("Subtraction: ")
print(np.subtract(x, y))

print("Division : ")
print(np.divide(x, y))

print("Multiplication: ")
print(np.multiply(x, y))

print("Dot product: ")
print(np.dot(x, y))

print("Inner product: ")
print(np.inner(x, y))

print("Outer product: ")
print(np.outer(x, y))

print("Determinant of y:")
print(np.linalg.det(y))

print("Rank of x: ")
print(np.linalg.matrix_rank(x))

print("Square root : ")
print(np.sqrt(x))

print("The summation of elements : ")
print(np.sum(y))

print("The column wise summation  : ")
print(np.sum(y, axis=0))

print("The row wise summation: ")
print(np.sum(y, axis=1))

print("Matrix transposition : ")
print(x.T)

print("Inverse :")
print(np.linalg.inv(y))

w, v = np.linalg.eig(x)
print('Eigenvalues: ', w)
print('Eigenvectors :\n', v)

