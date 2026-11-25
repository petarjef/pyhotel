"""Generise docs/data.js iz tasks.py i lectures.py.

Pokreni iz korena repoa kad god menjas zadatke:  python build_web_data.py
(Ne uvozi PySide6, cita samo podatke.)
"""
import ast
import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).parent
SKIP = {"ML_25_01_Uvod_1.html"}  # isto kao u hotel.py


def load_tasks():
    """Uvozi tasks.py kao modul (bez PySide6; tasks.py sadrzi samo podatke)."""
    spec = importlib.util.spec_from_file_location("tasks", BASE / "tasks.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_sections():
    """Cita SECTIONS iz lectures.py kao tekst (ast.literal_eval), jer bi uvoz lectures.py
    zahtevao PySide6.
    """
    tree = ast.parse((BASE / "lectures.py").read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "SECTIONS":
            return ast.literal_eval(node.value)
    raise SystemExit("SECTIONS nije nadjen u lectures.py")


def build_js(t, sections):
    """Vraca tekst docs/data.js (bez resenja zadataka)."""
    lessons = [title for _, items in sections[1:] for f, title in items if f not in SKIP]

    quiz = {str(k): [{"code": c, "options": o, "answer": a} for c, o, a in v]
            for k, v in t.QUIZ.items()}
    # resenja se ne ukljucuju u web verziju
    code = {str(k): [{"text": x, "expected": e, "starter": s} for x, e, s, _sol in v]
            for k, v in t.CODE.items()}
    topics = [{"title": name, "items": [{"file": f, "title": title} for f, title in items]}
              for name, items in sections]

    return "window.HOTEL_DATA = " + json.dumps(
        {"lessons": lessons, "quiz": quiz, "code": code, "topics": topics},
        ensure_ascii=False, indent=1) + ";\n"


def main():
    """Pise docs/data.js i ispisuje koliko je spratova, kvizova i zadataka."""
    t = load_tasks()
    sections = load_sections()
    out = build_js(t, sections)
    (BASE / "docs" / "data.js").write_text(out, encoding="utf-8")
    n_lessons = sum(len(items) for _, items in sections[1:]) - 1
    print(f"docs/data.js: {n_lessons} spratova, {sum(map(len, t.QUIZ.values()))} kviz pitanja, "
          f"{sum(map(len, t.CODE.values()))} zadataka za kod")


if __name__ == "__main__":
    main()

