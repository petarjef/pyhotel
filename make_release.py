import shutil
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "release" / "app"

EXCLUDE_DIRS = {".venv", "__pycache__", ".git", ".vscode", "lessons",
                "release", "installer_output"}
EXCLUDE_FILES = {"settings.json", "progress.json", "chat_history.json",
                 "api_key.txt", "make_zip.py", "make_release.py",
                 "convert_lessons.py", "start.bat"}
EXCLUDE_SUFFIX = {".pyc", ".iss", ".zip"}

# knjiga i prezentacije se namerno pakuju u instaler (uz dozvolu profesora);
# lessons/ (izvorni .ipynb) se ne pakuje
for needed in ("book", "lessons_html"):
    d = ROOT / needed
    if not d.is_dir() or not any(d.iterdir()):
        print(f"UPOZORENJE: {needed}/ je prazan ili ne postoji - instaler ce biti bez toga!")

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