
import random
from gen.util import put, clear
from gen import trees
import refs

INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1


def build():
    gen_2_1(); gen_2_5(); gen_2_6(); gen_2_7(); gen_2_10(); gen_2_12(); gen_2_13()


def _deep_violation(t):
    root_key = t.key[0]
    v = t.right[0]
    assert v != -1
    while t.left[v] != -1:
        v = t.left[v]
    t.key[v] = root_key - 1
    return t


def gen_2_1():
    pid = "2.1"; clear(pid)
    r = refs.ref_2_1
    put(pid, "01_sample1", "5\n4 1 2\n2 3 4\n5 -1 -1\n1 -1 -1\n3 -1 -1", ref=r,
        expect="1 2 3 4 5\n4 2 1 3 5\n1 3 2 5 4")
    put(pid, "02_sample2",
        "10\n0 7 2\n10 -1 -1\n20 -1 6\n30 8 9\n40 3 -1\n50 -1 -1\n60 1 -1\n70 5 4\n"
        "80 -1 -1\n90 -1 -1", ref=r,
        expect="50 70 80 30 90 40 0 20 10 60\n0 70 50 40 30 80 90 20 60 10\n"
               "50 80 90 30 40 70 10 60 20 0")
    put(pid, "03_single", "1\n1000000000 -1 -1", ref=r, expect="1000000000 1000000000 1000000000")

    put(pid, "04_not_bst_duplicates", "5\n7 1 2\n7 3 -1\n7 -1 4\n7 -1 -1\n7 -1 -1", ref=r)
    put(pid, "05_only_left_child", "2\n5 1 -1\n0 -1 -1", ref=r, expect="0 5\n5 0\n0 5")
    put(pid, "06_only_right_child", "2\n5 -1 1\n7 -1 -1", ref=r, expect="5 7\n5 7\n7 5")
    rnd = random.Random(201)
    t, _ = trees.perfect(10)
    put(pid, "07_perfect_1023", trees.dump_zero_based(t, rnd), ref=r)

    put(pid, "big_08_left_chain_1e5", trees.dump_zero_based(trees.chain(10 ** 5, "left")), ref=r)
    put(pid, "big_09_right_chain_1e5", trees.dump_zero_based(trees.chain(10 ** 5, "right")), ref=r)
    put(pid, "big_10_zigzag_1e5", trees.dump_zero_based(trees.zigzag(10 ** 5)), ref=r)
    put(pid, "big_11_random_1e5",
        trees.dump_zero_based(trees.random_bst(10 ** 5, rnd, 0, 10 ** 9), rnd), ref=r)

    put(pid, "12_key_bounds", "3\n0 1 2\n1000000000 -1 -1\n0 -1 -1", ref=r)


def gen_2_5():
    pid = "2.5"; clear(pid)
    r = refs.ref_2_5
    put(pid, "01_sample",
        "insert 2\ninsert 5\ninsert 3\nexists 2\nexists 4\nnext 4\nprev 4\n"
        "delete 5\nnext 4\nprev 4", ref=r, expect="true\nfalse\n5\n3\nnone\n3")
    put(pid, "02_empty_input", "", ref=r, expect="")

    put(pid, "03_empty_tree_queries",
        "exists 1\nnext 1\nprev 1\ndelete 1\nexists 1", ref=r, expect="false\nnone\nnone\nfalse")

    put(pid, "04_duplicates",
        "insert 5\ninsert 5\ninsert 5\nexists 5\ndelete 5\nexists 5\ndelete 5\nexists 5",
        ref=r, expect="true\nfalse\nfalse")

    put(pid, "05_delete_root_two_children",
        "insert 10\ninsert 5\ninsert 15\ninsert 12\ninsert 20\ndelete 10\nexists 10\n"
        "next 10\nprev 10\nnext 11\nprev 13", ref=r, expect="false\n12\n5\n12\n12")

    put(pid, "06_delete_one_child",
        "insert 10\ninsert 5\ninsert 1\ndelete 5\nexists 1\nnext 1\nprev 10\n"
        "insert 20\ninsert 30\ndelete 20\nnext 10\nprev 30", ref=r,
        expect="true\n10\n1\n30\n10")

    put(pid, "07_bounds",
        "insert -1000000000\ninsert 1000000000\ninsert 0\nnext -1000000000\n"
        "prev 1000000000\nnext 1000000000\nprev -1000000000\nexists 0", ref=r,
        expect="0\n0\nnone\nnone\ntrue")

    put(pid, "08_strict_next_prev",
        "insert 1\ninsert 2\ninsert 3\nnext 2\nprev 2\nnext 3\nprev 1", ref=r,
        expect="3\n1\nnone\nnone")

    ops = ["insert %d" % i for i in range(1, 41)]
    ops += ["delete %d" % i for i in range(10, 30)]
    ops += ["next 9", "prev 30", "exists 20", "exists 30"]
    put(pid, "09_chain_then_delete", "\n".join(ops), ref=r, expect="30\n9\nfalse\ntrue")

    rnd = random.Random(205)
    ops = []
    for _ in range(100):
        op = rnd.choice(["insert", "insert", "delete", "exists", "next", "prev"])
        ops.append("%s %d" % (op, rnd.randint(-20, 20)))
    put(pid, "10_random_100_ops", "\n".join(ops), ref=r)

    put(pid, "11_negative_keys",
        "insert -5\ninsert -10\ninsert -1\ndelete -7\nexists -10\nnext -10\nprev -1\n"
        "delete -10\nnext -10\nprev -1", ref=r, expect="true\n-5\n-5\n-5\n-5")


def gen_2_6():
    pid = "2.6"; clear(pid)
    r = refs.ref_2_6
    put(pid, "01_sample_correct", "3\n2 1 2\n1 -1 -1\n3 -1 -1", ref=r, expect="CORRECT")
    put(pid, "02_sample_incorrect", "3\n1 1 2\n2 -1 -1\n3 -1 -1", ref=r, expect="INCORRECT")
    put(pid, "03_sample_empty", "0", ref=r, expect="CORRECT")
    put(pid, "04_sample_right_chain", "5\n1 -1 1\n2 -1 2\n3 -1 3\n4 -1 4\n5 -1 -1", ref=r,
        expect="CORRECT")
    put(pid, "05_sample_perfect", "7\n4 1 2\n2 3 4\n6 5 6\n1 -1 -1\n3 -1 -1\n5 -1 -1\n7 -1 -1",
        ref=r, expect="CORRECT")
    put(pid, "06_sample_grandchild", "4\n4 1 -1\n2 2 3\n1 -1 -1\n5 -1 -1", ref=r,
        expect="INCORRECT")
    put(pid, "07_single", "1\n%d -1 -1" % INT_MAX, ref=r, expect="CORRECT")

    put(pid, "08_int32_bounds", "3\n0 1 2\n%d -1 -1\n%d -1 -1" % (INT_MIN, INT_MAX), ref=r,
        expect="CORRECT")
    put(pid, "09_int32_bounds_bad", "3\n0 1 2\n%d -1 -1\n%d -1 -1" % (INT_MAX, INT_MIN), ref=r,
        expect="INCORRECT")
    rnd = random.Random(206)

    put(pid, "big_10_left_chain_1e5",
        trees.dump_zero_based(trees.chain(10 ** 5, "left")), ref=r, expect="CORRECT")
    put(pid, "big_11_random_1e5",
        trees.dump_zero_based(trees.random_bst(10 ** 5, rnd, -10 ** 9, 10 ** 9), rnd),
        ref=r, expect="CORRECT")

    t = trees.random_bst(10 ** 5, rnd, -10 ** 9, 10 ** 9)
    put(pid, "big_12_deep_violation", trees.dump_zero_based(_deep_violation(t)), ref=r,
        expect="INCORRECT")

    t = trees.chain(10 ** 5, "right")
    t.key[t.size() - 1] = -1
    put(pid, "big_13_chain_last_bad", trees.dump_zero_based(t), ref=r, expect="INCORRECT")


def gen_2_7():
    pid = "2.7"; clear(pid)
    r = refs.ref_2_7
    put(pid, "01_sample_correct", "3\n2 1 2\n1 -1 -1\n3 -1 -1", ref=r, expect="CORRECT")
    put(pid, "02_sample_incorrect", "3\n1 1 2\n2 -1 -1\n3 -1 -1", ref=r, expect="INCORRECT")
    put(pid, "03_sample_dup_right", "3\n2 1 2\n1 -1 -1\n2 -1 -1", ref=r, expect="CORRECT")
    put(pid, "04_sample_dup_left", "3\n2 1 2\n2 -1 -1\n3 -1 -1", ref=r, expect="INCORRECT")
    put(pid, "05_sample_right_chain", "5\n1 -1 1\n2 -1 2\n3 -1 3\n4 -1 4\n5 -1 -1", ref=r,
        expect="CORRECT")
    put(pid, "06_sample_perfect", "7\n4 1 2\n2 3 4\n6 5 6\n1 -1 -1\n3 -1 -1\n5 -1 -1\n7 -1 -1",
        ref=r, expect="CORRECT")
    put(pid, "07_sample_intmax", "1\n2147483647 -1 -1", ref=r, expect="CORRECT")
    put(pid, "08_empty", "0", ref=r, expect="CORRECT")

    n = 1000
    lines = ["%d" % n] + ["7 -1 %d" % (i + 1) for i in range(n - 1)] + ["7 -1 -1"]
    put(pid, "09_all_equal_right_chain", "\n".join(lines), ref=r, expect="CORRECT")

    lines = ["%d" % n] + ["7 %d -1" % (i + 1) for i in range(n - 1)] + ["7 -1 -1"]
    put(pid, "10_all_equal_left_chain", "\n".join(lines), ref=r, expect="INCORRECT")

    put(pid, "11_dup_deeper_right", "3\n2 -1 1\n3 2 -1\n2 -1 -1", ref=r, expect="CORRECT")

    put(pid, "12_dup_hidden_left", "3\n5 1 -1\n3 -1 2\n5 -1 -1", ref=r, expect="INCORRECT")

    put(pid, "13_int32_dup", "3\n%d 1 2\n%d -1 -1\n%d -1 -1" % (INT_MIN, INT_MIN, INT_MIN),
        ref=r, expect="INCORRECT")
    put(pid, "14_int32_dup_right", "2\n%d -1 1\n%d -1 -1" % (INT_MIN, INT_MIN), ref=r,
        expect="CORRECT")
    put(pid, "15_int32_span", "3\n0 1 2\n%d -1 -1\n%d -1 -1" % (INT_MIN, INT_MAX), ref=r,
        expect="CORRECT")
    rnd = random.Random(207)

    keys = sorted(rnd.randint(-1000, 1000) for _ in range(10 ** 5))
    t = trees.chain(10 ** 5, "right")
    for pos, v in enumerate(trees.inorder(t)):
        t.key[v] = keys[pos]
    put(pid, "big_16_many_duplicates", trees.dump_zero_based(t), ref=r, expect="CORRECT")
    t = trees.random_bst(10 ** 5, rnd, -10 ** 9, 10 ** 9)
    put(pid, "big_17_deep_violation", trees.dump_zero_based(_deep_violation(t)), ref=r,
        expect="INCORRECT")
    t = trees.random_bst(10 ** 5, rnd, -10 ** 9, 10 ** 9)
    put(pid, "big_18_random_correct", trees.dump_zero_based(t, rnd), ref=r, expect="CORRECT")


def gen_2_10():
    pid = "2.10"; clear(pid)
    r = refs.ref_2_10
    put(pid, "01_sample_yes", "6\n-2 0 2\n8 4 3\n9 0 0\n3 6 5\n6 0 0\n0 0 0", ref=r, expect="YES")
    put(pid, "02_sample_empty", "0", ref=r, expect="YES")
    put(pid, "03_sample_no", "3\n5 2 3\n6 0 0\n4 0 0", ref=r, expect="NO")
    put(pid, "04_single", "1\n-1000000000 0 0", ref=r, expect="YES")

    put(pid, "05_equal_keys", "3\n5 2 3\n5 0 0\n7 0 0", ref=r, expect="NO")
    put(pid, "06_equal_right", "2\n5 0 2\n5 0 0", ref=r, expect="NO")

    put(pid, "07_grandchild", "4\n4 2 0\n2 3 4\n1 0 0\n5 0 0", ref=r, expect="NO")
    rnd = random.Random(210)

    put(pid, "08_n2000_yes", trees.dump_one_based(trees.random_bst(2000, rnd)), ref=r,
        expect="YES")

    put(pid, "big_09_chain_2e5_yes",
        trees.dump_one_based(trees.chain(2 * 10 ** 5, "right")), ref=r, expect="YES")
    put(pid, "big_10_left_chain_2e5_yes",
        trees.dump_one_based(trees.chain(2 * 10 ** 5, "left"), order="dfs"), ref=r, expect="YES")
    put(pid, "big_11_random_2e5_yes",
        trees.dump_one_based(trees.random_bst(2 * 10 ** 5, rnd)), ref=r, expect="YES")
    t = trees.random_bst(2 * 10 ** 5, rnd)
    put(pid, "big_12_deep_violation", trees.dump_one_based(_deep_violation(t)), ref=r,
        expect="NO")

    t = trees.chain(2 * 10 ** 5, "right")
    t.key[t.size() - 1] = -5
    put(pid, "big_13_chain_last_bad", trees.dump_one_based(t), ref=r, expect="NO")

    t = trees.chain(1000, "right")
    for i in range(t.size()):
        t.key[i] = 42
    put(pid, "14_all_equal", trees.dump_one_based(t), ref=r, expect="NO")


def gen_2_12():
    pid = "2.12"; clear(pid)
    r = refs.ref_2_12
    put(pid, "01_sample", "6\n-2 0 2\n8 4 3\n9 0 0\n3 6 5\n6 0 0\n0 0 0", ref=r,
        expect="3\n-1\n0\n0\n0\n0")
    put(pid, "02_empty", "0", ref=r, expect="")
    put(pid, "03_single", "1\n7 0 0", ref=r, expect="0")

    put(pid, "04_right_chain_10", trees.dump_one_based(trees.chain(10, "right")), ref=r)
    put(pid, "05_left_chain_10", trees.dump_one_based(trees.chain(10, "left")), ref=r)
    t, _ = trees.perfect(5)
    put(pid, "06_perfect_31", trees.dump_one_based(t), ref=r)
    rnd = random.Random(212)
    put(pid, "07_random_1000", trees.dump_one_based(trees.random_bst(1000, rnd)), ref=r)

    put(pid, "08_dfs_numbering",
        trees.dump_one_based(trees.random_bst(500, rnd), order="dfs"), ref=r)
    put(pid, "big_09_chain_2e5", trees.dump_one_based(trees.chain(2 * 10 ** 5, "right")), ref=r)
    put(pid, "big_10_zigzag_2e5", trees.dump_one_based(trees.zigzag(2 * 10 ** 5)), ref=r)
    put(pid, "big_11_random_2e5", trees.dump_one_based(trees.random_bst(2 * 10 ** 5, rnd)), ref=r)

    put(pid, "12_key_bounds", "3\n0 2 3\n-1000000000 0 0\n1000000000 0 0", ref=r,
        expect="0\n0\n0")


def _random_rotation_case(h, rnd, keys_from=1, max_nodes=None):
    while True:
        left_sub = trees.random_avl(h, rnd)
        right_sub = trees.random_avl(h + 2, rnd)
        t = trees.merge(0, left_sub, right_sub)
        if max_nodes is None or t.size() <= max_nodes:
            break
    trees.relabel_bst_keys(t, list(range(keys_from, keys_from + t.size())))
    return t


def _rotation_case(h, kind, rnd=None, keys_from=1):
    left_sub, _ = trees.perfect(h)
    if kind == "small0":
        y, _ = trees.perfect(h + 1)
        z, _ = trees.perfect(h + 1)
    elif kind == "small_plus":
        y, _ = trees.perfect(h)
        z, _ = trees.perfect(h + 1)
    else:
        y, _ = trees.perfect(h + 1)
        z, _ = trees.perfect(h)
    right_sub = trees.merge(0, y, z)
    t = trees.merge(0, left_sub, right_sub)
    n = t.size()
    keys = list(range(keys_from, keys_from + n))
    trees.relabel_bst_keys(t, keys)
    return t


def gen_2_13():
    pid = "2.13"; clear(pid)
    put(pid, "01_sample", "7\n-2 7 2\n8 4 3\n9 0 0\n3 6 5\n6 0 0\n0 0 0\n-7 0 0")

    put(pid, "02_min_small_rotation", "3\n1 0 2\n2 0 3\n3 0 0")
    put(pid, "03_min_big_rotation", "3\n1 0 2\n3 3 0\n2 0 0")
    rnd = random.Random(213)
    put(pid, "04_small_rot_balance0", trees.dump_one_based(_rotation_case(1, "small0")))
    put(pid, "05_small_rot_balance_plus", trees.dump_one_based(_rotation_case(2, "small_plus")))
    put(pid, "06_big_rot", trees.dump_one_based(_rotation_case(2, "big")))
    put(pid, "07_big_rot_deeper", trees.dump_one_based(_rotation_case(3, "big"), order="dfs"))

    t = _rotation_case(2, "small0", keys_from=-10 ** 9)
    put(pid, "08_negative_keys", trees.dump_one_based(t))

    for i, h in enumerate((3, 4, 5, 6), start=9):
        put(pid, "%02d_random_avl_h%d" % (i, h),
            trees.dump_one_based(_random_rotation_case(h, rnd), order="dfs" if h % 2 else "bfs"))

    put(pid, "big_13_small_rot_1e5", trees.dump_one_based(_rotation_case(15, "small0")))
    put(pid, "big_14_big_rot_1e5", trees.dump_one_based(_rotation_case(15, "big")))
    put(pid, "big_15_chain_like", trees.dump_one_based(_rotation_case(14, "small_plus"),
                                                       order="dfs"))
    put(pid, "big_16_random_avl", trees.dump_one_based(
        _random_rotation_case(16, rnd, max_nodes=200000), order="dfs"))
