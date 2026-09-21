

import argparse
import importlib
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from lib.harness import run_solution, compare_tokens
from problems import PROBLEMS, all_ids, sort_key

GREEN = "\033[32m"; RED = "\033[31m"; YELLOW = "\033[33m"; DIM = "\033[2m"; OFF = "\033[0m"


def colored(text, color, use):
    return color + text + OFF if use else text


def data_dir(pid):
    return os.path.join(HERE, "data", pid)


def _materialize(path, work):
    if os.path.exists(path):
        return path
    if os.path.exists(path + ".gz"):
        import gzip
        dst = os.path.join(work, os.path.basename(path))
        with gzip.open(path + ".gz", "rb") as src, open(dst, "wb") as f:
            shutil.copyfileobj(src, f)
        return dst
    return None


def _read(path):
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    if os.path.exists(path + ".gz"):
        import gzip
        with gzip.open(path + ".gz", "rt") as f:
            return f.read()
    return None


def list_tests(pid, quick):
    d = data_dir(pid)
    if not os.path.isdir(d):
        return []
    names = set()
    for f in os.listdir(d):
        if f.endswith(".in"):
            names.add(f[:-3])
        elif f.endswith(".in.gz"):
            names.add(f[:-6])
    names = sorted(names)
    if quick:
        names = [n for n in names if not n.startswith("big")]
    return [(n, os.path.join(d, n + ".in"), os.path.join(d, n + ".out")) for n in names]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*", help="номера задач, например 1.1 2.13")
    ap.add_argument("--lab", help="lab1|lab2|lab3|lab4")
    ap.add_argument("--quick", action="store_true", help="пропустить тяжёлые тесты big_*")
    ap.add_argument("--only-big", action="store_true", help="только тяжёлые тесты")
    ap.add_argument("-v", "--verbose", action="store_true", help="печатать каждый тест")
    ap.add_argument("--timeout", type=float, default=0.0,
                    help="жёсткий таймаут, сек (по умолчанию 10x лимита задачи, минимум 30)")
    args = ap.parse_args()

    use_color = sys.stdout.isatty()
    ids = args.ids or all_ids()
    ids = [i for i in ids if i in PROBLEMS]
    if args.lab:
        ids = [i for i in ids if PROBLEMS[i]["lab"] == args.lab]
    ids.sort(key=sort_key)
    if not ids:
        print("нет задач по фильтру")
        return 1

    work = tempfile.mkdtemp(prefix="dsa_tests_")
    total_fail = 0
    total_run = 0
    try:
        for pid in ids:
            info = PROBLEMS[pid]
            tests = list_tests(pid, args.quick)
            if args.only_big:
                tests = [t for t in tests if t[0].startswith("big")]
            checker = None
            if info.get("checker"):
                checker = importlib.import_module("checkers." + info["checker"])
            for sol_rel in info["solutions"]:
                sol = os.path.join(ROOT, sol_rel)
                head = "%-5s %-38s %s" % (pid, info["title"][:38], sol_rel)
                if not os.path.exists(sol):
                    print(colored("НЕТ ФАЙЛА " + head, RED, use_color))
                    total_fail += 1
                    continue
                if not tests:
                    print(colored("НЕТ ТЕСТОВ " + head, YELLOW, use_color))
                    continue
                fails = []
                worst = 0.0
                worst_mem = 0.0
                for name, fin, fout in tests:
                    total_run += 1
                    hard = args.timeout or max(30.0, info["tl"] * 10)
                    real_in = _materialize(fin, work)
                    res = run_solution(sol, real_in, work, hard)
                    worst = max(worst, res.seconds)
                    worst_mem = max(worst_mem, res.mem_mb)
                    if res.timed_out:
                        fails.append((name, "ЗАВИС (> %.0f c)" % hard))
                        continue
                    if res.code != 0:
                        err = res.stderr.strip().splitlines()
                        fails.append((name, "ОШИБКА: " + (err[-1] if err else "код %d" % res.code)))
                        continue
                    if checker:
                        ok, msg = checker.check(_read(fin), res.stdout, _read(fout))
                    else:
                        expected = _read(fout)
                        if expected is None:
                            ok, msg = False, "нет файла с ответом"
                        else:
                            ok, msg = compare_tokens(res.stdout, expected)
                    if not ok:
                        fails.append((name, msg))
                    if args.verbose:
                        mark = colored("ok  ", GREEN, use_color) if ok else colored("FAIL", RED, use_color)
                        print("   %s %-28s %6.2f c  %6.1f Мб %s" % (
                            mark, name, res.seconds, res.mem_mb, "" if ok else msg))
                if fails:
                    total_fail += len(fails)
                    print(colored("FAIL  " + head, RED, use_color) +
                          "  (%d из %d)" % (len(fails), len(tests)))
                    for name, msg in fails[:6]:
                        print("        %-28s %s" % (name, msg))
                    if len(fails) > 6:
                        print("        ... ещё %d" % (len(fails) - 6))
                else:
                    print(colored("OK    " + head, GREEN, use_color) +
                          "  %d тестов, макс %.2f c (лимит %.0f c), %.0f Мб" % (
                              len(tests), worst, info["tl"], worst_mem))
    finally:
        shutil.rmtree(work, ignore_errors=True)

    print("")
    print("Всего запусков: %d, провалов: %d" % (total_run, total_fail))
    return 1 if total_fail else 0


if __name__ == "__main__":
    sys.exit(main())
