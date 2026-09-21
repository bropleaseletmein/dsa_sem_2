
import random
from gen.util import put, clear
from gen import graphs as G
import refs


def build():
    gen_3_1(); gen_3_2(); gen_3_5(); gen_3_6(); gen_3_7(); gen_3_9(); gen_3_10()


def gen_3_1():
    pid = "3.1"; clear(pid)
    r = refs.ref_3_1
    put(pid, "01_sample1", "4 4\n1 2\n3 2\n4 3\n1 4\n1 4", ref=r, expect="1")
    put(pid, "02_sample2", "4 2\n1 2\n3 2\n1 4", ref=r, expect="0")

    put(pid, "03_min_connected", "2 1\n1 2\n1 2", ref=r, expect="1")
    put(pid, "04_min_disconnected", "2 1\n2 1\n1 2", ref=r, expect="1")

    n = 1000
    put(pid, "05_long_path", G.dump(n, G.path_edges(n), (1, n)), ref=r, expect="1")

    edges = G.path_edges(500) + [(i, i + 1) for i in range(501, 1000)]
    put(pid, "06_two_components", G.dump(1000, edges, (1, 1000)), ref=r, expect="0")

    put(pid, "07_star", G.dump(1000, G.star_edges(1000), (2, 1000)), ref=r, expect="1")
    rnd = random.Random(301)

    edges = G.random_simple(1000, 1000, rnd)
    put(pid, "08_random_max", G.dump(1000, edges, (1, 1000)), ref=r)

    edges = G.random_simple(999, 999, rnd)
    put(pid, "09_isolated_target", G.dump(1000, edges, (1, 1000)), ref=r, expect="0")

    put(pid, "10_cycle", G.dump(1000, G.cycle_edges(1000), (1, 500)), ref=r, expect="1")


def gen_3_2():
    pid = "3.2"; clear(pid)
    r = refs.ref_3_2
    put(pid, "01_sample", "4 2\n1 2\n3 2", ref=r, expect="2")
    put(pid, "02_no_edges", "1000 0", ref=r, expect="1000")
    put(pid, "03_single_vertex", "1 0", ref=r, expect="1")
    put(pid, "04_path_all", G.dump(1000, G.path_edges(1000)), ref=r, expect="1")

    edges = [(2 * i - 1, 2 * i) for i in range(1, 501)]
    put(pid, "05_pairs", G.dump(1000, edges), ref=r, expect="500")

    put(pid, "06_cycle_plus_isolated", G.dump(1000, G.cycle_edges(600)), ref=r, expect="401")
    rnd = random.Random(302)
    put(pid, "07_random_max", G.dump(1000, G.random_simple(1000, 1000, rnd)), ref=r)

    edges = [(i, j) for i in range(1, 46) for j in range(i + 1, 46)][:1000]
    put(pid, "08_clique_plus_isolated", G.dump(1000, edges), ref=r)
    put(pid, "09_two_stars",
        G.dump(1000, G.star_edges(500) + [(500 + 1, i) for i in range(502, 1001)]), ref=r,
        expect="2")


def gen_3_5():
    pid = "3.5"; clear(pid)
    r = refs.ref_3_5
    put(pid, "01_sample1", "4 4\n1 2\n4 1\n2 3\n3 1", ref=r, expect="2")
    put(pid, "02_sample2", "5 7\n2 1\n3 2\n3 1\n4 3\n4 1\n5 2\n5 3", ref=r, expect="5")
    put(pid, "03_single", "1 0", ref=r, expect="1")
    put(pid, "04_no_edges", "1000 0", ref=r, expect="1000")

    n = 10000
    put(pid, "05_big_cycle", G.dump(n, G.cycle_edges(n)), ref=r, expect="1")

    put(pid, "big_06_dag_chain", G.dump(n, G.path_edges(n)), ref=r, expect="%d" % n)

    edges = []
    for k in range(2500):
        b = 4 * k + 1
        edges += [(b, b + 1), (b + 1, b + 2), (b + 2, b + 3), (b + 3, b)]
        if b + 4 <= n:
            edges.append((b + 3, b + 4))
    put(pid, "big_07_cycle_chain", G.dump(n, edges[:10000]), ref=r)

    edges = G.cycle_edges(5000) + [(5000 + i, 5000 + i % 5000 + 1) for i in range(1, 5001)]
    edges.append((1, 5001))
    put(pid, "big_08_two_big_sccs", G.dump(n, edges[:10000]), ref=r)
    rnd = random.Random(305)
    put(pid, "big_09_random_sparse", G.dump(n, G.random_simple(n, 10000, rnd, directed=True)),
        ref=r)

    put(pid, "10_dense_small", G.dump(100, G.random_simple(100, 4000, rnd, directed=True)), ref=r)

    edges = G.cycle_edges(50) + [(50 + i, 50 + i % 50 + 1) for i in range(1, 51)] + [(1, 51), (51, 1)]
    put(pid, "11_butterfly", G.dump(100, edges), ref=r)


def gen_3_6():
    pid = "3.6"; clear(pid)
    r = refs.ref_3_6
    put(pid, "01_sample1", "4 4\n1 2\n4 1\n2 3\n3 1\n2 4", ref=r, expect="2")
    put(pid, "02_sample2", "5 4\n5 2\n1 3\n3 4\n1 4\n3 5", ref=r, expect="-1")
    put(pid, "03_adjacent", "2 1\n1 2\n1 2", ref=r, expect="1")
    put(pid, "04_no_edges", "2 0\n1 2", ref=r, expect="-1")

    n = 10 ** 5
    put(pid, "big_05_long_chain", G.dump(n, G.path_edges(n), (1, n)), ref=r,
        expect="%d" % (n - 1))

    edges = G.path_edges(n)[:n - 1]
    edges.append((1, n // 2))
    put(pid, "big_06_chain_with_shortcut", G.dump(n, edges, (1, n)), ref=r)

    put(pid, "big_07_star", G.dump(n, G.star_edges(n), (2, n)), ref=r, expect="2")
    rnd = random.Random(306)
    put(pid, "big_08_random_max",
        G.dump(n, G.random_simple(n, 10 ** 5, rnd), (1, n)), ref=r)

    edges = G.path_edges(50000) + [(i, i + 1) for i in range(50001, n)]
    put(pid, "big_09_two_components", G.dump(n, edges, (1, n)), ref=r, expect="-1")

    w = 300
    edges = []
    for i in range(w):
        for j in range(w):
            v = i * w + j + 1
            if j + 1 < w:
                edges.append((v, v + 1))
            if i + 1 < w:
                edges.append((v, v + w))
    put(pid, "big_10_grid", G.dump(w * w, edges, (1, w * w)), ref=r, expect="%d" % (2 * (w - 1)))


def gen_3_7():
    pid = "3.7"; clear(pid)
    r = refs.ref_3_7
    put(pid, "01_sample1", "4 4\n1 2\n4 1\n2 3\n3 1", ref=r, expect="0")
    put(pid, "02_sample2", "5 4\n5 2\n4 2\n3 4\n1 4", ref=r, expect="1")
    put(pid, "03_no_edges", "100000 0", ref=r, expect="1")
    put(pid, "04_triangle", "3 3\n1 2\n2 3\n3 1", ref=r, expect="0")
    put(pid, "05_even_cycle", G.dump(4, G.cycle_edges(4)), ref=r, expect="1")

    edges = G.path_edges(99996) + [(99997, 99998), (99998, 99999), (99999, 99997)]
    put(pid, "big_06_odd_cycle_last_component", G.dump(10 ** 5, edges), ref=r, expect="0")

    put(pid, "big_07_even_cycle_1e5", G.dump(10 ** 5, G.cycle_edges(10 ** 5)), ref=r, expect="1")

    put(pid, "big_08_odd_cycle_1e5", G.dump(99999, G.cycle_edges(99999)), ref=r, expect="0")

    put(pid, "big_09_complete_bipartite", G.dump(600, G.complete_bipartite(300, 300)), ref=r,
        expect="1")

    rnd = random.Random(307)
    n = 10 ** 5
    edges = [(rnd.randint(1, i - 1), i) for i in range(2, n + 1)]
    put(pid, "big_10_random_tree", G.dump(n, edges), ref=r, expect="1")

    edges2 = list(edges) + [(1, 2), (2, 3), (1, 3)]
    seen = set()
    uniq = []
    for u, v in edges2:
        k = (min(u, v), max(u, v))
        if k not in seen:
            seen.add(k)
            uniq.append((u, v))
    put(pid, "big_11_tree_plus_triangle", G.dump(n, uniq), ref=r)

    w = 300
    edges = []
    for i in range(w):
        for j in range(w):
            v = i * w + j + 1
            if j + 1 < w:
                edges.append((v, v + 1))
            if i + 1 < w:
                edges.append((v, v + w))
    put(pid, "big_12_grid", G.dump(w * w, edges), ref=r, expect="1")


def gen_3_9():
    pid = "3.9"; clear(pid)
    r = refs.ref_3_9
    put(pid, "01_sample", "4 4\n1 2 -5\n4 1 2\n2 3 2\n3 1 1", ref=r, expect="1")
    put(pid, "02_no_edges", "1000 0", ref=r, expect="0")

    put(pid, "03_negative_edges_dag", "4 4\n1 2 -10000\n2 3 -10000\n3 4 -10000\n1 4 5",
        ref=r, expect="0")

    put(pid, "04_zero_cycle", "3 3\n1 2 -5\n2 3 -5\n3 1 10", ref=r, expect="0")

    put(pid, "05_two_vertex_cycle", "2 2\n1 2 -5\n2 1 1", ref=r, expect="1")

    put(pid, "06_cycle_minus_one", "3 3\n1 2 -5\n2 3 -5\n3 1 9", ref=r, expect="1")

    put(pid, "07_unreachable_cycle", "5 4\n1 2 3\n3 4 -5\n4 5 -5\n5 3 1", ref=r, expect="1")

    n = 1000
    edges = [(i, i + 1, -1) for i in range(1, n)] + [(n, 1, n - 2)]
    edges.reverse()
    put(pid, "08_long_cycle_n1000", G.dump(n, edges), ref=r, expect="1")

    edges = [(i, i + 1, -1) for i in range(1, n)] + [(n, 1, n - 1)]
    edges.reverse()
    put(pid, "09_long_cycle_zero", G.dump(n, edges), ref=r, expect="0")
    rnd = random.Random(309)

    edges = []
    seen = set()
    while len(edges) < 10000:
        u = rnd.randint(1, n - 1)
        v = rnd.randint(u + 1, n)
        if (u, v) in seen:
            continue
        seen.add((u, v))
        edges.append((u, v, rnd.randint(-10000, 10000)))
    put(pid, "big_10_dag_max", G.dump(n, edges), ref=r, expect="0")

    edges2 = list(edges)
    edges2.append((n, 1, -10000))
    put(pid, "big_11_dag_plus_back_edge", G.dump(n, edges2[:10000]), ref=r)

    e = G.random_simple(n, 10000, rnd, directed=True)
    put(pid, "big_12_random_weighted",
        G.dump(n, [(u, v, rnd.randint(-100, 10000)) for u, v in e]), ref=r)


    chain = [(i, i + 1, -10) for i in range(1, n)]
    chain.reverse()
    filler = []
    seen = set((u, v) for u, v, _ in chain)
    while len(filler) < 10000 - len(chain):
        u = rnd.randint(1, n - 1)
        v = rnd.randint(u + 1, n)
        if (u, v) in seen:
            continue
        seen.add((u, v))
        filler.append((u, v, rnd.randint(0, 10000)))
    put(pid, "big_13_worst_order", G.dump(n, chain + filler), ref=r, expect="0")


def gen_3_10():
    pid = "3.10"; clear(pid)
    r = refs.ref_3_10
    put(pid, "01_sample1", "6 7\n1 2 10\n2 3 5\n1 3 100\n3 5 7\n5 4 10\n4 3 -18\n6 1 -1\n1",
        ref=r, expect="0\n10\n-\n-\n-\n*")
    put(pid, "02_sample2", "5 4\n1 2 1\n4 1 2\n2 3 2\n3 1 -5\n4", ref=r,
        expect="-\n-\n-\n0\n*")
    put(pid, "03_single_vertex", "1 0\n1", ref=r, expect="0")
    put(pid, "04_all_unreachable", "4 2\n2 3 5\n3 4 5\n1", ref=r, expect="0\n*\n*\n*")

    put(pid, "05_source_in_cycle", "3 3\n1 2 -1\n2 3 -1\n3 1 -1\n1", ref=r, expect="-\n-\n-")

    put(pid, "06_zero_cycle", "3 3\n1 2 5\n2 3 -5\n3 1 0\n1", ref=r, expect="0\n5\n0")

    n = 1000
    edges = [(i, i + 1, -10 ** 9) for i in range(1, n)]
    put(pid, "07_huge_negative_chain", G.dump(n, edges, (1,)), ref=r)
    edges = [(i, i + 1, 10 ** 9) for i in range(1, n)]
    put(pid, "08_huge_positive_chain", G.dump(n, edges, (1,)), ref=r)

    edges = [(i, i + 1, 1) for i in range(1, n)]
    edges.reverse()
    put(pid, "09_reverse_chain", G.dump(n, edges, (1,)), ref=r)

    edges = [(i, i + 1, 1) for i in range(1, 500)]
    edges += [(500, 501, -1), (501, 502, -1), (502, 500, -1)]
    edges += [(502, 600, 3)]
    edges += [(700, 701, 5)]
    put(pid, "10_downstream_minus_inf", G.dump(1000, edges, (1,)), ref=r)
    rnd = random.Random(310)

    edges = []
    seen = set()
    while len(edges) < 10000:
        u = rnd.randint(1, n - 1)
        v = rnd.randint(u + 1, n)
        if (u, v) in seen:
            continue
        seen.add((u, v))
        edges.append((u, v, rnd.randint(-10 ** 6, 10 ** 6)))
    put(pid, "big_11_max_dag", G.dump(n, edges, (1,)), ref=r)

    edges2 = list(edges[:9998]) + [(n, 2, -10 ** 9), (2, n, 1)]
    put(pid, "big_12_max_with_neg_cycle", G.dump(n, edges2, (1,)), ref=r)

    e = G.random_simple(n, 10000, rnd, directed=True)
    put(pid, "big_13_random_source",
        G.dump(n, [(u, v, rnd.randint(-5, 1000)) for u, v in e], (500,)), ref=r)

    chain = [(i, i + 1, -1000) for i in range(1, n)]
    chain.reverse()
    filler = []
    seen = set((u, v) for u, v, _ in chain)
    while len(filler) < 10000 - len(chain):
        u = rnd.randint(1, n - 1)
        v = rnd.randint(u + 1, n)
        if (u, v) in seen:
            continue
        seen.add((u, v))
        filler.append((u, v, rnd.randint(0, 10 ** 6)))
    put(pid, "big_14_worst_order", G.dump(n, chain + filler, (1,)), ref=r)
