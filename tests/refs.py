
from collections import deque
from fractions import Fraction
import sys
import threading


def ref_1_1_value(text):
    it = text.split()
    n, W = int(it[0]), int(it[1])
    items = []
    k = 2
    for _ in range(n):
        p, w = int(it[k]), int(it[k + 1])
        k += 2
        items.append((p, w))
    total = Fraction(0)
    cap = Fraction(W)

    rest = []
    for p, w in items:
        if w == 0:
            total += p
        else:
            rest.append((p, w))
    rest.sort(key=lambda pw: Fraction(pw[0], pw[1]), reverse=True)
    for p, w in rest:
        if cap <= 0:
            break
        take = min(Fraction(w), cap)
        total += Fraction(p, w) * take
        cap -= take
    return total


def ref_1_2(text):
    it = [int(x) for x in text.split()]
    d, m, n = it[0], it[1], it[2]
    stops = it[3:3 + n]
    pts = [0] + stops + [d]
    INF = float("inf")
    dp = [INF] * len(pts)
    dp[0] = 0
    for i in range(len(pts)):
        if dp[i] == INF:
            continue
        cost = dp[i] + (1 if i > 0 else 0)
        for j in range(i + 1, len(pts)):
            if pts[j] - pts[i] > m:
                break
            if cost < dp[j]:
                dp[j] = cost
    return "-1" if dp[-1] == INF else str(dp[-1])


def ref_1_3(text):
    it = text.split()
    n = int(it[0])
    a = sorted(int(x) for x in it[1:1 + n])
    b = sorted(int(x) for x in it[1 + n:1 + 2 * n])
    return str(sum(x * y for x, y in zip(a, b)))


def ref_1_8(text):
    it = [int(x) for x in text.split()]
    n = it[0]
    segs = [(it[1 + 2 * i], it[2 + 2 * i]) for i in range(n)]

    by_finish = {}
    for s, f in segs:
        by_finish.setdefault(f, []).append(s)
    top = max(f for _, f in segs)
    best = [0] * (top + 1)
    for t in range(1, top + 1):
        cur = best[t - 1]
        for s in by_finish.get(t, ()):
            cand = best[s] + 1
            if cand > cur:
                cur = cand
        best[t] = cur
    return str(best[top])


def ref_1_10_feasible(n, apples):
    gain = sorted([i for i in range(n) if apples[i][1] >= apples[i][0]],
                  key=lambda i: apples[i][0])
    loss = sorted([i for i in range(n) if apples[i][1] < apples[i][0]],
                  key=lambda i: -apples[i][1])
    return gain + loss


def ref_1_10_simulate(order, s, apples):
    for i in order:
        a, b = apples[i]
        if s - a <= 0:
            return False
        s = s - a + b
    return True


def ref_1_11(text):
    it = [int(x) for x in text.split()]
    W, n = it[0], it[1]
    ws = it[2:2 + n]
    mask = 1
    limit = (1 << (W + 1)) - 1
    for w in ws:
        if w == 0 or w > W:
            continue
        mask |= (mask << w) & limit
    reach = mask & limit
    return str(reach.bit_length() - 1)


def _knight_moves():
    pos = {}
    grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], [None, '0', None]]
    for r in range(4):
        for c in range(3):
            if grid[r][c] is not None:
                pos[grid[r][c]] = (r, c)
    moves = {d: [] for d in pos}
    for d, (r, c) in pos.items():
        for dr, dc in ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)):
            for e, (r2, c2) in pos.items():
                if (r + dr, c + dc) == (r2, c2):
                    moves[d].append(e)
    return {int(k): sorted(int(x) for x in v) for k, v in moves.items()}


def ref_1_17(text):
    MOD = 10 ** 9
    n = int(text.split()[0])
    mv = _knight_moves()
    cnt = [0] * 10
    for d in range(10):
        if d not in (0, 8):
            cnt[d] = 1
    for _ in range(n - 1):
        nxt = [0] * 10
        for d in range(10):
            if cnt[d]:
                for e in mv[d]:
                    nxt[e] = (nxt[e] + cnt[d]) % MOD
        cnt = nxt
    return str(sum(cnt) % MOD)


RANKS = '6789TJQKA'


def _beats(c, x, trump):
    if x[1] == trump:
        return c[1] == trump and RANKS.index(c[0]) > RANKS.index(x[0])
    if c[1] == x[1]:
        return RANKS.index(c[0]) > RANKS.index(x[0])
    return c[1] == trump


def ref_1_21(text):
    lines = [l for l in text.splitlines() if l.strip()]
    n, m, trump = lines[0].split()[0], lines[0].split()[1], lines[0].split()[2]
    n, m = int(n), int(m)
    hand = lines[1].split()
    attack = lines[2].split()

    adj = [[j for j in range(n) if _beats(hand[j], attack[i], trump)] for i in range(m)]
    match = [-1] * n

    def try_kuhn(i, used):
        for j in adj[i]:
            if not used[j]:
                used[j] = True
                if match[j] == -1 or try_kuhn(match[j], used):
                    match[j] = i
                    return True
        return False

    for i in range(m):
        if not try_kuhn(i, [False] * n):
            return "NO"
    return "YES"


def _read_tree_0(text):
    it = text.split()
    n = int(it[0])
    key, left, right = [0] * n, [-1] * n, [-1] * n
    k = 1
    for i in range(n):
        key[i] = int(it[k]); left[i] = int(it[k + 1]); right[i] = int(it[k + 2])
        k += 3
    return n, key, left, right


def _read_tree_1(text):
    it = text.split()
    n = int(it[0])
    key = [0] * (n + 1); left = [0] * (n + 1); right = [0] * (n + 1)
    k = 1
    for i in range(1, n + 1):
        key[i] = int(it[k]); left[i] = int(it[k + 1]); right[i] = int(it[k + 2])
        k += 3
    return n, key, left, right


def _run_deep(fn):
    box = {}

    def target():
        box['v'] = fn()

    old = sys.getrecursionlimit()
    sys.setrecursionlimit(1000000)
    threading.stack_size(256 * 1024 * 1024)
    t = threading.Thread(target=target)
    t.start()
    t.join()
    sys.setrecursionlimit(old)
    return box['v']


def ref_2_1(text):
    n, key, left, right = _read_tree_0(text)

    def go():
        ino, pre, post = [], [], []

        def walk(v):
            if v == -1:
                return
            pre.append(key[v])
            walk(left[v])
            ino.append(key[v])
            walk(right[v])
            post.append(key[v])

        walk(0)
        return ino, pre, post

    ino, pre, post = _run_deep(go)
    return "\n".join(" ".join(map(str, x)) for x in (ino, pre, post))


def ref_2_5(text):
    import bisect
    arr = []
    out = []
    for line in text.splitlines():
        parts = line.split()
        if not parts:
            continue
        op, x = parts[0], int(parts[1])
        i = bisect.bisect_left(arr, x)
        present = i < len(arr) and arr[i] == x
        if op == "insert":
            if not present:
                arr.insert(i, x)
        elif op == "delete":
            if present:
                arr.pop(i)
        elif op == "exists":
            out.append("true" if present else "false")
        elif op == "next":
            j = bisect.bisect_right(arr, x)
            out.append(str(arr[j]) if j < len(arr) else "none")
        elif op == "prev":
            j = bisect.bisect_left(arr, x)
            out.append(str(arr[j - 1]) if j > 0 else "none")
    return "\n".join(out)


def _bst_check(n, key, left, right, root, none, strict_right):
    if n == 0:
        return True
    order, stack = [], [root]
    while stack:
        v = stack.pop()
        order.append(v)
        if left[v] != none:
            stack.append(left[v])
        if right[v] != none:
            stack.append(right[v])
    lo = {}
    hi = {}
    for v in reversed(order):
        mn = mx = key[v]
        l, r = left[v], right[v]
        if l != none:
            if hi[l] >= key[v]:
                return False
            mn = min(mn, lo[l]); mx = max(mx, hi[l])
        if r != none:
            if strict_right:
                if lo[r] <= key[v]:
                    return False
            else:
                if lo[r] < key[v]:
                    return False
            mn = min(mn, lo[r]); mx = max(mx, hi[r])
        lo[v] = mn
        hi[v] = mx
    return True


def ref_2_6(text):
    n, key, left, right = _read_tree_0(text)
    ok = _bst_check(n, key, left, right, 0, -1, True)
    return "CORRECT" if ok else "INCORRECT"


def ref_2_7(text):
    n, key, left, right = _read_tree_0(text)
    ok = _bst_check(n, key, left, right, 0, -1, False)
    return "CORRECT" if ok else "INCORRECT"


def ref_2_10(text):
    n, key, left, right = _read_tree_1(text)
    ok = _bst_check(n, key, left, right, 1, 0, True)
    return "YES" if ok else "NO"


def heights_1(n, left, right):
    h = [0] * (n + 1)
    if n == 0:
        return h
    stack = [(1, False)]
    while stack:
        v, done = stack.pop()
        if done:
            h[v] = 1 + max(h[left[v]], h[right[v]])
            continue
        stack.append((v, True))
        if left[v]:
            stack.append((left[v], False))
        if right[v]:
            stack.append((right[v], False))
    return h


def ref_2_12(text):
    n, key, left, right = _read_tree_1(text)
    h = heights_1(n, left, right)
    return "\n".join(str(h[right[i]] - h[left[i]]) for i in range(1, n + 1))


def ref_2_13_tree(text):
    n, key, left, right = _read_tree_1(text)
    h = heights_1(n, left, right)
    a = 1
    b = right[a]
    if h[right[b]] - h[left[b]] == -1:
        c = left[b]
        right[a] = left[c]
        left[b] = right[c]
        left[c] = a
        right[c] = b
        root = c
    else:
        right[a] = left[b]
        left[b] = a
        root = b
    return root, key, left, right, n


def _read_graph(text, weighted=False, extra=0):
    it = [int(x) for x in text.split()]
    n, m = it[0], it[1]
    k = 2
    edges = []
    for _ in range(m):
        if weighted:
            edges.append((it[k], it[k + 1], it[k + 2])); k += 3
        else:
            edges.append((it[k], it[k + 1])); k += 2
    tail = it[k:k + extra]
    return n, m, edges, tail


class DSU(object):
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.r = [0] * (n + 1)

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True


def ref_3_1(text):
    n, m, edges, tail = _read_graph(text, extra=2)
    d = DSU(n)
    for a, b in edges:
        d.union(a, b)
    u, v = tail
    return "1" if d.find(u) == d.find(v) else "0"


def ref_3_2(text):
    n, m, edges, _ = _read_graph(text)
    d = DSU(n)
    comp = n
    for a, b in edges:
        if d.union(a, b):
            comp -= 1
    return str(comp)


def ref_3_5(text):
    n, m, edges, _ = _read_graph(text)
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
    index = [0] * (n + 1)
    low = [0] * (n + 1)
    on = [False] * (n + 1)
    idx = [1]
    stack = []
    comps = 0
    for s in range(1, n + 1):
        if index[s]:
            continue
        work = [(s, 0)]
        while work:
            v, pi = work[-1]
            if pi == 0:
                index[v] = low[v] = idx[0]
                idx[0] += 1
                stack.append(v)
                on[v] = True
            recurse = False
            for i in range(pi, len(g[v])):
                w = g[v][i]
                if index[w] == 0:
                    work[-1] = (v, i + 1)
                    work.append((w, 0))
                    recurse = True
                    break
                elif on[w] and index[w] < low[v]:
                    low[v] = index[w]
            if recurse:
                continue
            if low[v] == index[v]:
                comps += 1
                while True:
                    w = stack.pop()
                    on[w] = False
                    if w == v:
                        break
            work.pop()
            if work:
                u = work[-1][0]
                if low[v] < low[u]:
                    low[u] = low[v]
    return str(comps)


def ref_3_6(text):
    n, m, edges, tail = _read_graph(text, extra=2)
    g = [[] for _ in range(n + 1)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    u, v = tail
    dist = [-1] * (n + 1)
    dist[u] = 0
    q = deque([u])
    while q:
        x = q.popleft()
        if x == v:
            break
        for y in g[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)
    return str(dist[v])


def ref_3_7(text):
    n, m, edges, _ = _read_graph(text)
    parent = list(range(n + 1))
    rel = [0] * (n + 1)

    def find(x):
        path = []
        while parent[x] != x:
            path.append(x)
            x = parent[x]
        acc = 0
        for y in reversed(path):
            acc ^= rel[y]
            parent[y] = x
            rel[y] = acc
        return x

    ok = True
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            if rel[a] == rel[b]:
                ok = False
        else:
            parent[ra] = rb
            rel[ra] = rel[a] ^ rel[b] ^ 1
    return "1" if ok else "0"


def ref_3_9(text):
    n, m, edges, _ = _read_graph(text, weighted=True)
    dist = [0] * (n + 1)
    for i in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            return "0"
    return "1"


def ref_3_10(text):
    n, m, edges, tail = _read_graph(text, weighted=True, extra=1)
    s = tail[0]
    INF = float("inf")
    dist = [INF] * (n + 1)
    dist[s] = 0
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    bad = set()
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            bad.add(v)
    g = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        g[u].append(v)
    q = deque(bad)
    while q:
        x = q.popleft()
        for y in g[x]:
            if y not in bad:
                bad.add(y)
                q.append(y)
    out = []
    for i in range(1, n + 1):
        if dist[i] == INF:
            out.append("*")
        elif i in bad:
            out.append("-")
        else:
            out.append(str(dist[i]))
    return "\n".join(out)


def ref_3_15(text):
    lines = text.splitlines()
    n, m = map(int, lines[0].split())
    grid = [lines[1 + i] for i in range(n)]
    qx, qy, L = map(int, lines[1 + n].split())
    heroes = [tuple(map(int, lines[2 + n + i].split())) for i in range(4)]
    INF = float("inf")
    dist = [[INF] * m for _ in range(n)]
    dist[qx - 1][qy - 1] = 0
    q = deque([(qx - 1, qy - 1)])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            a, b = x + dx, y + dy
            if 0 <= a < n and 0 <= b < m and grid[a][b] == '0' and dist[a][b] == INF:
                dist[a][b] = dist[x][y] + 1
                q.append((a, b))
    total = 0
    for ax, ay, p in heroes:
        if dist[ax - 1][ay - 1] <= L:
            total += p
    return str(total)


def _find_all(t, p):
    res = []
    if not p or len(p) > len(t):
        return res
    i = t.find(p)
    while i != -1:
        res.append(i + 1)
        i = t.find(p, i + 1)
    return res


def _occ_output(t, p):
    res = _find_all(t, p)
    return "%d\n%s" % (len(res), " ".join(map(str, res)))


def ref_4_1(text):
    lines = text.split()
    return _occ_output(lines[1], lines[0])


def ref_4_2(text):
    s = text.strip("\n").replace(" ", "")
    n = len(s)
    left = [0] * 26
    right = [0] * 26
    for ch in s:
        right[ord(ch) - 97] += 1
    total = 0
    for i, ch in enumerate(s):
        c = ord(ch) - 97
        right[c] -= 1
        for k in range(26):
            total += left[k] * right[k]
        left[c] += 1
    return str(total)


def ref_4_3(text):
    parts = text.split()
    return _occ_output(parts[1], parts[0])


def ref_4_4(text):
    data = text.split()
    s = data[0]
    q = int(data[1])
    out = []
    k = 2
    for _ in range(q):
        a, b, l = int(data[k]), int(data[k + 1]), int(data[k + 2])
        k += 3
        out.append("Yes" if s[a:a + l] == s[b:b + l] else "No")
    return "\n".join(out)


def prefix_function(s):
    n = len(s)
    pi = [0] * n
    k = 0
    for i in range(1, n):
        c = s[i]
        while k and c != s[k]:
            k = pi[k - 1]
        if c == s[k]:
            k += 1
        pi[i] = k
    return pi


def z_function(s):
    n = len(s)
    z = [0] * n
    if n:
        z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def pi_from_z(s):
    n = len(s)
    z = z_function(s)
    pi = [0] * n
    for i in range(n - 1, 0, -1):
        if z[i] > 0:
            pi[i + z[i] - 1] = max(pi[i + z[i] - 1], z[i])
    for i in range(n - 2, 0, -1):
        if pi[i] < pi[i + 1] - 1:
            pi[i] = pi[i + 1] - 1
    return pi


def z_from_pi(s):
    n = len(s)
    pi = prefix_function(s)
    z = [0] * n
    for i in range(n - 1, 0, -1):
        if pi[i]:
            z[i - pi[i] + 1] = max(z[i - pi[i] + 1], pi[i])
    if n:
        z[0] = n
    i = 1
    while i < n:
        t = i
        if z[i] > 0:
            for j in range(1, z[i]):
                if z[i + j] > z[j]:
                    break
                z[i + j] = min(z[j], z[i] - j)
                t = i + j
        i = t + 1
    return z


def ref_4_5(text):
    s = text.split("\n")[0].strip()
    return " ".join(map(str, pi_from_z(s)))


def ref_4_6(text):
    s = text.split("\n")[0].strip()
    return " ".join(map(str, z_from_pi(s)[1:]))


def lcs_length(s, t):
    if not s or not t:
        return 0
    MAXN = 2 * len(s) + 5
    nxt = [dict() for _ in range(MAXN)]
    link = [-1] * MAXN
    length = [0] * MAXN
    last = 0
    size = 1
    for ch in s:
        cur = size
        size += 1
        length[cur] = length[last] + 1
        p = last
        while p != -1 and ch not in nxt[p]:
            nxt[p][ch] = cur
            p = link[p]
        if p == -1:
            link[cur] = 0
        else:
            q = nxt[p][ch]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:
                clone = size
                size += 1
                length[clone] = length[p] + 1
                nxt[clone] = dict(nxt[q])
                link[clone] = link[q]
                while p != -1 and nxt[p].get(ch) == q:
                    nxt[p][ch] = clone
                    p = link[p]
                link[q] = clone
                link[cur] = clone
        last = cur
    v, l, best = 0, 0, 0
    for ch in t:
        while v and ch not in nxt[v]:
            v = link[v]
            l = length[v]
        if ch in nxt[v]:
            v = nxt[v][ch]
            l += 1
        else:
            v, l = 0, 0
        if l > best:
            best = l
    return best


def decomposition_cost(s):
    n = len(s)
    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[0] = 0
    for i in range(n):
        if dp[i] == INF:
            continue
        base = dp[i] + (1 if i > 0 else 0)
        sub = s[i:]
        pi = prefix_function(sub)
        for L in range(1, n - i + 1):
            cost = base + L
            k = pi[L - 1]
            p = L - k
            if k and L % p == 0:
                packed = base + p + 1 + len(str(L // p))
                if packed < cost:
                    cost = packed
            if cost < dp[i + L]:
                dp[i + L] = cost
    return dp[n]
