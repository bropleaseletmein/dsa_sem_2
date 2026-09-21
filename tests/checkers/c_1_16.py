


def _parse(inp):
    it = [int(x) for x in inp.split()]
    n = it[0]
    a = [it[1 + i * n: 1 + (i + 1) * n] for i in range(n)]
    return n, a


def _held_karp(n, a):
    if n == 1:
        return 0
    INF = float("inf")
    full = 1 << n
    dp = [[INF] * n for _ in range(full)]
    for v in range(n):
        dp[1 << v][v] = 0
    for mask in range(full):
        row = dp[mask]
        for v in range(n):
            cur = row[v]
            if cur == INF or not (mask >> v) & 1:
                continue
            av = a[v]
            for u in range(n):
                if (mask >> u) & 1:
                    continue
                nm = mask | (1 << u)
                val = cur + av[u]
                if val < dp[nm][u]:
                    dp[nm][u] = val
    return min(dp[full - 1])


def check(inp, out, exp):
    n, a = _parse(inp)
    toks = out.split()
    if len(toks) != n + 1:
        return False, u"ожидалось 1 + %d чисел, получено %d" % (n, len(toks))
    length = int(toks[0])
    path = [int(x) for x in toks[1:]]
    if sorted(path) != list(range(1, n + 1)):
        return False, u"второй строкой должна быть перестановка 1..%d" % n
    real = sum(a[path[i] - 1][path[i + 1] - 1] for i in range(n - 1))
    if real != length:
        return False, u"длина пути %d, а выведено %d" % (real, length)
    best = _held_karp(n, a)
    if length != best:
        return False, u"путь не оптимален: %d, оптимум %d" % (length, best)
    return True, ""
