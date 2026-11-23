"""Cuvanje progresa: koji su nivoi resena.

Resen nivo se pamti kao string "sprat-nivo" (npr. "3-5") u datoteci progress.json.
"""

import json
from pathlib import Path

FILE = Path(__file__).parent / "progress.json"
LEVELS = 12


def _load():
    """Cita progress.json i vraca skup resenih nivoa; ako fajla nema ili je ostecen, vraca prazan skup."""
    try:
        return set(json.loads(FILE.read_text(encoding="utf-8"))["solved"])
    except Exception:
        return set()


# skup se ucitava jednom, pri uvozu modula
_solved = _load()


def mark(floor, level):
    """Oznaci nivo kao resen i odmah upisi ceo skup u progress.json."""
    _solved.add(f"{floor}-{level}")
    try:
        FILE.write_text(json.dumps({"solved": sorted(_solved)}), encoding="utf-8")
    except OSError:
        pass  # nema prava pisanja: progres ostaje u memoriji do zatvaranja igre


def is_solved(floor, level):
    """True ako je nivo vec resen."""
    return f"{floor}-{level}" in _solved


def done_count(floor):
    """Koliko UZASTOPNIH nivoa je resen od prvog. Staje na prvom nereseno, pa se nivoi
    otkljucavaju redom i znacka na tabli sprata prikazuje n/12.
    """
    n = 0
    while n < LEVELS and is_solved(floor, n + 1):
        n += 1
    return n