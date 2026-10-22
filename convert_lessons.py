"""Pretvara lessons/*.ipynb u lessons_html/*.html.

- Notebook u kom ima kod-celija koja nikad nije pokrenuta se pre konverzije
  izvrsi ceo (Run All), pa HTML ima sve izlaze. Vec izvrseni se ne diraju.
- input() se pri izvrsavanju zamenjuje lazom: vraca odgovor iz INPUTS
  (trazi se podniz u tekstu poruke), a ako nema poklapanja DEFAULT_INPUT.
- Greske u celijama (npr. namerne greske iz predavanja) ostaju vidljive u HTML-u.
- Slike iz markdown-a (![](slika.png)) se ugradjuju u HTML; slike moraju da
  budu u lessons/ (ili podfolderu) tacno kako ih notebook navodi.
"""
import re
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

BASE = Path(__file__).parent
SRC = BASE / "lessons"
OUT = BASE / "lessons_html"
OUT.mkdir(exist_ok=True)

DEFAULT_INPUT = "5"
INPUTS = [  # (podniz poruke malim slovima, sta "korisnik unese")
    ("jedan prirodan", "7"),
    ("poluprečnik", "3"),
    ("površinu kruga", "P"),
    ("trenutnu temperaturu", "30"),
    ("traženu temperaturu", "20"),
    ("realni broj", "-3"),
    ("string", "python"),
]
TIMEOUT = 180  # sekundi po celiji

SETUP = f'''_ANSWERS = {INPUTS!r}
def _fake_input(prompt=""):
    answer = {DEFAULT_INPUT!r}
    for key, value in _ANSWERS:
        if key in str(prompt).lower():
            answer = value
            break
    print(str(prompt) + answer)
    return answer
get_ipython().kernel.raw_input = _fake_input'''

IMG = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")


def never_run(nb):
    return [c for c in nb.cells
            if c.cell_type == "code" and c.source.strip() and c.get("execution_count") is None]


def missing_images(nb):
    out = []
    for c in nb.cells:
        if c.cell_type == "markdown":
            for url in IMG.findall(c.source):
                if not url.startswith(("http", "data:", "attachment:")) and not (SRC / url).exists():
                    out.append(url)
    return out


exporter = HTMLExporter(embed_images=True)
for path in sorted(SRC.glob("*.ipynb")):
    nb = nbformat.read(path, as_version=4)
    todo = never_run(nb)
    if todo:
        nb.cells.insert(0, nbformat.v4.new_code_cell(SETUP))
        ep = ExecutePreprocessor(timeout=TIMEOUT, allow_errors=True, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": str(SRC)}})
        nb.cells.pop(0)  # sakrij pomocnu celiju
        errors = [(c, o) for c in nb.cells if c.cell_type == "code"
                  for o in c.get("outputs", []) if o.get("output_type") == "error"]
        status = f"IZVRSEN ({len(todo)} celija nije bilo pokrenuto, gresaka u celijama: {len(errors)})"
    else:
        errors, status = [], "OK (vec ima izlaze)"
    print(f"{path.name}: {status}")
    for c, e in errors:
        print(f"    ! {e['ename']}: {c.source.strip().splitlines()[0][:70]}")
    missing = missing_images(nb)
    for url in missing:
        print(f"    ! SLIKA NEDOSTAJE: lessons/{url}")
        for c in nb.cells:  # da konverzija ne pukne na nepostojecoj slici
            if c.cell_type == "markdown":
                c.source = re.sub(r"!\[([^\]]*)\]\(" + re.escape(url) + r"[^)]*\)",
                                  r"*[slika nedostaje: \1]*", c.source)
    body, _ = exporter.from_notebook_node(nb, resources={"metadata": {"path": str(SRC)}})
    (OUT / (path.stem + ".html")).write_text(body, encoding="utf-8")