from pathlib import Path
from nbconvert import HTMLExporter

BASE = Path(__file__).parent
SRC = BASE / "lessons"
OUT = BASE / "lessons_html"
OUT.mkdir(exist_ok=True)

exporter = HTMLExporter(embed_images=True)
for nb in sorted(SRC.glob("*.ipynb")):
    body, _ = exporter.from_filename(str(nb))
    (OUT / (nb.stem + ".html")).write_text(body, encoding="utf-8")
    print("OK", nb.name)