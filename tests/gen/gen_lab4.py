
import random
import string
from gen.util import put, clear
import refs

LOWER = string.ascii_lowercase


def rand_str(n, rnd, alphabet=LOWER):
    return "".join(rnd.choice(alphabet) for _ in range(n))


def fibonacci_word(limit):
    a, b = "a", "ab"
    while len(b) < limit:
        a, b = b, b + a
    return b[:limit]


def thue_morse(limit):
    s = "a"
    while len(s) < limit:
        s += "".join("b" if c == "a" else "a" for c in s)
    return s[:limit]


def build():
    gen_4_1(); gen_4_2(); gen_4_3(); gen_4_4(); gen_4_5(); gen_4_6(); gen_4_7(); gen_4_9()


def gen_4_1():
    pid = "4.1"; clear(pid)
    r = refs.ref_4_1
    put(pid, "01_sample", "aba\nabaCaba", ref=r, expect="2\n1 5")

    put(pid, "02_pattern_longer", "abcdef\nabc", ref=r, expect="0")
    put(pid, "03_equal", "abc\nabc", ref=r, expect="1\n1")

    put(pid, "04_overlapping", "aaa\naaaaa", ref=r, expect="3\n1 2 3")
    put(pid, "05_no_match", "xyz\nabcabcabc", ref=r, expect="0")

    put(pid, "06_case_sensitive", "Abc\nabcAbcABC", ref=r, expect="1\n4")

    put(pid, "07_single_char_max", "a\n%s" % ("a" * 10000), ref=r)

    put(pid, "08_last_char_differs", "%s\n%s" % ("a" * 100 + "b", "a" * 100 + "c"), ref=r,
        expect="0")
    rnd = random.Random(401)
    put(pid, "09_random_small_alphabet", "%s\n%s" % (rand_str(3, rnd, "ab"),
                                                     rand_str(10000, rnd, "ab")), ref=r)

    put(pid, "big_10_worst_naive", "%s\n%s" % ("a" * 5000, "a" * 10000), ref=r)

    put(pid, "big_11_near_miss", "%s\n%s" % ("a" * 99 + "b", ("a" * 99 + "c") * 100), ref=r,
        expect="0")
    put(pid, "big_12_periodic", "%s\n%s" % ("a" * 99 + "b", ("a" * 99 + "b") * 100), ref=r)


def gen_4_2():
    pid = "4.2"; clear(pid)
    r = refs.ref_4_2
    put(pid, "01_sample1", "treasure", ref=r, expect="8")
    put(pid, "02_sample2", "you will never find the treasure", ref=r, expect="146")
    put(pid, "03_too_short", "ab", ref=r, expect="0")
    put(pid, "04_single_letter", "a", ref=r, expect="0")
    put(pid, "05_aaa", "aaa", ref=r, expect="1")
    put(pid, "06_aba", "aba", ref=r, expect="1")
    put(pid, "07_all_different", "abc", ref=r, expect="0")

    put(pid, "08_spaces_join", "a b a", ref=r, expect="1")
    put(pid, "09_spaces_only_words", "ab ba ab", ref=r)
    rnd = random.Random(402)

    n = 300000
    put(pid, "big_10_all_same", "a" * n, ref=r, expect=str(n * (n - 1) * (n - 2) // 6))
    put(pid, "big_11_two_letters", "ab" * (n // 2), ref=r)
    put(pid, "big_12_random_lower", rand_str(n, rnd), ref=r)

    words = [rand_str(3, rnd) for _ in range(n // 4)]
    put(pid, "big_13_many_spaces", " ".join(words)[:n].strip(), ref=r)


def gen_4_3():
    pid = "4.3"; clear(pid)
    r = refs.ref_4_3
    put(pid, "01_sample1", "aba\nabacaba", ref=r, expect="2\n1 5")
    put(pid, "02_sample2", "Test\ntestTesttesT", ref=r, expect="1\n5")
    put(pid, "03_sample3", "aaaaa\nbaaaaaaa", ref=r, expect="3\n2 3 4")
    put(pid, "04_pattern_longer", "abcabc\nabc", ref=r, expect="0")
    put(pid, "05_equal", "abcabc\nabcabc", ref=r, expect="1\n1")
    put(pid, "06_single_char_pattern", "z\nzzazz", ref=r, expect="4\n1 2 4 5")
    rnd = random.Random(403)

    t = list(rand_str(10 ** 6, rnd, "ab"))
    p = rand_str(30, rnd, "ab")
    for pos in (0, 250000, 999970):
        t[pos:pos + 30] = list(p)
    put(pid, "big_07_text_1e6", "%s\n%s" % (p, "".join(t)), ref=r)

    put(pid, "big_08_many_matches", "%s\n%s" % ("a" * 1000, "a" * 500000), ref=r)

    put(pid, "big_09_near_miss", "%s\n%s" % ("a" * 999 + "b", ("a" * 999 + "c") * 1000), ref=r,
        expect="0")
    put(pid, "big_10_periodic", "%s\n%s" % ("ab" * 5, "ab" * 500000), ref=r)

    put(pid, "big_11_case", "%s\n%s" % ("AB" * 5, "ab" * 500000), ref=r, expect="0")


def gen_4_4():
    pid = "4.4"; clear(pid)
    r = refs.ref_4_4
    put(pid, "01_sample", "trololo\n4\n0 0 7\n2 4 3\n3 5 1\n1 3 2", ref=r,
        expect="Yes\nYes\nYes\nNo")
    put(pid, "02_single_char", "a\n2\n0 0 1\n0 0 0", ref=r, expect="Yes\nYes")

    put(pid, "03_zero_length", "abcd\n3\n0 3 0\n1 1 0\n0 0 4", ref=r, expect="Yes\nYes\nYes")

    put(pid, "04_last_char", "aaaaab\n2\n0 1 5\n0 0 6", ref=r, expect="No\nYes")
    put(pid, "05_full_length", "abcabc\n2\n0 3 3\n0 0 6", ref=r, expect="Yes\nYes")
    rnd = random.Random(404)
    n = 500000
    q = 100000

    lines = ["a" * n, str(q)]
    for _ in range(q):
        l = rnd.randint(1, 1000)
        lines.append("%d %d %d" % (rnd.randint(0, n - l), rnd.randint(0, n - l), l))
    put(pid, "big_06_all_same_max", "\n".join(lines), ref=r)

    s = rand_str(n, rnd, "ab")
    lines = [s, str(q)]
    for _ in range(q):
        l = rnd.randint(1, 50)
        lines.append("%d %d %d" % (rnd.randint(0, n - l), rnd.randint(0, n - l), l))
    put(pid, "big_07_random_short_queries", "\n".join(lines), ref=r)

    s = "abc" * (n // 3)
    lines = [s, str(q)]
    for i in range(q):
        l = rnd.randint(1, 5000)
        a = rnd.randint(0, len(s) - l - 3)
        shift = 3 if i % 2 == 0 else 1
        lines.append("%d %d %d" % (a, a + shift, l))
    put(pid, "big_08_periodic", "\n".join(lines), ref=r)

    s = rand_str(n, rnd, LOWER)
    lines = [s, "1000"]
    for _ in range(1000):
        l = rnd.randint(n - 10, n)
        lines.append("%d %d %d" % (rnd.randint(0, n - l), rnd.randint(0, n - l), l))
    put(pid, "big_09_long_substrings", "\n".join(lines), ref=r)

    lines = [s, "1000"]
    for _ in range(1000):
        l = rnd.randint(1, n)
        a = rnd.randint(0, n - l)
        lines.append("%d %d %d" % (a, a, l))
    put(pid, "big_10_same_index", "\n".join(lines), ref=r)


def _string_suite(pid, ref, min_len=1):
    rnd = random.Random(405)
    n = 10 ** 6
    put(pid, "03_two_chars", "ab", ref=ref)
    put(pid, "04_repeat_two", "aaaa", ref=ref)
    put(pid, "05_mixed_case", "aAaAaA", ref=ref)
    put(pid, "06_periodic_small", "abcabcabcabc", ref=ref)
    put(pid, "07_almost_period", "aaaaab", ref=ref)
    mid = 3 * 10 ** 5

    put(pid, "big_08_all_same_1e6", "a" * n, ref=ref)
    put(pid, "big_09_fibonacci_1e6", fibonacci_word(n), ref=ref)
    put(pid, "big_10_random_full_1e6", rand_str(n, rnd, LOWER), ref=ref)
    put(pid, "big_11_thue_morse", thue_morse(mid), ref=ref)
    put(pid, "big_12_random_binary", rand_str(mid, rnd, "ab"), ref=ref)
    put(pid, "big_13_blocks", ("a" * 999 + "b") * 300, ref=ref)
    put(pid, "big_14_ab_alternating", "ab" * (mid // 2), ref=ref)


def gen_4_5():
    pid = "4.5"; clear(pid)
    r = refs.ref_4_5
    put(pid, "01_sample1", "aaaAAA", ref=r, expect="0 1 2 0 0 0")
    put(pid, "02_sample2", "abacaba", ref=r, expect="0 0 1 0 1 2 3")
    _string_suite(pid, r)
    put(pid, "15_single_char", "z", ref=r, expect="0")


def gen_4_6():
    pid = "4.6"; clear(pid)
    r = refs.ref_4_6
    put(pid, "01_sample1", "aaaAAA", ref=r, expect="2 1 0 0 0")
    put(pid, "02_sample2", "abacaba", ref=r, expect="0 1 0 3 0 1")
    _string_suite(pid, r, min_len=2)


def gen_4_7():
    pid = "4.7"; clear(pid)
    put(pid, "01_sample", "cool toolbox\naaa bb\naabaa babbaab")

    put(pid, "02_identical", "abcabc abcabc")

    put(pid, "03_disjoint_alphabets", "aaaa bbbb")

    put(pid, "04_one_common_char", "abc cde")

    put(pid, "05_common_at_end", "xxxxxabc yyyyyabc")
    rnd = random.Random(407)

    lines = ["%s %s" % (rand_str(20, rnd, "abc"), rand_str(20, rnd, "abc")) for _ in range(1000)]
    put(pid, "06_many_short_lines", "\n".join(lines))

    put(pid, "big_07_equal_50k", "%s %s" % ("a" * 50000, "a" * 50000))

    put(pid, "big_08_random_50k", "%s %s" % (rand_str(50000, rnd, "ab"),
                                             rand_str(50000, rnd, "ab")))

    common = rand_str(20000, rnd, "ab")
    s = rand_str(15000, rnd, "ab") + common + rand_str(15000, rnd, "ab")
    t = rand_str(15000, rnd, "ab") + common + rand_str(15000, rnd, "ab")
    put(pid, "big_09_long_common", "%s %s" % (s, t))

    put(pid, "big_10_periodic_shift", "%s %s" % ("ab" * 25000, "ba" * 25000))

    put(pid, "big_11_asymmetric", "%s %s" % (rand_str(90000, rnd, "ab"),
                                             rand_str(10000, rnd, "ab")))


def gen_4_9():
    pid = "4.9"; clear(pid)
    put(pid, "01_sample1", "ABCABCDEDEDEF")
    put(pid, "02_sample2", "Hello")
    put(pid, "03_single", "A")

    put(pid, "04_two_same", "aa")
    put(pid, "05_three_same", "aaa")

    put(pid, "06_two_digit_multiplier", "ab" * 15)

    put(pid, "07_nested_repeats", ("ab" * 10 + "c") * 10)

    put(pid, "08_long_period_twice", "abcdefghij" * 2)
    put(pid, "09_prefix_trap", "aaaaabaaaaab")
    rnd = random.Random(409)
    put(pid, "10_random_200", rand_str(200, rnd, "ab"))
    put(pid, "11_random_200_wide", rand_str(200, rnd, LOWER))

    put(pid, "big_12_all_same_5000", "a" * 5000)
    put(pid, "big_13_periodic_5000", "abcde" * 1000)
    put(pid, "big_14_random_5000", rand_str(5000, rnd, "ab"))
