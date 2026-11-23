# Python Hotel – technical documentation (English)

> Purpose: so that both authors can explain **every** part of the code at the presentation.
> Bugs and risks are listed separately in `AUDIT.en.md`.
> Srpska verzija: `DOKUMENTACIJA.sr.md`.

---

## 1. What the project is

**Python Hotel** is an educational game for learning Python. The player climbs a pixel-art hotel: **each floor is one lesson** of the course *Business Decision-Making and Machine Learning* (book by Azdejković, Radojičić, Stamenković). There are 26 floors, each with 12 levels:

| Level | Type | What the player does |
|---|---|---|
| 1, 3, 5, 7, 9, 11 | **Quiz** | Picks one of 4 answers (e.g. "what does this code print?") |
| 2, 4, 6, 8, 10, 12 | **Code** | Writes Python code whose **output** must match the requested output |

Total: 26 × 6 = **156 quiz questions** and 26 × 6 = **156 coding tasks**.

Besides the game there are:
- **Code Lab** – a free Python editor (the door in the hotel lobby).
- **Lectures** – the book chapters, opened from the internet.
- **Help AI (Monty Python)** – a chat with an AI tutor (Google Gemini, the user's own free API key).

There are **two versions** of the same game:
1. **Desktop** (Python + PySide6/Qt) – installed on Windows with an installer.
2. **Web** (HTML + JavaScript + Pyodide) – runs in the browser, hosted on GitHub Pages from the `docs/` folder.

---

## 2. Technologies and why they were chosen

| Technology | Where | Why |
|---|---|---|
| **Python 3.12+** | desktop | The language we teach; all logic is written in it |
| **PySide6 (Qt 6)** | desktop UI | Official Qt for Python: windows, widgets, drawing (`QPainter`), threads (`QThread`), web view (`QWebEngineView`) |
| **jupyter_client + ipykernel** | desktop lab | A real Python kernel as in a Jupyter notebook: keeps variables between runs, supports `input()`, interrupt and restart |
| **google-genai** | desktop AI | Official Gemini API library (streamed answers) |
| **Plain JavaScript** | web | Simple, no build step, works on GitHub Pages |
| **Pyodide 0.27.2** | web lab | CPython compiled to WebAssembly – real Python in the browser, no server |
| **Web Worker** | web lab | Pyodide runs in its own thread, so long code does not freeze the page and **STOP** can kill it |
| **Canvas 2D** | web | Same pixel-art drawing as `QPainter` on desktop |
| **localStorage** | web | Stores progress, API key and chat history in the browser |
| **Inno Setup** | installer | Builds `PythonHotel_Setup.exe` for Windows |
| **Press Start 2P font** | both | Retro pixel look |

---

## 3. Repository layout

```
pyhotel/
├── main.py             ← desktop entry point (window + 3 tabs)
├── play.py             ← the "game": hotel → levels → quiz / lab; answer checking
├── hotel.py            ← hotel drawing (QPainter), floor clicks
├── lab.py              ← Code Lab: editor + Jupyter kernel
├── tasks.py            ← ALL data: 156 quizzes + 156 tasks (+ solutions)
├── progress.py         ← saves solved levels in progress.json
├── ai.py               ← chat with the Gemini tutor + ACCOUNT page
├── lectures.py         ← lesson list (SECTIONS) + book reader
├── build_web_data.py   ← generates docs/data.js from tasks.py + lectures.py
├── make_release.py     ← prepares release/app for the installer
├── requirements.txt    ← libraries (pinned versions)
├── verify_tasks.py     ← automatic check of all tasks, quizzes and data.js
├── installer.iss       ← Inno Setup script (Windows installer)
├── assets/             ← font, icon, Python logo
├── docs/               ← WEB version (GitHub Pages)
│   ├── index.html      ← page structure
│   ├── style.css       ← look
│   ├── app.js          ← all web logic
│   ├── pyworker.js     ← Web Worker that runs Pyodide (Python)
│   ├── data.js         ← GENERATED file (never edit by hand)
│   └── assets/         ← font and images for the web
└── documentation/      ← this documentation and the audit
```

Files created at run time (not in the repo, see `.gitignore`): `progress.json`, `settings.json`, `chat_history.json`.

---

## 4. Architecture – how everything is connected

### 4.1 Desktop

```
                          main.py
                  MainWindow (460×816)
        ┌──────────────┬─────────┬───────────────┐
        │ tab Lectures │ tab PLAY│ tab Help AI   │   ← QStackedWidget
        └──────┬───────┴────┬────┴───────┬───────┘
               │            │            │
        lectures.py      play.py        ai.py
        LecturesPage     PlayPage       ChatPage
        (SECTIONS,       (QStackedWidget)  ├ ChatWidget (chat)
         QWebEngine)       │               └ AccountPage (key, model)
                           │
      ┌──────────┬─────────┼──────────┬──────────┐
      │ idx 0    │ idx 1   │ idx 2    │ idx 3    │
   HotelPage  LevelsPage  QuizPage   TaskLab
   (hotel.py) (12 buttons)(4 options)(lab.py → CodeLab + CHECK)
                                          │
                                   Jupyter kernel
                                   (separate process)

   tasks.py ──► data (QUIZ, CODE, get_task)
   progress.py ─► progress.json
```

`PlayPage` is the **screen manager**: it holds 4 screens in a `QStackedWidget` and switches between them using signals (Qt *signal/slot* mechanism).

### 4.2 Data flow (single source of truth)

```
tasks.py (QUIZ, CODE)   lectures.py (SECTIONS)
        │                       │
        ├── desktop ────────────┤  (imports the modules directly)
        │
        └── build_web_data.py ──► docs/data.js ──► docs/app.js (web)
              (strips solutions)
```

Tasks are written in **one place only** (`tasks.py`). After changing them, run `python build_web_data.py` so the web version gets the changes. Solutions are **not** written to `data.js`, so players cannot find them in the page source.

---

## 5. Data – `tasks.py`

```python
QUIZ[floor] = [ (code, [4 answers], correct_index), ... ]                       # 6 items
CODE[floor] = [ (task_text, expected_output, starter_code, sample_solution), ... ]  # 6 items
```

`get_task(floor, level)` turns (floor, level) into a dict:
- odd level → `QUIZ[floor][(level-1)//2]` → `{"type":"quiz","code","options","answer"}`
- even level → `CODE[floor][level//2 - 1]` → `{"type":"code","text","expected","starter"}` (**the solution is deliberately not returned**; it stays in `tasks.py` for verification only)
- returns `None` if the floor has no tasks or the level is not 1–12.

Example: level 7 → `(7-1)//2 = 3` → the 4th quiz question; level 8 → `8//2-1 = 3` → the 4th coding task.

`S = ""` is just a shorthand for an empty starter code.

### Floors (lessons)

`LESSONS` (in `hotel.py`) is built from `SECTIONS` (in `lectures.py`): all lessons except the book intro (`SECTIONS[0]`) and `ML_25_01_Uvod_1.html` (the `SKIP` set). The result is 26 floors:
16 "Python basics" + 5 "Business decision-making" + 5 "Machine learning". Floor *n* matches lesson *n*.

---

## 6. Desktop – module by module

### 6.1 `main.py`
- Creates `QApplication`, loads the **Press Start 2P** font (`QFontDatabase`) and sets it as the default.
- `STYLE` is a **Qt stylesheet** (CSS-like) for the tab buttons.
- `MainWindow` has a header of 3 buttons (`QPushButton`, `checkable`) in a `QButtonGroup` (exclusive) and a `QStackedWidget` below. A click calls `stack.setCurrentIndex(i)`. The initial tab is **PLAY**.
- On Windows it calls `SetCurrentProcessExplicitAppUserModelID` so the taskbar shows our icon instead of Python's (in `try/except` since it does not exist elsewhere).
- `main()` runs only when the file is executed directly (`if __name__ == "__main__":`), so `main.py` can be imported safely (e.g. in a test).

### 6.2 `hotel.py` – how the hotel looks

**Constants**: `W=320` (scene width), building `BX=32, BW=256`, floor height `FLOOR_H=96`, colours, etc.

**`Hotel(QWidget)`**
- Fixed size: height = top + 26 floors × 96 + lobby. Placed in a `QScrollArea`.
- `paintEvent` draws the roof, billboard, floors, name plates and lobby. **Optimisation**: only the visible floors are drawn (`ev.rect()`).
- Floors are drawn from the top: row `r` maps to floor index `n-1-r` (the top floor is the last lesson, the ground floor is floor 1).
- Each floor is made of rectangles (`fr()` = fillRect): bricks, three windows, a plate `"N. Lesson name"` (elided with `elidedText` if too long) and an `n/12` badge.
- `floor_state(i)` → `"done"` (green), `"cur"` (yellow) or `"locked"` (grey). Because `UNLOCK_ALL = True`, **all floors are unlocked** (intentional). A floor is "done" when all 12 levels are solved.
- **Confetti**: when every floor is finished (`all_done()`), every 85 ticks (~5 s) 48 particles shoot out of the billboard; each has a velocity and "gravity" (`c[3] += 0.35`).
- Mouse: `mouseMoveEvent` changes the cursor (hand / forbidden), `mousePressEvent` emits `floor_clicked(n)` or `door_clicked`. `_floor_at(pos)` converts the y coordinate to a floor.

**`HotelPage(QWidget)`**
- Holds a `QScrollArea` with the hotel and grass (`Ground`); the background (sky gradient, stars, clouds) is painted in `paintEvent`.
- A `QTimer` every 60 ms calls `_frame()` → increments `tick`, moves confetti, refreshes clouds.
- Two `CloudButton`s (up/down arrows) scroll by ±208 px with a `QPropertyAnimation` (250 ms).
- `showEvent` scrolls to the bottom (ground floor) the first time it is shown.

### 6.3 `play.py` – game flow

Classes:

| Class | Role |
|---|---|
| `LevelsPage` | 3-column grid of 12 level buttons for the chosen floor |
| `QuizPage` | Read-only code box + 4 answer buttons |
| `TaskLab(CodeLab)` | Code Lab + **CHECK** and **NEXT** buttons |
| `PlayPage(QStackedWidget)` | Wires all screens together with signals |

**Level state** (`LevelsPage.show_floor`): a level is `done` if solved, `cur` if it is the first unsolved one (`lvl == done_count + 1`), otherwise `locked` (button disabled). So levels must be solved **in order**.

**Quiz** (`QuizPage._pick`): correct answer → green, message "TACNO!", shows NEXT, emits `solved`. Wrong → red and that button is disabled (the player can try again).

**Answer checking – the heart of the game** (`TaskLab`):
1. Click **CHECK** → `check()`: `captured = ""`, `checking = True`, calls `run()`.
2. While the kernel streams output, the overridden `_write()` appends the text both to `captured` and to the screen.
3. When the kernel reports it is done (`_set_running(False)`), `_norm(captured)` is compared with `_norm(expected)`.
4. `same_output` first compares the `_norm` versions (strips trailing spaces from lines and blank lines at the start/end) and then versions where numbers are reduced to a canonical form (`_canon_nums`): `20` and `20.0` count as equal. The web uses the same rule (`LENIENT_NUMBERS`).
5. Match → ">>> TACNO!", show NEXT, emit `solved`. Otherwise → ">>> JOS NE. Trazeni output: …".

`PlayPage._solved` → `progress.mark(floor, level)`. `_next()` opens the next level, or returns to the level list after level 12.

**Signal wiring** (in `PlayPage.__init__`): e.g. `hotel_page.floor_clicked → _open_floor`, `levels.level_chosen → _open_level`, `quiz.solved → _solved`, `lab.next_clicked → _next`. Key point for the defence: **no screen calls another directly; screens only emit signals and `PlayPage` decides what happens next**.

### 6.4 `lab.py` – Code Lab

**`CodeEdit(QPlainTextEdit)`** – an editor with three additions:
- `Ctrl+Enter` → signal `run_requested`.
- `Enter` keeps the previous line's indentation and adds 4 spaces after a `:`.
- `Tab` inserts 4 spaces.

**`CodeLab(QWidget)`** – top: BACK/RUN/STOP/RESET buttons; below, the task text, the editor (stretch 3), the output (stretch 2) and a hidden field for `input()`.

**How execution works** (Jupyter protocol):
1. `ensure_kernel()` → `start_new_kernel("python3")` starts a **separate process** with a Python kernel and returns `km` (KernelManager – controls the process) and `kc` (KernelClient – sends and receives messages). The kernel starts **lazily**, on first use, and stays alive.
2. `run()` → `kc.execute(code)` returns a `msg_id`.
3. A `QTimer` every 40 ms calls `_poll()`:
   - reads the **iopub** channel (kernel output) until `queue.Empty`;
   - checks the **stdin** channel for `input_request`.
4. `_handle(msg)` ignores messages whose `parent_header.msg_id` is not ours. Types:
   - `stream` → ordinary `print` output;
   - `execute_result` / `display_data` → text form of the result (like Jupyter, the last expression is printed);
   - `error` → traceback (ANSI colours removed with the `ANSI` regex);
   - `status: idle` → execution finished, `_set_running(False)`.
5. **Plots**: when the kernel sends `display_data` with `image/png` (e.g. `plt.show()`), `_show_image` decodes the PNG (base64), builds a `QPixmap` and shows it in a `QScrollArea` below the output; images are cleared on the next run / RESET.
6. `input()` → the kernel sends `input_request`; a `QLineEdit` appears and Enter sends `kc.input(text)`.
7. **STOP** → `km.interrupt_kernel()` (like Ctrl+C). **RESET** → `km.restart_kernel()` (all variables are wiped). On app exit (`aboutToQuit`) `shutdown()` is called.

**Why a kernel and not `exec()`/`subprocess`?** Variables persist between runs (the README promises that), and user code cannot crash the game itself because it runs in another process.

### 6.5 `progress.py`
- `_solved` is a set of strings `"floor-level"` (e.g. `"3-5"`), loaded from `progress.json` on import.
- `mark(f, l)` adds and immediately rewrites the whole file.
- `done_count(f)` counts **consecutive** solved levels from the first one (stops at the first unsolved) – this is why levels unlock in order.

### 6.6 `ai.py` – the "Monty Python" AI tutor

- **Settings**: `settings.json` (`key`, `model`); if there is no key, the `GEMINI_API_KEY` environment variable is used. Default model `gemini-3.1-flash-lite`.
- **`SYSTEM`** is the system instruction: answer only about Python and course topics, briefly, in the user's language (Serbian Latin by default), hint first and solution later.
- **`Worker(QThread)`**: the network call runs in its own thread so the window does not freeze. It emits `chunk(str)` for each piece of the answer (*streaming*) and `failed(str)` on error. Errors are translated: 400/401/403 invalid key, 404 model not found, 429 limit reached.
- **`ChatWidget`**:
  - `history` (sent to the model: last 20 messages, with leading "assistant" messages dropped) and `shown` (what the user sees).
  - `send()` appends the message and starts the `Worker`; `_on_chunk` appends text, and rendering is limited to at most once per 80 ms (`render_timer`) so long conversations stay fast; `_on_fail` shows the error and removes the question from history; `_on_done` saves the answer to `chat_history.json`.
  - `render()` builds HTML for the `QTextBrowser`.
- **`fmt(text)`**: converts Markdown-like text to HTML that Qt understands. A code block is opened/closed only by a line that **starts** with ```; an unclosed block (stream in progress) is shown as code to the end. Plain text: `html.escape`, `**bold**`, `` `code` ``. `html.escape` prevents HTML injection from answers.
- **`AccountPage`**: key (masked) and model input; GET KEY opens Google AI Studio.
- The key is stored in plain text in `settings.json` (local, not in the repo). `save_settings` returns `False` if writing fails, and ACCOUNT shows a message.

### 6.7 `lectures.py`
- `SECTIONS`: list of (group name, [(file, title), …]); it is also the source of the floors.
- `book_url(file)` → `https://dazdejkovic.github.io/OI_25_jb1/<file>`; the book is **read online** (it is not in the repo).
- `LecturesPage` (`QStackedWidget`): 0 = book cover (`BookCover`), 1 = chapter list, 2 = reader (`QWebEngineView`, created only on first open). An opened chapter is marked green.

---

## 7. Web version

### 7.1 `docs/index.html` + `style.css`
One page with three "tabs" (`#page-lectures`, `#page-play`, `#page-ai`); inside each there are several "views" (`.view`) and only one is visible (`hidden` attribute). PLAY views: hotel, levels, quiz, lab. This mirrors the `QStackedWidget` structure of the desktop version.

### 7.2 `docs/data.js`
Generated: `window.HOTEL_DATA = { lessons, quiz, code, topics }`. Task entries contain `text, expected, starter` – **no solutions**.

### 7.3 `docs/app.js` – parts in order
| Part | What it does |
|---|---|
| `store` | Wrapper around `localStorage` (JSON, with `try/catch` for private mode) |
| `progress` | Same as `progress.py` (set of `"floor-level"`, `doneCount`) |
| tabs / `showView` | Switching pages and views |
| lectures | Builds the list of links to the online book (`esc()` protects against HTML injection) |
| `sky` | Canvas background, animated every 60 ms |
| `hotel` | Same drawing as `hotel.py` but on `<canvas>` using `devicePixelRatio` (sharp on retina screens); click → floor/door; confetti |
| `getTask`, `showLevels`, `loadQuiz` | Same as `get_task`, `LevelsPage`, `QuizPage` |
| `lab` | Manages the Web Worker: RUN, CHECK, STOP, RESET, `input()` |
| `sameOutput` | Output comparison; `LENIENT_NUMBERS` treats `20` and `20.0` as equal |
| `chat` | Gemini via `fetch` and reading a *Server-Sent Events* stream |

### 7.4 `docs/pyworker.js` – Python in the browser
1. Loads Pyodide 0.27.2 from a CDN (that is why the first run needs internet).
2. In Python it sets `sys.stdout/stderr` to an `_Out` object that forwards every `write` to JavaScript (`_emit`), unbuffered.
3. `_run(src)`: parses the code with `ast`; the **last expression** is evaluated separately and printed (`repr`) – it behaves like Jupyter. Errors are printed without internal frames.
4. `input()`: JS holds the lines from the box under the editor; `setStdin` returns one line at a time (when none are left → `EOFError`).
5. Libraries: `loadPackagesFromImports(code)` finds and loads `numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib` automatically.
6. **Plots**: `__grab_figs()` saves every open matplotlib figure as PNG (base64) and sends it to the page, which displays it.
7. **STOP / RESET**: Pyodide cannot be interrupted from inside, so the **whole Worker is killed (`terminate`) and a new one is created** – hence STOP in the browser clears variables (the README says so).

Worker ↔ page messages (`postMessage`): `status`, `ready`, `out`, `figs`, `done`, `fatal`.

### 7.5 Chat in the web version
`fetch` to `generativelanguage.googleapis.com/.../streamGenerateContent?alt=sse` with the `x-goog-api-key` header (the key is not in the URL). The answer arrives as a stream of `data: {...}` lines; they are parsed line by line and the text is appended to the bubble. Key and history are in `localStorage` (the key is sent only to Google).

---

## 8. Desktop ↔ Web comparison

| | Desktop | Web |
|---|---|---|
| UI | PySide6 widgets | HTML + CSS |
| Hotel drawing | `QPainter` | `<canvas>` 2D |
| Python | Jupyter kernel (process) | Pyodide (WASM) in a Worker |
| Libraries | installed in venv | loaded on demand from a CDN |
| STOP | interrupt, variables stay | worker restart, variables are wiped |
| Plots | shown as images below the output | shown as images below the output |
| Output comparison | `20` = `20.0` (`same_output`) | `20` = `20.0` (`LENIENT_NUMBERS`) |
| Progress | `progress.json` | `localStorage` |
| AI key | `settings.json` | `localStorage` |
| Data | `tasks.py` directly | `data.js` (generated) |

---

## 9. Build and delivery

1. **Changing tasks** → `python build_web_data.py` → commit `docs/data.js`.
2. **Web**: GitHub Pages serves the `docs/` folder (`.nojekyll` disables Jekyll processing).
3. **Windows installer**:
   - `python make_release.py` copies only what the game needs to `release/app` (code, `assets/`, `requirements.txt`); it excludes `docs/`, `documentation/`, personal JSON files and tools. It refuses to run if `requirements.txt` is missing.
   - Inno Setup compiles `installer.iss`: installs to `%LOCALAPPDATA%\PythonHotel` (no admin rights), looks for Python 3.12–3.14 in the registry and, if missing, **downloads Python 3.12.10**; creates `.venv`, runs `pip install -r requirements.txt`; creates shortcuts launching `pythonw.exe main.py`.

### Verifying tasks
`python verify_tasks.py` runs every solution, checks that the starter code does not pass by itself, that quiz answers match the real output and that `docs/data.js` is up to date. Run it after every change to `tasks.py`.

### Running from source (development)
```bash
python -m venv .venv
.venv\Scripts\activate            # Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```
Web locally: `cd docs && python -m http.server 8000`, then open `http://localhost:8000`.

---

## 10. End-to-end example: a player solves level 2 on floor 1

1. In the hotel they click floor 1 → `Hotel.mousePressEvent` → `floor_clicked(1)` → `PlayPage._open_floor`.
2. `LevelsPage.show_floor(1)` draws the grid; level 1 is yellow (`cur`), the rest grey.
3. They solve the quiz (level 1) → `QuizPage._pick` → `solved` → `progress.mark(1,1)` → written to `progress.json`; NEXT → `_next` → `_open_level(1,2)`.
4. `get_task(1,2)` returns the task "Ispisi tekst: Hello, world!"; `TaskLab.load_task` sets `expected`.
5. The player types `print("Hello, world!")` and clicks CHECK.
6. `check()` → `run()` → `kc.execute(...)`; the kernel prints; `_poll` collects `stream` messages into `captured`.
7. The kernel reports `idle` → `_set_running(False)` → `_norm(captured) == _norm(expected)` → ">>> TACNO!", `solved` → `progress.mark(1,2)`, NEXT shown.
8. The badge on the floor plate becomes `2/12`.

---

## 11. Questions the committee may ask (and answers)

**Why a Jupyter kernel instead of `exec()`?**
The player's code runs in a separate process: it cannot crash the game, it can be interrupted (STOP) and restarted (RESET), and variables persist between runs as in Jupyter.

**How does the game know a task is solved?**
It captures the kernel output (`stream` messages), normalises it (`_norm`) and compares it with the expected output. It does not check *how* it was solved, only *what* is printed.

**Why is data in one file while the web has `data.js`?**
A single source of truth prevents inconsistencies. `build_web_data.py` produces `data.js` and removes the solutions.

**Why `QThread` for the AI?**
The network call takes time; on the main thread it would freeze the window. The Worker emits signals (`chunk`, `failed`) and the GUI receives them on the main thread (Qt transfers them safely).

**Why does STOP clear variables in the browser?**
Pyodide is single-threaded WebAssembly that cannot be interrupted from outside; the only way is to kill the Worker.

**Where is the API key and is it safe?**
Only on the user's machine (`settings.json` / `localStorage`), sent only to Google. It is not encrypted on disk; it is not in the repo (`.gitignore`).

**What does `UNLOCK_ALL = True` mean?**
Intentional: all floors are open, but **levels within a floor** still go in order.

**How is the hotel drawn?**
No images: everything is rectangles (`fillRect`) in a loop; the floor is drawn from index `n-1-r`; only visible floors are painted.

**What is signal/slot?**
Qt's notification mechanism: an object emits a signal (`Signal`) and another object's slot (function) is attached with `.connect`. Screens do not know about each other; `PlayPage` wires them together.

**What are the known weaknesses?**
See `AUDIT.en.md`. Most findings are fixed; what remains is the duplicated desktop/web logic, the shared kernel between levels (intentional) and unpinned versions inside Pyodide. Admitting them yourself is better than the committee finding them.

---

## 12. Glossary

- **Kernel** – a separate process that executes Python code and returns results as messages.
- **iopub / stdin** – Jupyter channels: kernel output / input requests.
- **Signal / Slot** – Qt mechanism for communication between objects.
- **Pyodide** – Python precompiled to WebAssembly.
- **Web Worker** – a separate browser thread with no access to the page (talks through messages).
- **SSE** – *Server-Sent Events*, a stream of text events over HTTP (streaming of the AI answer).
- **Streaming** – showing the answer in parts while it is still arriving.
- **venv** – an isolated Python environment with its own libraries.
