def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M


def transpose(M):
    if not isinstance(M[0], list):
        M = [M]
    rows = len(M)
    cols = len(M[0])
    MT = zeros_matrix(cols, rows)
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]
    return MT


def addition(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')
    C = zeros_matrix(rowsA, colsB)

    # Section 3: Perform element by element sum
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtraction(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]
    return C


def multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
    return C


def product(list):
    matrix_product = list[0]
    for matrix in list[1:]:
        matrix_product = multiply(matrix_product, matrix)
    return matrix_product


x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[7, 8, 9], [10, 11, 12], [1, 2, 3]]

print("Matrix transposition : ")
print(transpose(x))

print("Addition: ")
print(addition(x,y))

print("Subtraction: ")
print(subtraction(x,y))

print("multiply: ")
print(multiply(x,y))


