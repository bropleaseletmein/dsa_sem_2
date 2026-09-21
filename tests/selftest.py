

import itertools
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import refs
from gen import graphs as G

FAILED = []


def _norm(v):
    if isinstance(v, (list, tuple)):
        return [str(x) for x in v]
    return str(v).split()


def check(name, got, want, data=None):
    if _norm(got) != _norm(want):
        FAILED.append("%s: получено %r, ожидалось %r (%r)" % (name, got, want, data))


def t_1_2():
    rnd = random.Random(1)
    for _ in range(300):
        d = rnd.randint(4, 40)
        m = rnd.randint(1, 20)
        stops = sorted(rnd.sample(range(2, d), rnd.randint(1, min(6, d - 2))))
        inp = "%d\n%d\n%d\n%s" % (d, m, len(stops), " ".join(map(str, stops)))

        pts = [0] + stops + [d]
        INF = 10 ** 9
        best = {0: 0}
        for _ in range(len(pts)):
            nxt = dict(best)
            for i, c in best.items():
                for j in range(len(pts)):
                    if 0 < pts[j] - pts[i] <= m:
                        v = c + (1 if i > 0 else 0)
                        if v < nxt.get(j, INF):
                            nxt[j] = v
            best = nxt
        want = best.get(len(pts) - 1, -1)
        check("1.2", refs.ref_1_2(inp), want, inp)


def t_1_3():
    rnd = random.Random(2)
    for _ in range(200):
        n = rnd.randint(1, 6)
        a = [rnd.randint(-10, 10) for _ in range(n)]
        b = [rnd.randint(-10, 10) for _ in range(n)]
        want = max(sum(x * y for x, y in zip(a, perm)) for perm in itertools.permutations(b))
        inp = "%d\n%s\n%s" % (n, " ".join(map(str, a)), " ".join(map(str, b)))
        check("1.3", refs.ref_1_3(inp), want, inp)


def t_1_8():
    rnd = random.Random(3)
    for _ in range(200):
        n = rnd.randint(1, 8)
        segs = []
        for _ in range(n):
            s = rnd.randint(1, 10)
            segs.append((s, rnd.randint(s + 1, 12)))
        best = 0
        for mask in range(1 << n):
            chosen = sorted([segs[i] for i in range(n) if mask >> i & 1])
            ok = all(chosen[i][1] <= chosen[i + 1][0] for i in range(len(chosen) - 1))
            if ok:
                best = max(best, len(chosen))
        inp = "%d\n%s" % (n, "\n".join("%d %d" % s for s in segs))
        check("1.8", refs.ref_1_8(inp), best, inp)


def t_1_10():
    rnd = random.Random(4)
    for _ in range(300):
        n = rnd.randint(1, 6)
        s = rnd.randint(1, 8)
        apples = [(rnd.randint(1, 8), rnd.randint(1, 8)) for _ in range(n)]
        want = any(refs.ref_1_10_simulate(p, s, apples)
                   for p in itertools.permutations(range(n)))
        got = refs.ref_1_10_simulate(refs.ref_1_10_feasible(n, apples), s, apples)
        check("1.10", got, want, (s, apples))


def t_1_11():
    rnd = random.Random(5)
    for _ in range(200):
        W = rnd.randint(1, 40)
        n = rnd.randint(1, 8)
        w = [rnd.randint(0, 50) for _ in range(n)]
        best = 0
        for mask in range(1 << n):
            tot = sum(w[i] for i in range(n) if mask >> i & 1)
            if tot <= W:
                best = max(best, tot)
        inp = "%d %d\n%s" % (W, n, " ".join(map(str, w)))
        check("1.11", refs.ref_1_11(inp), best, inp)


def t_1_17():

    moves = refs._knight_moves()
    for n in range(1, 8):
        cur = [d for d in range(10) if d not in (0, 8)]
        for _ in range(n - 1):
            cur = [e for d in cur for e in moves[d]]
        check("1.17", refs.ref_1_17(str(n)), len(cur) % (10 ** 9), n)


def t_bst_checks():
    rnd = random.Random(6)
    for _ in range(400):
        n = rnd.randint(1, 7)
        keys = [rnd.randint(0, 4) for _ in range(n)]
        left = [-1] * n
        right = [-1] * n
        free = list(range(1, n))
        rnd.shuffle(free)
        for v in free:
            while True:
                p = rnd.randint(0, n - 1)
                if p == v:
                    continue
                side = rnd.choice(("l", "r"))
                if side == "l" and left[p] == -1:
                    left[p] = v
                    break
                if side == "r" and right[p] == -1:
                    right[p] = v
                    break

        seen = set()
        st = [0]
        while st:
            v = st.pop()
            if v in seen:
                break
            seen.add(v)
            for c in (left[v], right[v]):
                if c != -1:
                    st.append(c)
        if len(seen) != n:
            continue
        inp = "%d\n%s" % (n, "\n".join("%d %d %d" % (keys[i], left[i], right[i])
                                       for i in range(n)))

        def subtree(v):
            out = []
            st = [v]
            while st:
                x = st.pop()
                out.append(keys[x])
                for c in (left[x], right[x]):
                    if c != -1:
                        st.append(c)
            return out

        strict = all(all(k < keys[v] for k in subtree(left[v]) if left[v] != -1) and
                     all(k > keys[v] for k in subtree(right[v]) if right[v] != -1)
                     for v in range(n))
        dup_ok = all(all(k < keys[v] for k in subtree(left[v]) if left[v] != -1) and
                     all(k >= keys[v] for k in subtree(right[v]) if right[v] != -1)
                     for v in range(n))
        check("2.6", refs.ref_2_6(inp), "CORRECT" if strict else "INCORRECT", inp)
        check("2.7", refs.ref_2_7(inp), "CORRECT" if dup_ok else "INCORRECT", inp)


def t_graphs():
    rnd = random.Random(7)
    for _ in range(200):
        n = rnd.randint(1, 8)
        m = rnd.randint(0, min(12, n * (n - 1) // 2))
        edges = G.random_simple(n, m, rnd)

        reach = [[i == j for j in range(n + 1)] for i in range(n + 1)]
        for u, v in edges:
            reach[u][v] = reach[v][u] = True
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if reach[i][k] and reach[k][j]:
                        reach[i][j] = True
        comps = len({frozenset(j for j in range(1, n + 1) if reach[i][j])
                     for i in range(1, n + 1)})
        check("3.2", refs.ref_3_2(G.dump(n, edges)), comps, edges)
        if n >= 2:
            u, v = rnd.sample(range(1, n + 1), 2)
            check("3.1", refs.ref_3_1(G.dump(n, edges, (u, v))),
                  1 if reach[u][v] else 0, (edges, u, v))

            INF = float("inf")
            d = [[INF] * (n + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                d[i][i] = 0
            for a, b in edges:
                d[a][b] = d[b][a] = 1
            for k in range(1, n + 1):
                for i in range(1, n + 1):
                    for j in range(1, n + 1):
                        if d[i][k] + d[k][j] < d[i][j]:
                            d[i][j] = d[i][k] + d[k][j]
            want = -1 if d[u][v] == INF else d[u][v]
            check("3.6", refs.ref_3_6(G.dump(n, edges, (u, v))), want, (edges, u, v))

        ok = 0
        for mask in range(1 << n):
            if all(((mask >> (u - 1)) & 1) != ((mask >> (v - 1)) & 1) for u, v in edges):
                ok = 1
                break
        check("3.7", refs.ref_3_7(G.dump(n, edges)), ok, edges)

        de = G.random_simple(n, m, rnd, directed=True)
        r = [[i == j for j in range(n + 1)] for i in range(n + 1)]
        for u, v in de:
            r[u][v] = True
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if r[i][k] and r[k][j]:
                        r[i][j] = True
        sccs = len({frozenset(j for j in range(1, n + 1) if r[i][j] and r[j][i])
                    for i in range(1, n + 1)})
        check("3.5", refs.ref_3_5(G.dump(n, de)), sccs, de)


def t_bellman():
    rnd = random.Random(8)
    for _ in range(200):
        n = rnd.randint(1, 6)
        m = rnd.randint(0, 10)
        base = G.random_simple(n, m, rnd, directed=True)
        edges = [(u, v, rnd.randint(-5, 5)) for u, v in base]
        INF = float("inf")

        d = [INF] * (n + 1)
        s = rnd.randint(1, n)
        d[s] = 0
        for _ in range(4 * n + 10):
            for u, v, w in edges:
                if d[u] != INF and d[u] + w < d[v]:
                    d[v] = d[u] + w
        minus = set()
        for _ in range(n + 2):
            for u, v, w in edges:
                if d[u] != INF and (d[u] + w < d[v] or u in minus):
                    minus.add(v)
        want = []
        for i in range(1, n + 1):
            if d[i] == INF:
                want.append("*")
            elif i in minus:
                want.append("-")
            else:
                want.append(str(d[i]))
        got = refs.ref_3_10(G.dump(n, edges, (s,)))
        check("3.10", got, "\n".join(want), (edges, s))

        has = False
        for k in range(1, n + 1):
            for cyc in itertools.permutations(range(1, n + 1), k):
                w = 0
                ok = True
                for i in range(k):
                    a, b = cyc[i], cyc[(i + 1) % k]
                    ws = [e[2] for e in edges if e[0] == a and e[1] == b]
                    if not ws:
                        ok = False
                        break
                    w += min(ws)
                if ok and w < 0:
                    has = True
                    break
            if has:
                break
        check("3.9", refs.ref_3_9(G.dump(n, edges)), 1 if has else 0, edges)


def t_strings():
    rnd = random.Random(9)
    for _ in range(400):
        n = rnd.randint(1, 30)
        s = "".join(rnd.choice("ab") for _ in range(n))
        naive_pi = [0] * n
        for i in range(1, n):
            for k in range(i, 0, -1):
                if s[:k] == s[i - k + 1:i + 1]:
                    naive_pi[i] = k
                    break
        naive_z = [0] * n
        naive_z[0] = n
        for i in range(1, n):
            k = 0
            while i + k < n and s[k] == s[i + k]:
                k += 1
            naive_z[i] = k
        check("4.5", refs.pi_from_z(s), " ".join(map(str, naive_pi)), s)
        check("4.6", refs.z_from_pi(s), " ".join(map(str, naive_z)), s)
        check("4.5/kmp", refs.prefix_function(s), " ".join(map(str, naive_pi)), s)
        check("4.6/z", refs.z_function(s), " ".join(map(str, naive_z)), s)

        cnt = sum(1 for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n)
                  if s[i] == s[k])
        check("4.2", refs.ref_4_2(s), cnt, s)

        t = "".join(rnd.choice("ab") for _ in range(rnd.randint(1, 20)))
        best = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in t:
                    best = max(best, j - i)
        check("4.7", refs.lcs_length(s, t), best, (s, t))


def t_decomposition():
    rnd = random.Random(10)
    for _ in range(120):
        n = rnd.randint(1, 12)
        s = "".join(rnd.choice("ab") for _ in range(n))

        INF = 10 ** 9
        best = [INF] * (n + 1)
        best[0] = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                piece = s[i:j]
                L = j - i
                cost = L
                for p in range(1, L):
                    if L % p == 0 and piece == piece[:p] * (L // p):
                        cost = min(cost, p + 1 + len(str(L // p)))
                add = cost + (1 if i > 0 else 0)
                if best[i] + add < best[j]:
                    best[j] = best[i] + add
        check("4.9", refs.decomposition_cost(s), best[n], s)


def main():
    for fn in (t_1_2, t_1_3, t_1_8, t_1_10, t_1_11, t_1_17, t_bst_checks,
               t_graphs, t_bellman, t_strings, t_decomposition):
        fn()
        print("  %-16s %s" % (fn.__name__, "ошибок нет" if not FAILED else "ЕСТЬ ОШИБКИ"))
        if FAILED:
            for f in FAILED[:5]:
                print("     " + f)
            return 1
    print("Все эталоны согласуются с полным перебором.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
