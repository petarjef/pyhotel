import json
from pathlib import Path

FILE = Path(__file__).parent / "progress.json"
LEVELS = 12


def _load():
    try:
        return set(json.loads(FILE.read_text(encoding="utf-8"))["solved"])
    except Exception:
        return set()


_solved = _load()


def mark(floor, level):
    _solved.add(f"{floor}-{level}")
    try:
        FILE.write_text(json.dumps({"solved": sorted(_solved)}), encoding="utf-8")
    except OSError:
        pass  # nema prava pisanja: progres ostaje u memoriji do zatvaranja igre


def is_solved(floor, level):
    return f"{floor}-{level}" in _solved


def done_count(floor):
    n = 0
    while n < LEVELS and is_solved(floor, n + 1):
        n += 1
    return n