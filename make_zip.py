import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT.parent / "pyhotel_release.zip"

# Ovo se NE ubacuje u zip
EXCLUDE_DIRS = {".venv", "__pycache__", ".git", ".vscode", "lessons"}
EXCLUDE_FILES = {
    "settings.json", "progress.json", "chat_history.json",
    "api_key.txt", "make_zip.py", "convert_lessons.py",
}

count = 0
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if rel.name in EXCLUDE_FILES or rel.suffix == ".pyc":
            continue
        zf.write(p, Path("pyhotel") / rel)
        count += 1

print(f"Napravljeno: {OUT}  ({count} fajlova)")