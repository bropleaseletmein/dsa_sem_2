
from fractions import Fraction
import refs


def check(inp, out, exp):
    toks = out.split()
    if len(toks) != 1:
        return False, u"ожидалось одно число, получено %d токенов" % len(toks)
    try:
        got = Fraction(toks[0])
    except (ValueError, ZeroDivisionError):
        return False, u"не число: %r" % toks[0]
    want = refs.ref_1_1_value(inp)
    if abs(got - want) > Fraction(1, 1000):
        return False, u"ожидалось %.4f, получено %s" % (float(want), toks[0])
    if "." not in toks[0] or len(toks[0].split(".")[1]) < 4:
        return False, u"нужно минимум 4 знака после запятой, получено %r" % toks[0]
    return True, ""
