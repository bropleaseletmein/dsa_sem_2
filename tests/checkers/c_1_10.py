
import refs


def _parse(inp):
    it = [int(x) for x in inp.split()]
    n, s = it[0], it[1]
    apples = [(it[2 + 2 * i], it[3 + 2 * i]) for i in range(n)]
    return n, s, apples


def check(inp, out, exp):
    n, s, apples = _parse(inp)
    order = refs.ref_1_10_feasible(n, apples)
    feasible = refs.ref_1_10_simulate(order, s, apples)
    toks = out.split()
    if toks == ["-1"]:
        if feasible:
            return False, (u"выведено -1, хотя порядок существует, например %s"
                           % " ".join(str(i + 1) for i in order))
        return True, ""
    if not feasible:
        return False, u"выведен порядок, хотя съесть все яблоки нельзя (ответ -1)"
    if len(toks) != n:
        return False, u"ожидалось %d номеров, получено %d" % (n, len(toks))
    try:
        got = [int(x) - 1 for x in toks]
    except ValueError:
        return False, u"не числа: %r" % toks[:5]
    if sorted(got) != list(range(n)):
        return False, u"это не перестановка номеров 1..%d" % n
    if not refs.ref_1_10_simulate(got, s, apples):
        return False, u"при таком порядке рост становится <= 0"
    return True, ""
