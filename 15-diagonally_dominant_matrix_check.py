import numpy as np


def is_dom(m):
    n = m.shape[0]
    for i in range(0, n):

        summation = 0
        for j in range(0, n):
            summation = summation + abs(m[i][j])

        summation = summation - abs(m[i][i])

        if (abs(m[i][i]) < summation):
            return False

    return True


x = np.array([[3, 2, 0],
              [0, -1, 0],
              [2, 3, 7]])

print(is_dom(x))
