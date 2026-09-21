
import random


class Shape(object):

    def __init__(self):
        self.left = []
        self.right = []
        self.key = []

    def add(self, key):
        self.left.append(-1)
        self.right.append(-1)
        self.key.append(key)
        return len(self.key) - 1

    def size(self):
        return len(self.key)


def bst_from_keys(keys):
    t = Shape()
    if not keys:
        return t
    t.add(keys[0])
    for k in keys[1:]:
        v = 0
        while True:
            if k < t.key[v]:
                if t.left[v] == -1:
                    t.left[v] = t.add(k)
                    break
                v = t.left[v]
            elif k > t.key[v]:
                if t.right[v] == -1:
                    t.right[v] = t.add(k)
                    break
                v = t.right[v]
            else:
                break
    return t


def chain(n, side, start=1, step=1):
    t = Shape()
    keys = [start + i * step for i in range(n)]
    if side == "left":
        keys = keys[::-1]
    prev = t.add(keys[0])
    for k in keys[1:]:
        cur = t.add(k)
        if side == "left":
            t.left[prev] = cur
        else:
            t.right[prev] = cur
        prev = cur
    return t


def zigzag(n, start=0):
    t = Shape()
    lo, hi = start, start + n - 1
    mid = (lo + hi) // 2
    root = t.add(mid)
    cur, low, high, go_left = root, lo, hi, True
    used = 1
    while used < n:
        if go_left:
            k = low
            low += 1
        else:
            k = high
            high -= 1
        node = t.add(k)
        if k < t.key[cur]:
            t.left[cur] = node
        else:
            t.right[cur] = node
        cur = node
        used += 1
        go_left = not go_left
    return t


def perfect(h, first=0):
    t = Shape()
    if h == 0:
        return t, first

    def build(height, lo):
        if height == 0:
            return -1, lo
        cnt = (1 << (height - 1)) - 1
        node = t.add(0)
        l, nxt = build(height - 1, lo)
        t.key[node] = nxt
        nxt += 1
        r, nxt = build(height - 1, nxt)
        t.left[node] = l
        t.right[node] = r
        return node, nxt

    root, nxt = build(h, first)
    assert root == 0 or root != -1
    if root != 0:
        _reindex_root_first(t, root)
    return t, nxt


def _reindex_root_first(t, root):
    order = list(range(t.size()))
    order.remove(root)
    order = [root] + order
    pos = {old: new for new, old in enumerate(order)}
    key = [t.key[o] for o in order]
    left = [pos[t.left[o]] if t.left[o] != -1 else -1 for o in order]
    right = [pos[t.right[o]] if t.right[o] != -1 else -1 for o in order]
    t.key, t.left, t.right = key, left, right


def merge(root_key, l_tree, r_tree):
    t = Shape()
    t.add(root_key)
    for sub, is_left in ((l_tree, True), (r_tree, False)):
        if sub.size() == 0:
            continue
        base = t.size()
        for i in range(sub.size()):
            t.add(sub.key[i])
        for i in range(sub.size()):
            t.left[base + i] = base + sub.left[i] if sub.left[i] != -1 else -1
            t.right[base + i] = base + sub.right[i] if sub.right[i] != -1 else -1
        if is_left:
            t.left[0] = base
        else:
            t.right[0] = base
    return t


def inorder(t):
    if t.size() == 0:
        return []
    res, stack, v = [], [], 0
    while stack or v != -1:
        while v != -1:
            stack.append(v)
            v = t.left[v]
        v = stack.pop()
        res.append(v)
        v = t.right[v]
    return res


def relabel_bst_keys(t, keys):
    for pos, v in enumerate(inorder(t)):
        t.key[v] = keys[pos]


def dump_zero_based(t, rnd=None):
    n = t.size()
    if n == 0:
        return "0"
    order = list(range(n))
    if rnd is not None:
        rest = order[1:]
        rnd.shuffle(rest)
        order = [0] + rest
    pos = {old: new for new, old in enumerate(order)}
    lines = ["%d" % n]
    for new in range(n):
        old = order[new]
        l = pos[t.left[old]] if t.left[old] != -1 else -1
        r = pos[t.right[old]] if t.right[old] != -1 else -1
        lines.append("%d %d %d" % (t.key[old], l, r))
    return "\n".join(lines)


def dump_one_based(t, order="bfs"):
    n = t.size()
    if n == 0:
        return "0"
    seq = []
    if order == "bfs":
        from collections import deque
        q = deque([0])
        while q:
            v = q.popleft()
            seq.append(v)
            if t.left[v] != -1:
                q.append(t.left[v])
            if t.right[v] != -1:
                q.append(t.right[v])
    else:
        stack = [0]
        while stack:
            v = stack.pop()
            seq.append(v)
            if t.right[v] != -1:
                stack.append(t.right[v])
            if t.left[v] != -1:
                stack.append(t.left[v])
    pos = {old: i + 1 for i, old in enumerate(seq)}
    lines = ["%d" % n]
    for old in seq:
        l = pos[t.left[old]] if t.left[old] != -1 else 0
        r = pos[t.right[old]] if t.right[old] != -1 else 0
        lines.append("%d %d %d" % (t.key[old], l, r))
    return "\n".join(lines)


def random_bst(n, rnd, lo=-10 ** 9, hi=10 ** 9):
    keys = rnd.sample(range(lo, hi), n) if hi - lo > 4 * n else list(range(lo, lo + n))
    return bst_from_keys(keys)


def random_avl(h, rnd, keys_from=0):
    def build(height):
        if height == 0:
            return Shape()
        if height == 1:
            t = Shape()
            t.add(0)
            return t
        choice = rnd.choice([(height - 1, height - 1), (height - 1, height - 2),
                             (height - 2, height - 1)])
        return merge(0, build(choice[0]), build(choice[1]))

    t = build(h)
    relabel_bst_keys(t, list(range(keys_from, keys_from + t.size())))
    return t
