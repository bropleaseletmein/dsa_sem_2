
import re
import refs

TOKEN = re.compile(r'^([A-Za-z]+)(?:\*([0-9]+))?$')


def check(inp, out, exp):
    s = inp.split("\n")[0].strip()
    ans = out.strip()
    if not ans:
        return False, u"пустой вывод"
    if "\n" in ans:
        return False, u"ожидалась одна строка"
    built = []
    for part in ans.split("+"):
        m = TOKEN.match(part)
        if not m:
            return False, u"кусок %r не соответствует формату строка[*число]" % part
        word, mult = m.group(1), m.group(2)
        if mult is not None:
            k = int(mult)
            if k < 1:
                return False, u"множитель %d в %r" % (k, part)
            built.append(word * k)
        else:
            built.append(word)
    if "".join(built) != s:
        return False, u"представление раскрывается не в исходную строку"
    best = refs.decomposition_cost(s)
    if len(ans) != best:
        return False, u"длина записи %d, минимальная %d" % (len(ans), best)
    return True, ""
