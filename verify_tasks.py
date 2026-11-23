"""Provera svih zadataka i kvizova. Pokretanje iz korena repoa:  python verify_tasks.py

1. svako "primer resenje" mora da ispise tacno ono sto pise u `expected`;
2. pocetni (starter) kod sam ne sme da prodje proveru;
3. kviz pitanje ciji kod ispisuje nesto mora da ima tacno jednu opciju koja odgovara
   stvarnom ispisu (ili imenu greske) i to mora da bude oznacena;
4. docs/data.js mora da bude azuran u odnosu na tasks.py i lectures.py.

Potrebne su biblioteke iz requirements.txt (zadaci koriste numpy, pandas, ...).
Izlazni kod je 0 samo ako je sve u redu.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import build_web_data
import tasks

ROOT = Path(__file__).parent


def run(code):
    """Izvrsava kod u novom Python procesu (-I = izolovano) u privremenoj fascikli; vraca (stdout, stderr)."""
    with tempfile.TemporaryDirectory() as d:  # zadaci pisu fajlove, pa u privremenu fasciklu
        r = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True,
                           cwd=d, timeout=120, env={**os.environ, "MPLBACKEND": "Agg"})
    return r.stdout, r.stderr


def norm(s):
    """Isto normalizovanje ispisa kao _norm u play.py."""
    return "\n".join(line.rstrip() for line in s.strip().splitlines())


def main():
    """Radi sve cetiri provere iz opisa na vrhu fajla; vraca 0 samo ako je sve u redu."""
    bad = []
    n_code = n_quiz = n_concept = 0

    for floor, items in tasks.CODE.items():
        for i, (_text, expected, starter, solution) in enumerate(items):
            level = 2 * i + 2
            n_code += 1
            out, err = run(solution)
            if norm(out) != norm(expected):
                bad.append(f"zadatak {floor}-{level}: resenje ispisuje {norm(out)!r}, ocekivano {expected!r} {err.strip()[-100:]}")
            if norm(run(starter)[0]) == norm(expected):
                bad.append(f"zadatak {floor}-{level}: pocetni kod sam prolazi proveru")

    for floor, items in tasks.QUIZ.items():
        for i, (code, options, answer) in enumerate(items):
            level = 2 * i + 1
            if "print(" not in code:  # konceptualno pitanje ili racun u komentaru: proveriti rucno
                n_concept += 1
                continue
            n_quiz += 1
            out, err = run(code)
            hits = [k for k, t in enumerate(options) if norm(t) == norm(out)]
            if not hits and err:
                exc = err.strip().splitlines()[-1].split(":")[0]
                hits = [k for k, t in enumerate(options) if exc in t]
            if hits != [answer]:
                bad.append(f"kviz {floor}-{level}: ispis {norm(out)!r}, opcije koje odgovaraju {hits}, oznaceno {answer}")

    # data.js
    sections = build_web_data.load_sections()
    expected_js = build_web_data.build_js(tasks, sections)
    current = (ROOT / "docs" / "data.js").read_text(encoding="utf-8")
    if current != expected_js:
        bad.append("docs/data.js nije azuran: pokreni  python build_web_data.py")

    print(f"zadaci: {n_code}, kvizovi sa ispisom: {n_quiz}, konceptualni (rucno): {n_concept}")
    for b in bad:
        print("GRESKA:", b)
    print("SVE U REDU" if not bad else f"{len(bad)} problema")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
