


def dump(n, edges, tail=None):
    lines = ["%d %d" % (n, len(edges))]
    for e in edges:
        lines.append(" ".join(str(x) for x in e))
    if tail:
        lines.append(" ".join(str(x) for x in tail))
    return "\n".join(lines)


def random_simple(n, m, rnd, directed=False, allow_antiparallel=True):
    seen = set()
    edges = []
    guard = 0
    while len(edges) < m and guard < 50 * m + 1000:
        guard += 1
        u = rnd.randint(1, n)
        v = rnd.randint(1, n)
        if u == v:
            continue
        key = (u, v) if directed and allow_antiparallel else (min(u, v), max(u, v))
        if key in seen:
            continue
        seen.add(key)
        edges.append((u, v))
    return edges


def path_edges(n, directed=False):
    return [(i, i + 1) for i in range(1, n)]


def cycle_edges(n):
    return [(i, i % n + 1) for i in range(1, n + 1)]


def star_edges(n):
    return [(1, i) for i in range(2, n + 1)]


def complete_bipartite(a, b):
    return [(i, a + j) for i in range(1, a + 1) for j in range(1, b + 1)]
