"""Priprema fasciklu release/app za Inno Setup (installer.iss).

Pokretanje iz korena repoa:  python make_release.py
Kopira samo ono sto igra treba za rad (kod, assets/, requirements.txt).
Knjiga se ne pakuje (cita se online), web verzija (docs/) i dokumentacija takodje ne.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "release" / "app"

EXCLUDE_DIRS = {".venv", "__pycache__", ".git", ".vscode", ".github",
                "release", "installer_output", "docs", "documentation"}
EXCLUDE_FILES = {"settings.json", "progress.json", "chat_history.json",
                 "make_release.py", "build_web_data.py", "verify_tasks.py",
                 "README.md", ".gitignore"}
EXCLUDE_SUFFIX = {".pyc", ".iss", ".zip"}

if not (ROOT / "requirements.txt").is_file():
    raise SystemExit("GRESKA: requirements.txt ne postoji - instaler bi pao pri pip install.")

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

count = 0
for p in sorted(ROOT.rglob("*")):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        continue
    if rel.name in EXCLUDE_FILES or rel.suffix in EXCLUDE_SUFFIX:
        continue
    dest = OUT / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dest)
    count += 1

print(f"Kopirano {count} fajlova u {OUT}")


