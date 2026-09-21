
import refs


def _read_out(out):
    it = out.split()
    if not it:
        raise ValueError(u"пустой вывод")
    n = int(it[0])
    key = [0] * (n + 1); left = [0] * (n + 1); right = [0] * (n + 1)
    if len(it) != 1 + 3 * n:
        raise ValueError(u"ожидалось %d чисел, получено %d" % (1 + 3 * n, len(it)))
    k = 1
    for i in range(1, n + 1):
        key[i] = int(it[k]); left[i] = int(it[k + 1]); right[i] = int(it[k + 2])
        k += 3
    return n, key, left, right


def _shape(key, left, right, v):
    stack = [(v, 0)]
    done = {}
    while stack:
        x, st = stack.pop()
        if x == 0:
            continue
        if st == 0:
            stack.append((x, 1))
            stack.append((left[x], 0))
            stack.append((right[x], 0))
        else:
            done[x] = (key[x], done.get(left[x]), done.get(right[x]))
    return done.get(v)


def check(inp, out, exp):
    n_in, key_in, left_in, right_in = refs._read_tree_1(inp)
    root_e, key_e, left_e, right_e, n_e = refs.ref_2_13_tree(inp)
    try:
        n, key, left, right = _read_out(out)
    except ValueError as e:
        return False, str(e)
    if n != n_e:
        return False, u"число вершин %d, ожидалось %d" % (n, n_e)
    for i in range(1, n + 1):
        for c in (left[i], right[i]):
            if c != 0 and not (i < c <= n):
                return False, u"вершина %d: номер ребёнка %d нарушает формат (i < child <= N)" % (i, c)

    seen = set()
    stack = [1]
    while stack:
        v = stack.pop()
        if v in seen:
            return False, u"вершина %d достижима дважды - это не дерево" % v
        seen.add(v)
        if left[v]:
            stack.append(left[v])
        if right[v]:
            stack.append(right[v])
    if len(seen) != n:
        return False, u"из корня достижимы не все вершины (%d из %d)" % (len(seen), n)
    if sorted(key[1:]) != sorted(key_e[1:]):
        return False, u"набор ключей изменился"
    if _shape(key, left, right, 1) != _shape(key_e, left_e, right_e, root_e):
        return False, u"структура дерева не совпадает с результатом левого поворота"
    return True, ""
