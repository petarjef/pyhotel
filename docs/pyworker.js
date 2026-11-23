// Python (Pyodide) radi u Web Worker-u, pa STOP moze da ga ugasi a stranica ostaje živa.
const PYODIDE = "https://cdn.jsdelivr.net/pyodide/v0.27.2/full/";
try {
  importScripts(PYODIDE + "pyodide.js");
} catch (e) {
  postMessage({ t: "fatal", s: "ne mogu da dohvatim Python sa interneta. Proveri vezu i probaj ponovo." });
}

let py = null;
let stdinLines = [];
const SETUP = `
import os, sys, warnings

class _Out:
    # bez baferovanja: print(end="") i prompt od input() izlaze odmah
    encoding = "utf-8"
    errors = "strict"
    def write(self, s):
        _emit(s)
        return len(s)
    def flush(self):
        pass
    def isatty(self):
        return False

sys.stdout = sys.stderr = _Out()
os.environ["MPLBACKEND"] = "AGG"
warnings.filterwarnings("ignore", message=".*non-interactive.*")

import ast, traceback
_ns = globals()

def _run(src):
    # kao Jupyter: poslednji izraz se ispisuje; greske bez internih frejmova
    try:
        tree = ast.parse(src, "<code>", "exec")
        last = None
        if tree.body and isinstance(tree.body[-1], ast.Expr):
            last = ast.Expression(tree.body.pop().value)
        exec(compile(tree, "<code>", "exec"), _ns)
        if last is not None:
            v = eval(compile(last, "<code>", "eval"), _ns)
            if v is not None:
                print(repr(v))
    except SystemExit:
        pass
    except BaseException as e:
        tb = e.__traceback__.tb_next if e.__traceback__ else None
        if isinstance(e, SyntaxError):
            tb = None
        sys.stderr.write("".join(traceback.format_exception(type(e), e, tb)))

def __grab_figs():
    import sys, io, base64
    if "matplotlib.pyplot" not in sys.modules:
        return []
    plt = sys.modules["matplotlib.pyplot"]
    out = []
    for n in plt.get_fignums():
        buf = io.BytesIO()
        plt.figure(n).savefig(buf, format="png", dpi=80, bbox_inches="tight")
        out.append(base64.b64encode(buf.getvalue()).decode())
    plt.close("all")
    return out
`;

async function init() {
  postMessage({ t: "status", s: "Ucitavam Python (prvi put traje par sekundi)..." });
  py = await loadPyodide({ indexURL: PYODIDE });
  py.globals.set("_emit", (s) => postMessage({ t: "out", s }));
  py.setStdin({
    stdin: () => {
      if (!stdinLines.length) return undefined;       // EOFError u Pythonu
      const line = stdinLines.shift();
      postMessage({ t: "out", s: line + "\n" });       // kao u terminalu, ispisi sta je uneto
      return line;
    },
  });
  py.runPython(SETUP);
  postMessage({ t: "ready" });
}
const ready = (typeof loadPyodide === "function" ? init() : Promise.reject("Pyodide nije ucitan")).catch((e) => postMessage({ t: "fatal", s: String(e) }));

function cleanTrace(msg) {
  // izbaci interne Pyodide frejmove, ostavi samo korisnikov kod
  return msg.replace(/ {2}File "\/lib\/python[^"]*_pyodide[^"]*"[^\n]*\n(?: {4}[^\n]*\n)*/g, "");
}

onmessage = async (e) => {
  const m = e.data;
  if (m.t !== "run") return;
  await ready;
  if (!py) {
    postMessage({ t: "fatal", s: "Python se nije ucitao. Proveri internet vezu, osvezi stranicu i probaj ponovo." });
    return;
  }
  stdinLines = m.stdin || [];
  try {
    await py.loadPackagesFromImports(m.code, {
      messageCallback: (s) => postMessage({ t: "status", s }),
      errorCallback: (s) => postMessage({ t: "status", s }),
    });
    postMessage({ t: "status", s: "Radi..." });
    py.globals.get("_run")(m.code);
  } catch (err) {
    postMessage({ t: "out", s: cleanTrace(String(err.message || err)) + "\n" });
  }
  try {
    const figs = py.globals.get("__grab_figs")().toJs();
    if (figs.length) postMessage({ t: "figs", figs });
  } catch (_) {}
  postMessage({ t: "done" });
};
