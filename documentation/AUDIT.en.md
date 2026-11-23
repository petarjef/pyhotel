# Python Hotel – audit report (English)

Date: 2026-11-23 · Repository state: branch `janjula/busy-mendel-r29paa`, latest commit `c832bd8`.
**No project code was changed.** All tests ran from a temporary environment outside the repo.
Srpska verzija: `AUDIT.sr.md`.

## 1. Summary

The game **works**: both the desktop and web versions passed every functional check that could be run. All 156 coding tasks and 122 of the 156 quiz questions were confirmed automatically by executing the code; the remaining 34 (conceptual questions) were reviewed by hand and are correct. The most serious problem is the **missing `requirements.txt`**, which would make the Windows installer fail. The rest are minor bugs and inconsistencies. **Section 3 describes the state before the fixes; section 4 shows what has been fixed since.**

## 2. What was checked and how

| # | Check | Method | Result |
|---|---|---|---|
| 1 | 156 coding tasks | Ran every "sample solution" and compared its output with `expected` (Python 3.13) | **156/156 pass** |
| 2 | 156 quiz questions | Ran the question code and compared the output with the 4 options | **122 correct (unambiguous)**, 34 conceptual → reviewed by hand, **all correct** |
| 3 | Tasks using `random` (floor 19) and the rest without libraries | Same test on **Python 3.12.7 (Pyodide)** | Same results |
| 4 | Is `docs/data.js` up to date? | Regenerated with `build_web_data.py` and compared | **Identical** (26 floors, 156 + 156) |
| 5 | Desktop app | Ran headless (offscreen) and "clicked" programmatically: tabs, opening a floor, quiz, CHECK, variable persistence, `input()`, STOP, RESET | **All works** |
| 6 | Web app | Chromium (Playwright): lectures, hotel, floor click, quiz, CHECK (right/wrong), variables persist, expression `1+2`, error, `input()`, STOP, variables cleared after STOP | **All works** (Pyodide was redirected locally because the CDN is blocked in the test environment) |
| 7 | Browser console errors | Monitored during the test | **None** |

### What could NOT be verified (check by hand before the presentation)
- The book URLs `dazdejkovic.github.io/OI_25_jb1/...` (network blocked in the test environment) – make sure they open.
- A real call to the **Gemini API** (no key) – the chat was only reviewed in code.
- The **Windows installer** (Inno Setup, registry, Python download) – only the script was reviewed.
- On-screen look (pixel art) – not inspected visually.
- Loading **NumPy/Pandas/SciPy/scikit-learn in Pyodide** on the web (needs the CDN).
- Floor 20–26 quizzes/tasks on the library versions the installer will install (see finding F6).

## 3. Findings

Severity: **High** (breaks things), **Medium** (poor experience / inconsistency), **Low** (cosmetic / cleanup).

### High

**F1. `requirements.txt` is missing.**
`installer.iss` runs `pip install -r "{app}\requirements.txt"`, but the file is not in the repo. The installer cannot install the libraries; the game will not start. The same applies to anyone running from source.
*Suggestion:* add `requirements.txt` (PySide6, jupyter_client, ipykernel, google-genai, numpy, pandas, scipy, scikit-learn, matplotlib), ideally with pinned versions.

### Medium

**F2. Six floor-18 (Matplotlib) tasks pass without a single line written.**
The expected output is `""` and the starter code is just `import matplotlib.pyplot as plt`, so CHECK immediately says "TACNO" (levels 2, 4, 6, 8, 10, 12). Confirmed programmatically.
*Suggestion:* check the figure state (e.g. number of lines, title) instead of output, or require output (`print(len(plt.gca().lines))`).

**F3. Web chat: history may start with a model message → likely error from the Gemini API.**
`app.js` sends `history.slice(-30)`. History alternates user/assistant and has an odd number of items after the question is appended, so with more than 30 items the first item of the slice is a model reply. The desktop version handles this (`while msgs[0].role != "user": pop`), the web does not. I believe the API rejects such a conversation, and a 400 error would be shown as "Key is invalid" (confusing). *I could not test on the real API.*
*Suggestion:* apply the same `while` fix in `app.js`.

**F4. The desktop does not show plots.**
For `plt.show()` the kernel sends an image, but `lab.py` prints only `text/plain` (e.g. `<Figure size 1280x960 with 1 Axes>`). The web version shows images. For floor 18 it means the player on desktop cannot see what they drew.
*Suggestion:* render `image/png` from `display_data`, or at least mention it in the task.

**F5. Desktop and web compare output differently.**
The web has `LENIENT_NUMBERS` (`20` = `20.0`), the desktop does not. The same solution can pass on the web and fail on desktop.
*Suggestion:* make them consistent (disable leniency on the web, or add it to `_norm` on the desktop).

**F6. Library versions are not pinned.**
Floor 20–26 tasks (pandas, scikit-learn, scipy) and some quizzes depend on the exact output/behaviour of the libraries. Tested with pandas 3.1.1, scikit-learn 1.9.1, scipy 1.18.1, numpy 2.5.5. The installer will install "latest" at installation time, and the web uses the versions bundled with Pyodide 0.27.2 (different). Future versions may change output and "break" tasks.
*Suggestion:* pin versions in `requirements.txt` and also verify the tasks on Pyodide.

**F7. Title "Sta ispisuje ovaj kod?" ("What does this code print?") on every quiz question (desktop).**
28 quiz questions have no code that prints anything (e.g. "What is a Monte Carlo simulation for?"), yet the title above is shown.
*Suggestion:* remove the title or show it only when the question contains `print`.

**F8. Shared kernel across levels.**
Variables carry over from level to level (the README lists this as a feature). Consequence: a player can "pass" a task that merely prints a variable left over from earlier. Intentional, but worth knowing for the defence.

### Low

**F9. `make_release.py` and the README disagree.**
The script warns when the folders `book` and `lessons_html` are missing, while the README says the book is neither in the repo nor in the installer. `EXCLUDE_FILES` lists files that do not exist (`make_zip.py`, `convert_lessons.py`, `start.bat`). `docs/` (the web version) is also copied into the installer where it is not needed.

**F10. Dead code:** `DONE_FLOORS`, `PROGRESS` (`hotel.py`), `self.blink` (set, never read), unused variable `extra` in `_paint_plate`, the `locked` branch in `LevelsPage` never runs because `UNLOCK_ALL = True`, two separate imports from `PySide6.QtGui` in `main.py`, `api_key.txt` in `.gitignore` (the file is never used).

**F11. `main.py` starts the application on import** (no `if __name__ == "__main__":`).

**F12. Data is written next to the code** (`progress.json`, `settings.json`, `chat_history.json`). Works in `%LOCALAPPDATA%` but would fail in a folder without write permission. `progress.mark` and `ai.save_settings` do not catch write errors (reading is guarded, writing is not).

**F13. Broad `except` blocks** in `lab._poll`, `ai.load_*`, `ai.save_history` sweep errors under the rug; good for stability, bad for debugging.

**F14. The chat re-renders everything on every chunk** (`ChatWidget._on_chunk → render()`): slow for long conversations.

**F15. Mixed languages and spelling.** Messages are in both Serbian and English; Serbian text has no diacritics (probably intentional). Typo in floor 10 task (level 8): "terarni operator" → "ternarni".

**F16. Security / privacy (informational).** The API key is stored in plain text (`settings.json`, `localStorage`). The Jupyter kernel talks over local TCP without encryption (console warning) – localhost only. AI answer text is properly escaped (no HTML injection).

**F17. Possible race in `lab._poll`** (output arriving after `idle`): not observed in tests; mentioned because CHECK could then wrongly say "JOS NE".

**F18. Duplicated logic** between `hotel.py` and `app.js` (drawing, checking). Any rule change must be made in two places.

## 4. Fix status

All findings were addressed. After the fixes, the following were re-run: `verify_tasks.py` (156 tasks, 121 quizzes with output, `data.js` – all fine), the desktop test (offscreen) and the web test (Chromium).

| Finding | Status | What was done |
|---|---|---|
| F1 | ✅ fixed | Added `requirements.txt` with pinned, tested versions; `make_release.py` refuses to run without it |
| F2 | ✅ fixed | Floor 18 tasks now require printing the plot state (line count, title, labels, legend); the starter no longer passes by itself; `verify_tasks.py` checks it |
| F3 | ✅ fixed | `app.js` drops leading model messages from the history; tested with a fake reply (29 messages sent, the first is the user's) |
| F4 | ✅ fixed | Desktop shows `image/png` plots below the output (tested) |
| F5 | ✅ fixed | Desktop got the same lenient number comparison as the web (`same_output`), following the intent of the "fix output check" commit |
| F6 | ⚠ partial | Versions pinned in `requirements.txt`. Checking floors 20–26 inside Pyodide is still impossible without CDN access; test manually in a browser |
| F7 | ✅ fixed | Title "Sta ispisuje ovaj kod?" hidden when the question is in a comment (35 questions have no `print`, the title is hidden for 34; the one with `t[0]=5` keeps it) |
| F8 | ➖ no change | Intentional behaviour (README); stays documented |
| F9 | ✅ fixed | `make_release.py` cleaned: no nonexistent files, does not copy `docs/`, `documentation/`, tools |
| F10 | ✅ fixed | Removed `DONE_FLOORS`, `PROGRESS`, `blink`, `extra`, the duplicate import, `api_key.txt`. The `locked` branch stays because it depends on `UNLOCK_ALL` |
| F11 | ✅ fixed | `if __name__ == "__main__":` in `main.py` |
| F12 | ✅ fixed | `progress.mark` and `ai.save_settings` catch write errors; ACCOUNT shows a message |
| F13 | ✅ fixed | `except Exception` replaced with narrower exceptions in `ai.py`; `lab._poll` has one clear block that reports the error type |
| F14 | ✅ fixed | Chat rendering limited to once per 80 ms (200 chunks → 1 render) |
| F15 | ⚠ partial | Fixed "terarni" → "ternarni". The Serbian/English mix stays (authors' decision) |
| F16 | ➖ no change | Informational |
| F17 | ➖ not a bug | Jupyter sends output and `idle` over the same iopub channel, so the order is guaranteed; the race cannot happen on that path |
| F18 | ⚠ partial | Duplicated desktop/web logic is unavoidable; added `verify_tasks.py` to keep the data consistent |

### How to re-check
```bash
pip install -r requirements.txt
python verify_tasks.py
```
