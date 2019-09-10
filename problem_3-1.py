
def f(A, B, i, j):
    if len(A) == i or len(B) == j:
        return max(len(A) - i, len(B) - j)
    if A[i] != B[j]:
        return 1 + min(f(A, B, i + 1, j), f(A, B, i, j + 1))
    else:
        return 1 + f(A, B, i + 1, j + 1)


print('Supersequence')

A = [1, 3, 4, 5, 1]
B = [0, 1, 3, 6, 9]
print('A = {}, B = {}, f(A, B) = {}'.format(A, B, f(A, B, 0, 0)))

A = []
B = []
print('A = {}, B = {}, f(A, B) = {}'.format(A, B, f(A, B, 0, 0)))

A = [1, 5, 0, 9]
B = []
print('A = {}, B = {}, f(A, B) = {}'.format(A, B, f(A, B, 0, 0)))

A = [1, 5, 0, 9]
B = [1, 5, 0, 9]
print('A = {}, B = {}, f(A, B) = {}'.format(A, B, f(A, B, 0, 0)))


def g(A, i, j):
    if i >= j:
        return 0
    if A[i] == A[j]:
        return 2 + g(A, i + 1, j - 1)
    if A[i] != A[j]:
        if i + 1 == j:
            return 3 + g(A, i + 1, j - 1)
        else:
            return 4 + g(A, i + 1, j - 1)


print('Palindrome')

A = 'COMMON'
print('g({}) = {}, g\'({}, {}) = {}'.format(
    A, g(A, 0, len(A) - 1), A, A[::-1], f(A, A[::-1], 0, 0)))

A = 'DEED'
print('g({}) = {}, g\'({}, {}) = {}'.format(
    A, g(A, 0, len(A) - 1), A, A[::-1], f(A, A[::-1], 0, 0)))

A = 'TEST'
print('g({}) = {}, g\'({}, {}) = {}'.format(
    A, g(A, 0, len(A) - 1), A, A[::-1], f(A, A[::-1], 0, 0)))
