
import random
from gen.util import put, clear
import refs


def build():
    gen_1_1(); gen_1_2(); gen_1_3(); gen_1_8(); gen_1_10()
    gen_1_11(); gen_1_12(); gen_1_16(); gen_1_17()


def gen_1_1():
    pid = "1.1"; clear(pid)
    put(pid, "01_sample1", "3 50\n60 20\n100 50\n120 30")
    put(pid, "02_sample2", "1 10\n500 30")

    put(pid, "03_zero_capacity", "3 0\n60 20\n100 50\n120 30")

    put(pid, "04_all_fits", "4 1000\n10 1\n20 2\n30 3\n40 4")

    put(pid, "05_zero_prices", "3 10\n0 5\n0 5\n0 5")

    put(pid, "06_zero_weight", "3 5\n1000000 0\n10 5\n20 10")

    put(pid, "07_repeating_fraction", "1 1\n1 3")

    put(pid, "08_equal_ratios", "5 7\n10 5\n4 2\n2 1\n20 10\n6 3")

    lines = ["1000 2000000"] + ["2000000 2000000"] * 1000
    put(pid, "09_max_values", "\n".join(lines))

    put(pid, "10_greedy_trap", "3 10\n100 10\n60 3\n60 3")
    rnd = random.Random(101)
    rows = ["1000 2000000"]
    for _ in range(1000):
        rows.append("%d %d" % (rnd.randint(0, 2000000), rnd.randint(1, 2000000)))
    put(pid, "big_11_random_max", "\n".join(rows))

    rows = ["1000 999999"] + ["%d %d" % (i + 1, 1) for i in range(1000)]
    put(pid, "12_tiny_weights", "\n".join(rows))


def gen_1_2():
    pid = "1.2"; clear(pid)
    r = refs.ref_1_2
    put(pid, "01_sample1", "950\n400\n4\n200 375 550 750", ref=r, expect="2")
    put(pid, "02_sample2", "10\n3\n4\n1 2 5 9", ref=r, expect="-1")
    put(pid, "03_sample3", "200\n250\n2\n100 150", ref=r, expect="0")

    put(pid, "04_exact_to_finish", "400\n400\n2\n100 200", ref=r, expect="0")

    put(pid, "05_exact_gaps", "300\n100\n2\n100 200", ref=r, expect="2")

    put(pid, "06_last_gap_too_long", "1000\n400\n2\n300 500", ref=r, expect="-1")

    put(pid, "07_first_unreachable", "1000\n100\n2\n500 600", ref=r, expect="-1")

    put(pid, "08_edge_plus_one", "401\n400\n1\n400", ref=r, expect="1")
    put(pid, "09_single_stop", "8\n5\n1\n4", ref=r, expect="1")

    put(pid, "10_dense_then_gap", "1000\n400\n5\n2 3 4 5 700", ref=r, expect="-1")

    stops = [350 * k for k in range(1, 286)]
    put(pid, "11_max_stops", "100000\n400\n%d\n%s" % (len(stops), " ".join(map(str, stops))),
        ref=r)

    put(pid, "12_skip_near_stop", "100\n50\n3\n10 45 60", ref=r, expect="2")
    put(pid, "13_m_small", "8\n2\n3\n2 4 6", ref=r, expect="3")

    stops = sorted(random.Random(7).sample(range(2, 99999), 300))
    put(pid, "14_n_300_random", "100000\n400\n300\n%s" % " ".join(map(str, stops)), ref=r)


def gen_1_3():
    pid = "1.3"; clear(pid)
    r = refs.ref_1_3
    put(pid, "01_sample1", "1\n23\n39", ref=r, expect="897")
    put(pid, "02_sample2", "3\n1 3 -5\n-2 4 1", ref=r, expect="23")
    put(pid, "03_all_negative", "4\n-1 -2 -3 -4\n-5 -6 -7 -8", ref=r)
    put(pid, "04_zeros", "3\n0 0 0\n-100000 0 100000", ref=r)
    put(pid, "05_single_negative", "1\n-100000\n-100000", ref=r, expect="10000000000")
    put(pid, "06_mixed_signs", "5\n-100000 -1 0 1 100000\n-100000 -1 0 1 100000", ref=r)

    a = " ".join(["100000"] * 1000)
    b = " ".join(["100000"] * 1000)
    put(pid, "07_max_magnitude", "1000\n%s\n%s" % (a, b), ref=r, expect="10000000000000")
    rnd = random.Random(3)
    a = [rnd.randint(-100000, 100000) for _ in range(1000)]
    b = [rnd.randint(-100000, 100000) for _ in range(1000)]
    put(pid, "08_random_max", "1000\n%s\n%s" % (
        " ".join(map(str, a)), " ".join(map(str, b))), ref=r)

    a = [-100000] * 500 + [100000] * 500
    b = [100000] * 500 + [-100000] * 500
    put(pid, "09_sign_pairing", "1000\n%s\n%s" % (
        " ".join(map(str, a)), " ".join(map(str, b))), ref=r, expect="10000000000000")


def gen_1_8():
    pid = "1.8"; clear(pid)
    r = refs.ref_1_8
    put(pid, "01_sample1", "1\n5 10", ref=r, expect="1")
    put(pid, "02_sample2", "3\n1 5\n2 3\n3 4", ref=r, expect="2")

    put(pid, "03_touching", "3\n1 5\n5 10\n10 20", ref=r, expect="3")

    put(pid, "04_identical", "5\n10 20\n10 20\n10 20\n10 20\n10 20", ref=r, expect="1")

    put(pid, "05_nested", "4\n1 100\n10 20\n30 40\n50 60", ref=r, expect="3")

    segs = ["1 1440"] + ["%d %d" % (i, i + 1) for i in range(1, 1000)]
    put(pid, "06_long_plus_short", "%d\n%s" % (len(segs), "\n".join(segs)), ref=r, expect="999")

    segs = ["%d %d" % (1, 1440) for _ in range(1000)]
    put(pid, "07_all_overlap", "1000\n%s" % "\n".join(segs), ref=r, expect="1")
    rnd = random.Random(11)
    segs = []
    for _ in range(1000):
        s = rnd.randint(1, 1439)
        f = rnd.randint(s + 1, 1440)
        segs.append("%d %d" % (s, f))
    put(pid, "08_random_max", "1000\n%s" % "\n".join(segs), ref=r)

    segs = ["%d %d" % (i, i + 1) for i in range(1, 1001)]
    put(pid, "09_unit_chain", "1000\n%s" % "\n".join(segs), ref=r, expect="1000")

    put(pid, "10_greedy_by_start_trap", "3\n1 1440\n2 3\n4 5", ref=r, expect="2")


def gen_1_10():
    pid = "1.10"; clear(pid)
    put(pid, "01_sample1", "3 5\n2 3\n10 5\n5 10")
    put(pid, "02_sample2", "3 5\n2 3\n10 5\n5 6")

    put(pid, "03_order_by_a_trap", "2 5\n4 1\n3 10")

    put(pid, "04_all_gainers", "3 2\n1 100\n50 60\n100 200")

    put(pid, "05_all_losers", "3 20\n5 4\n6 1\n7 3")

    put(pid, "06_exact_zero", "1 5\n5 100")
    put(pid, "07_single_ok", "1 6\n5 100")
    put(pid, "08_single_bad", "1 1\n1 1000")

    rnd = random.Random(21)
    rows = []
    for _ in range(1000):
        a = rnd.randint(1, 1000)
        rows.append("%d %d" % (a, min(1000, a + rnd.randint(0, 5))))
    put(pid, "09_max_tight", "1000 1000\n%s" % "\n".join(rows))

    rows = ["1000 1" for _ in range(1000)]
    put(pid, "10_max_impossible", "1000 1000\n%s" % "\n".join(rows))

    rows = ["%d %d" % (i, i * 2) for i in range(1, 501)] +\
           ["%d %d" % (1000, 1) for _ in range(500)]
    put(pid, "11_max_mixed", "1000 2\n%s" % "\n".join(rows))

    put(pid, "12_one_valid_start", "3 3\n2 1000\n900 1\n950 1")


def gen_1_11():
    pid = "1.11"; clear(pid)
    r = refs.ref_1_11
    put(pid, "01_sample", "10 3\n1 4 8", ref=r, expect="9")

    put(pid, "02_all_too_heavy", "10 3\n100000 11 50", ref=r, expect="0")

    put(pid, "03_exact_fill", "10000 4\n5000 3000 2000 9999", ref=r, expect="10000")

    put(pid, "04_zero_weights", "10 4\n0 0 3 7", ref=r, expect="10")
    put(pid, "05_single_item", "1 1\n1", ref=r, expect="1")

    put(pid, "06_greedy_trap", "10 3\n7 5 5", ref=r, expect="10")

    put(pid, "07_parity_gap", "9999 3\n4000 4000 2000", ref=r, expect="8000")

    put(pid, "big_08_worst_time", "10000 300\n%s" % " ".join(["1"] * 300), ref=r, expect="300")
    rnd = random.Random(31)
    ws = [rnd.randint(1, 100000) for _ in range(300)]
    put(pid, "big_09_random_max", "10000 300\n%s" % " ".join(map(str, ws)), ref=r)
    ws = [rnd.randint(1, 60) for _ in range(300)]
    put(pid, "big_10_dense_max", "10000 300\n%s" % " ".join(map(str, ws)), ref=r)


def gen_1_12():
    pid = "1.12"; clear(pid)
    put(pid, "01_sample", "3\n1 2 3")
    put(pid, "02_odd_sum", "3\n1 2 2")
    put(pid, "03_n1", "1\n1")
    put(pid, "04_two_ones", "2\n1 1")
    put(pid, "05_two_odd", "2\n1 2")
    put(pid, "06_all_ones_even", "10\n%s" % " ".join(["1"] * 10))
    put(pid, "07_all_ones_odd", "9\n%s" % " ".join(["1"] * 9))

    put(pid, "08_a_equals_i", "1000\n%s" % " ".join(str(i) for i in range(1, 1001)))
    rnd = random.Random(41)
    a = [rnd.randint(1, i) for i in range(1, 40001)]
    if sum(a) % 2:
        a[1] = 3 - a[1]
    put(pid, "big_09_max_random", "40000\n%s" % " ".join(map(str, a)))
    a = [i for i in range(1, 40001)]
    put(pid, "big_10_max_a_equals_i", "40000\n%s" % " ".join(map(str, a)))

    a = [1] * 100
    a[99] = 100
    put(pid, "11_one_big_element", "100\n%s" % " ".join(map(str, a)))
    put(pid, "12_all_ones_40000", "40000\n%s" % " ".join(["1"] * 40000))


def _matrix(n, vals):
    rows = [" ".join(str(vals[i][j]) for j in range(n)) for i in range(n)]
    return "%d\n%s" % (n, "\n".join(rows))


def _sym_random(n, rnd, lo=1, hi=1000000):
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j] = a[j][i] = rnd.randint(lo, hi)
    return a


def gen_1_16():
    pid = "1.16"; clear(pid)
    put(pid, "01_sample", "5\n0 183 163 173 181\n183 0 165 172 171\n"
                          "163 165 0 189 302\n173 172 189 0 167\n181 171 302 167 0")
    put(pid, "02_n1", "1\n0")
    put(pid, "03_n2", "2\n0 7\n7 0")
    put(pid, "04_all_zeros", "4\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0")

    put(pid, "05_nearest_neighbour_trap",
        "4\n0 1 100 100\n1 0 2 100\n100 2 0 3\n100 100 3 0")
    rnd = random.Random(51)
    put(pid, "06_n8_random", _matrix(8, _sym_random(8, rnd)))
    put(pid, "07_n10_random", _matrix(10, _sym_random(10, rnd)))

    a = _sym_random(13, rnd, 999000, 1000000)
    put(pid, "big_08_n13_max_weights", _matrix(13, a))
    put(pid, "big_09_n13_random", _matrix(13, _sym_random(13, rnd)))

    n = 12
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            same = (i < 6) == (j < 6)
            a[i][j] = a[j][i] = rnd.randint(1, 10) if same else rnd.randint(900, 1000)
    put(pid, "big_10_two_clusters", _matrix(n, a))


def gen_1_17():
    pid = "1.17"; clear(pid)
    r = refs.ref_1_17
    put(pid, "01_n1", "1", ref=r, expect="8")
    put(pid, "02_n2", "2", ref=r, expect="16")
    put(pid, "03_n3", "3", ref=r)
    put(pid, "04_n4", "4", ref=r)
    put(pid, "05_n10", "10", ref=r)
    put(pid, "06_n100", "100", ref=r)
    put(pid, "07_n999", "999", ref=r)
    put(pid, "08_n1000", "1000", ref=r)

    put(pid, "09_n50", "50", ref=r)
