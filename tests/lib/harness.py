import os
import resource
import subprocess
import sys
import threading
import time

IS_MAC = sys.platform == "darwin"


class RunResult(object):
    def __init__(self, stdout, stderr, code, seconds, mem_mb, timed_out):
        self.stdout = stdout
        self.stderr = stderr
        self.code = code
        self.seconds = seconds
        self.mem_mb = mem_mb
        self.timed_out = timed_out


def run_solution(solution_path, input_path, work_dir, hard_timeout):
    out_path = os.path.join(work_dir, "stdout.txt")
    err_path = os.path.join(work_dir, "stderr.txt")
    fin = open(input_path, "rb")
    fout = open(out_path, "wb")
    ferr = open(err_path, "wb")
    started = time.time()
    proc = subprocess.Popen(
        [sys.executable, os.path.abspath(solution_path)],
        stdin=fin, stdout=fout, stderr=ferr,
        cwd=os.path.dirname(os.path.abspath(solution_path)) or ".",
    )
    killed = {"flag": False}

    def _kill():
        killed["flag"] = True
        try:
            proc.kill()
        except OSError:
            pass

    timer = threading.Timer(hard_timeout, _kill)
    timer.start()
    try:
        pid, status, usage = os.wait4(proc.pid, 0)
    finally:
        timer.cancel()
        elapsed = time.time() - started
        fin.close()
        fout.close()
        ferr.close()
    proc.returncode = os.WEXITSTATUS(status) if os.WIFEXITED(status) else -os.WTERMSIG(status)
    raw = usage.ru_maxrss
    mem_mb = raw / (1024.0 * 1024.0) if IS_MAC else raw / 1024.0
    with open(out_path, "rb") as f:
        stdout = f.read().decode("utf-8", "replace")
    with open(err_path, "rb") as f:
        stderr = f.read().decode("utf-8", "replace")
    return RunResult(stdout, stderr, proc.returncode, elapsed, mem_mb, killed["flag"])


def tokens(text):
    return text.split()


def compare_tokens(actual, expected):
    a = tokens(actual)
    b = tokens(expected)
    if a == b:
        return True, ""
    if len(a) != len(b):
        return False, "ожидалось %d токенов, получено %d (ожид: %s | получ: %s)" % (
            len(b), len(a), _preview(b), _preview(a))
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return False, "токен #%d: ожидалось %r, получено %r" % (i + 1, y, x)
    return False, "различие"


def _preview(seq, limit=12):
    head = " ".join(seq[:limit])
    return head + (" ..." if len(seq) > limit else "") if seq else "<пусто>"


def set_soft_limits():
    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, resource.RLIM_INFINITY))
