import numpy as np


def inequality1():
    mat_size = np.random.randint(3, 6, 2)
    a = np.random.randint(-10, 10, size=mat_size)

    norm2 = np.sqrt(np.max(np.linalg.eigvals(np.inner(a, a))))
    norm1 = np.max(np.sum(np.abs(a), axis=0))
    inf_norm = np.max(np.sum(np.abs(a), axis=1))

    return norm2 <= np.sqrt(norm1 * inf_norm)


res = []
for i in range(0, 100000):
    res.append(inequality1())

print(any(x == False for x in res))

# #####################

def inequality2():
    mat_size = np.random.randint(3, 6, 2)
    a = np.random.randint(-10, 10, size=mat_size)

    n = a.shape[1]
    norm2 = np.sqrt(np.max(np.linalg.eigvals(np.inner(a, a))))
    frob = np.sqrt(np.sum(np.abs(a) ** 2))

    return norm2 <= frob <= np.sqrt(n) * norm2


res = []
for i in range(0, 100000):
    res.append(inequality2())

print(any(x == False for x in res))

# #####################

def inequality3():
    mat_size = np.random.randint(3, 6, 2)
    a = np.random.randint(-10, 10, size=mat_size)
    maximum = np.max(np.abs(a))
    norm2 = np.sqrt(np.max(np.linalg.eigvals(np.inner(a, a))))
    right = np.sqrt(a.shape[0] * a.shape[1]) * maximum

    return maximum <= norm2 <= right


res = []
for i in range(0, 100000):
    res.append(inequality2())

print(any(x == False for x in res))

# #####################

def inequality4():
    mat_size = np.random.randint(3, 6, 2)
    a = np.random.randint(0, 10, size=mat_size)

    inf_norm = np.max(np.sum(a, axis=1))

    left = 1 / np.sqrt(a.shape[1]) * inf_norm
    norm2 = np.sqrt(np.max(np.linalg.eigvals(np.inner(a, a))))
    right = np.sqrt(a.shape[0]) * inf_norm

    return left <= norm2 <= right


res = []
for i in range(0, 100000):
    res.append(inequality3())

print(any(x == False for x in res))

# #####################

def inequality5():
    mat_size = np.random.randint(3, 4, 2)
    a = np.random.randint(0, 10, size=mat_size)

    norm1 = np.max(np.sum(a, axis=1))
    norm2 = np.sqrt(np.max(np.linalg.eigvals(np.inner(a, a))))
    right = np.sqrt(a.shape[1]) * norm1

    return 1 / np.sqrt(a.shape[0]) * norm1 <= norm2 <= right


res = []
for i in range(0, 100000):
    res.append(inequality4())

print(any(x == False for x in res))