
import gzip
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(HERE, "data")
sys.path.insert(0, HERE)

GZIP_OVER = 64 * 1024


def _write(path, text):
    if len(text) > GZIP_OVER:
        for stale in (path,):
            if os.path.exists(stale):
                os.remove(stale)
        with gzip.open(path + ".gz", "wb") as f:
            f.write(text.encode())
        return path + ".gz"
    if os.path.exists(path + ".gz"):
        os.remove(path + ".gz")
    with open(path, "w") as f:
        f.write(text)
    return path


def put(pid, name, inp, out=None, ref=None, expect=None):
    d = os.path.join(DATA, pid)
    if not os.path.isdir(d):
        os.makedirs(d)
    if not inp.endswith("\n"):
        inp += "\n"
    if out is None and ref is not None:
        out = ref(inp)
    if expect is not None:
        got = " ".join((out or "").split())
        want = " ".join(expect.split())
        assert got == want, "%s/%s: эталон даёт %r, а в условии %r" % (pid, name, got, want)
    _write(os.path.join(d, name + ".in"), inp)
    if out is not None:
        if not out.endswith("\n"):
            out += "\n"
        _write(os.path.join(d, name + ".out"), out)
    return name


def clear(pid):
    d = os.path.join(DATA, pid)
    if os.path.isdir(d):
        for f in os.listdir(d):
            os.remove(os.path.join(d, f))
