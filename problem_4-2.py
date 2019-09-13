import numpy as np

R = C = np.array([i for i in range(10)])


def fill(R, C):
    if sum(R) != sum(C) or len(R) != len(C):
        raise Exception('sum(R) != sum(C)')
    n = len(R)
    A = np.zeros((n, n))
    for i in range(n):
        Curr = np.array([sum(A[:, j]) for j in range(n)])
        B = (C - Curr).argsort()[-R[i]:] if R[i] != 0 else []
        for j in range(n):
            A[i, j] = 1 if j in B else 0
    return A


print('fill({}, {}) = \n{}'.format(R, C, fill(R, C)))
