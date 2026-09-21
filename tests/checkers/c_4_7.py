
import refs


def check(inp, out, exp):
    pairs = []
    for line in inp.splitlines():
        parts = line.split()
        if len(parts) >= 2:
            pairs.append((parts[0], parts[1]))
    rows = [r for r in out.splitlines() if r.strip()]
    if len(rows) != len(pairs):
        return False, u"ожидалось %d строк ответа, получено %d" % (len(pairs), len(rows))
    for idx, ((s, t), row) in enumerate(zip(pairs, rows), 1):
        nums = row.split()
        if len(nums) != 3:
            return False, u"строка %d: ожидалось 3 числа, получено %r" % (idx, row)
        i, j, l = (int(x) for x in nums)
        best = refs.lcs_length(s, t)
        if l != best:
            return False, u"строка %d: длина %d, максимум %d" % (idx, l, best)
        if l:
            if not (0 <= i <= len(s) - l and 0 <= j <= len(t) - l):
                return False, u"строка %d: позиции вне строк" % idx
            if s[i:i + l] != t[j:j + l]:
                return False, u"строка %d: подстроки не совпадают (%r != %r)" % (
                    idx, s[i:i + l], t[j:j + l])
    return True, ""
