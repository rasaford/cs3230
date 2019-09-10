def S(A, i, j):
    if i >= j or A[i] != A[j]:
        return 0
    return 1 + S(A, i + 1, j - 1)


def f(A):
    max = -0x0ffff
    for j in range(len(A)):
        for i in range(j):
            v = S(A, i, j)
            if v > max:
                max = v
                substr = A[i:i + v]
    return max, substr


def f_prime(A):
    return max([S(A, i, j) for j in range(len(A)) for i in range(j)])


B = ['ALGORITHM', 'RECURSION', 'REDIVIDE', 'DYNAMICPROGRAMMINGMANYTIMES']
for a in B:
    print('f({}) = {}'.format(a, f(a)))
