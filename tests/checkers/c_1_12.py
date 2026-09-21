
import refs


def _parse(inp):
    it = [int(x) for x in inp.split()]
    n = it[0]
    return n, it[1:1 + n]


def _reference_subset(n, a):
    total = sum(a)
    if total % 2:
        return None
    target = total // 2
    res = []
    for i in range(n - 1, -1, -1):
        if a[i] <= target:
            target -= a[i]
            res.append(i + 1)
    return res if target == 0 else None


def check(inp, out, exp):
    n, a = _parse(inp)
    total = sum(a)
    ref = _reference_subset(n, a)
    toks = out.split()
    if toks and toks[0] == "-1":
        if ref is not None:
            return False, u"выведено -1, хотя разбиение существует"
        return True, ""
    if ref is None:
        return False, u"выведено разбиение, хотя сумма %d нечётна" % total
    if not toks:
        return False, u"пустой вывод"
    k = int(toks[0])
    idx = [int(x) for x in toks[1:]]
    if len(idx) != k:
        return False, u"заявлено k=%d, а номеров %d" % (k, len(idx))
    if len(set(idx)) != k:
        return False, u"номера повторяются"
    if any(i < 1 or i > n for i in idx):
        return False, u"номер вне диапазона 1..%d" % n
    got = sum(a[i - 1] for i in idx)
    if got * 2 != total:
        return False, u"сумма части = %d, а нужно %d" % (got, total // 2)
    if k == 0 or k == n:
        return False, u"одна из частей пуста"
    return True, ""
