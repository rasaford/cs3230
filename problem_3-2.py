money = [1, 4, 7, 13, 28, 52, 91, 365]


def greedy(n):
    if n == 0:
        return 0
    return 1 + greedy(n - max([x for x in money if x <= n]))


opt = {}


def optimal(n):
    if n == 0:
        return 0
    if n < 0:
        return 12345678
    if n in opt:
        return opt[n]
    opt[n] = min([1 + optimal(n - x) for x in money if x <= n])
    return opt[n]


for n in range(100000):
    g = greedy(n)
    o = optimal(n)
    if o != g:
        print('f({}) = greedy: {} optimal: {}'.format(n, g, o))
