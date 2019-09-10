import sys
import time


def b(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return sum(b(i) * b(n - i) for i in range(1, n))


def b2(n):
    br = [None] * (n+1)

    def b(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if br[n]:
            return br[n]
        br[n] = sum(b(i) * b(n - i) for i in range(1, n))
        return br[n]

    return b(n)


def b3(n):
    if n <= 0:
        return 0
    br = [1] * (n + 1)
    for i in range(2, n + 1):
        br[i] = sum(br[j] * br[i - j] for j in range(1, i))
    return br[n]


print('naive:')
start = time.time()
for i in range(15):
    print('b({}) = {}'.format(i, b(i)))
print("elapsed time {}".format(time.time() - start))

print('memoized:')
start = time.time()
for i in range(15):
    print('b({}) = {}'.format(i, b2(i)))
print("elapsed time {}".format(time.time() - start))


print('unrolled:')
start = time.time()
for i in range(15):
    print('b({}) = {}'.format(i, b3(i)))
print("elapsed time {}".format(time.time() - start))

