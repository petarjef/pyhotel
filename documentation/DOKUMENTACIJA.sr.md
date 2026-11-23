# Python Hotel – tehnička dokumentacija (srpski)

> Namena: da oba autora mogu da objasne **svaki** deo koda na odbrani.
> Pregled grešaka i rizika je u zasebnom fajlu `AUDIT.sr.md`.
> English version: `DOCUMENTATION.en.md`.

---

## 1. Šta je projekat

**Python Hotel** je edukativna igra za učenje Pythona. Igrač se „penje“ kroz piksel-art hotel: **svaki sprat je jedna lekcija** iz kursa *Poslovno odlučivanje i mašinsko učenje* (knjiga: Aždejković, Radojičić, Stamenković). Ima 26 spratova, a svaki sprat ima 12 nivoa:

| Nivo | Tip | Šta igrač radi |
|---|---|---|
| 1, 3, 5, 7, 9, 11 | **Kviz** | Bira jedan od 4 ponuđena odgovora (npr. „šta ispisuje ovaj kod?“) |
| 2, 4, 6, 8, 10, 12 | **Kod** | Piše Python kod čiji **ispis** mora da bude identičan traženom |

Ukupno: 26 × 6 = **156 kviz pitanja** i 26 × 6 = **156 programerskih zadataka**.

Pored igre postoje:
- **Code Lab** – slobodan Python editor (vrata u prizemlju hotela).
- **Lectures** – spisak poglavlja knjige koja se otvaraju sa interneta.
- **Help AI (Monty Python)** – čet sa AI tutorom (Google Gemini, korisnikov besplatan API ključ).

Postoje **dve verzije** iste igre:
1. **Desktop** (Python + PySide6/Qt) – instalira se na Windows preko instalera.
2. **Web** (HTML + JavaScript + Pyodide) – radi u browseru, hostuje se na GitHub Pages iz fascikle `docs/`.

---

## 2. Tehnologije i zašto su izabrane

| Tehnologija | Gde | Zašto |
|---|---|---|
| **Python 3.12+** | desktop | Jezik koji učimo, sav kod je u njemu |
| **PySide6 (Qt 6)** | desktop UI | Zvanični Qt za Python; imamo prozore, widgete, crtanje (`QPainter`), niti (`QThread`), web prikaz (`QWebEngineView`) |
| **jupyter_client + ipykernel** | desktop lab | Pravi Python kernel kao u Jupyter notebooku: čuva promenljive između pokretanja, podržava `input()`, prekid i restart |
| **google-genai** | desktop AI | Zvanična biblioteka za Gemini API (streaming odgovora) |
| **JavaScript (bez frameworka)** | web | Jednostavno, nema build koraka, radi na GitHub Pages |
| **Pyodide 0.27.2** | web lab | CPython kompajliran u WebAssembly – pravi Python direktno u browseru, bez servera |
| **Web Worker** | web lab | Pyodide radi u zasebnoj niti pa dugačak kod ne zamrzava stranicu i **STOP** može da je ugasi |
| **Canvas 2D** | web | Isto piksel-art crtanje kao `QPainter` u desktop verziji |
| **localStorage** | web | Čuvanje progresa, API ključa i istorije četa u browseru |
| **Inno Setup** | instaler | Pravi `PythonHotel_Setup.exe` za Windows |
| **Font Press Start 2P** | oba | Retro piksel izgled |

---

## 3. Struktura repozitorijuma

```
pyhotel/
├── main.py             ← ulazna tačka desktop aplikacije (prozor + 3 taba)
├── play.py             ← „igra“: hotel → nivoi → kviz / lab; provera rešenja
├── hotel.py            ← crtanje hotela (QPainter), klikovi na spratove
├── lab.py              ← Code Lab: editor + Jupyter kernel
├── tasks.py            ← SVI podaci: 156 kvizova + 156 zadataka (+ rešenja)
├── progress.py         ← čuvanje rešenih nivoa u progress.json
├── ai.py               ← čet sa Gemini AI tutorom + stranica ACCOUNT
├── lectures.py         ← spisak lekcija (SECTIONS) + čitač knjige
├── build_web_data.py   ← generiše docs/data.js iz tasks.py + lectures.py
├── make_release.py     ← priprema fascikle release/app za instaler
├── installer.iss       ← skripta za Inno Setup (Windows instaler)
├── assets/             ← font, ikonica, Python logo
├── docs/               ← WEB verzija (GitHub Pages)
│   ├── index.html      ← struktura stranice
│   ├── style.css       ← izgled
│   ├── app.js          ← sva logika web verzije
│   ├── pyworker.js     ← Web Worker u kome radi Pyodide (Python)
│   ├── data.js         ← GENERISAN fajl (ne uređuje se ručno)
│   └── assets/         ← font i slike za web
└── documentation/      ← ova dokumentacija i audit
```

Fajlovi koje aplikacija pravi u toku rada (nisu u repou, vidi `.gitignore`): `progress.json`, `settings.json`, `chat_history.json`.

---

## 4. Arhitektura – kako je sve povezano

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
        (SECTIONS,       (QStackedWidget)  ├ ChatWidget (čet)
         QWebEngine)       │               └ AccountPage (ključ, model)
                           │
      ┌──────────┬─────────┼──────────┬──────────┐
      │ idx 0    │ idx 1   │ idx 2    │ idx 3    │
   HotelPage  LevelsPage  QuizPage   TaskLab
   (hotel.py) (12 dugmadi)(4 opcije) (lab.py → CodeLab + CHECK)
                                          │
                                   Jupyter kernel
                                   (poseban proces)

   tasks.py ──► podaci (QUIZ, CODE, get_task)
   progress.py ─► progress.json
```

`PlayPage` je **upravljač ekrana**: drži 4 ekrana u `QStackedWidget`‑u i prebacuje se signalima (Qt *signal/slot* mehanizam).

### 4.2 Tok podataka (jedan izvor istine)

```
tasks.py (QUIZ, CODE)   lectures.py (SECTIONS)
        │                       │
        ├── desktop ────────────┤  (direktno uvozi module)
        │
        └── build_web_data.py ──► docs/data.js ──► docs/app.js (web)
              (izbacuje rešenja)
```

Zadaci se pišu **samo na jednom mestu** (`tasks.py`). Kada se oni promene, mora da se pokrene `python build_web_data.py` da bi web verzija dobila izmene. Rešenja (`solution`) se **ne** upisuju u `data.js` da ih igrač ne bi našao u izvornom kodu stranice.

---

## 5. Podaci – `tasks.py`

```python
QUIZ[sprat] = [ (kod, [4 odgovora], indeks_tačnog), ... ]   # 6 stavki
CODE[sprat] = [ (tekst_zadatka, očekivani_ispis, početni_kod, primer_rešenja), ... ]  # 6 stavki
```

`get_task(floor, level)` pretvara (sprat, nivo) u rečnik:
- neparan nivo → `QUIZ[floor][(level-1)//2]` → `{"type":"quiz","code","options","answer"}`
- paran nivo → `CODE[floor][level//2 - 1]` → `{"type":"code","text","expected","starter","solution"}`
- vraća `None` ako sprat nema zadatke ili nivo nije 1–12.

Primer: nivo 7 → `(7-1)//2 = 3` → četvrto kviz pitanje; nivo 8 → `8//2-1 = 3` → četvrti zadatak.

Promenljiva `S = ""` je samo prazan početni kod (skraćenica).

### Spratovi (lekcije)

`LESSONS` (u `hotel.py`) se gradi iz `SECTIONS` (u `lectures.py`): sve lekcije osim uvoda knjige (`SECTIONS[0]`) i `ML_25_01_Uvod_1.html` (skup `SKIP`). Rezultat je 26 spratova:
16 „Osnove Pajtona“ + 5 „Poslovno odlučivanje“ + 5 „Mašinsko učenje“. Sprat *n* odgovara lekciji *n*.

---

## 6. Desktop – modul po modul

### 6.1 `main.py`
- Pravi `QApplication`, učitava font **Press Start 2P** (`QFontDatabase`) i postavlja ga kao podrazumevani.
- `STYLE` je **Qt stylesheet** (sličan CSS‑u) za dugmad tabova.
- `MainWindow` ima zaglavlje od 3 dugmeta (`QPushButton`, `checkable`) u `QButtonGroup` (isključivi izbor) i `QStackedWidget` ispod. Klik na dugme menja `stack.setCurrentIndex(i)`. Početni tab je **PLAY**.
- Na Windowsu poziva `SetCurrentProcessExplicitAppUserModelID` da traka zadataka prikaže našu ikonicu umesto Pythonove (u `try/except` jer na drugim sistemima ne postoji).
- Napomena: `main()` se poziva na dnu fajla bez provere `__name__ == "__main__"`.

### 6.2 `hotel.py` – izgled hotela

**Konstante**: `W=320` (širina scene), zgrada `BX=32, BW=256`, visina sprata `FLOOR_H=96`, boje, itd.

**`Hotel(QWidget)`**
- Fiksne dimenzije: visina = vrh + 26 spratova × 96 + prizemlje. Nalazi se u `QScrollArea`.
- `paintEvent` crta krov, bilbord, spratove, table sa nazivom, prizemlje. **Optimizacija**: crta samo spratove koji se vide (`ev.rect()`).
- Sprat se crta od vrha: red `r` odgovara sprat‑indeksu `n-1-r` (najviši sprat je poslednja lekcija, prizemlje je sprat 1).
- Svaki sprat se crta pravougaonicima (`fr()` = fillRect): cigle, tri prozora, tabla `"N. Naziv lekcije"` (skraćena `elidedText` ako je predugačka) i značka `n/12`.
- `floor_state(i)` → `"done"` (zeleno), `"cur"` (žuto) ili `"locked"` (sivo). Zbog `UNLOCK_ALL = True` **svi spratovi su otključani** (namerno). Sprat je „done“ kad su rešena svih 12 nivoa.
- **Konfeti**: kad su svi spratovi završeni (`all_done()`), na svakih 85 „tikova“ (~5 s) iz bilborda izlazi 48 čestica; svaka ima brzinu i „gravitaciju“ (`c[3] += 0.35`).
- Miš: `mouseMoveEvent` menja kursor (ruka/zabranjeno), `mousePressEvent` emituje `floor_clicked(n)` ili `door_clicked`. `_floor_at(pos)` pretvara y‑koordinatu u sprat.

**`HotelPage(QWidget)`**
- Drži `QScrollArea` sa hotelom i travom (`Ground`), pozadinu (gradijent neba, zvezde, oblaci) crta u `paintEvent`.
- `QTimer` na 60 ms poziva `_frame()` → povećava `tick`, pomera konfete, osvežava oblake.
- Dva `CloudButton`‑a (strelice gore/dole) skroluju za ±208 px animacijom `QPropertyAnimation` (250 ms).
- `showEvent` pri prvom prikazivanju skroluje do dna (prizemlje).

### 6.3 `play.py` – tok igre

Klase:

| Klasa | Uloga |
|---|---|
| `LevelsPage` | Mreža 4×3 sa 12 dugmadi nivoa za izabrani sprat |
| `QuizPage` | Kod u read‑only polju + 4 dugmeta sa odgovorima |
| `TaskLab(CodeLab)` | Code Lab + dugmad **CHECK** i **NEXT** |
| `PlayPage(QStackedWidget)` | Povezuje sve ekrane signalima |

**Stanje nivoa** (`LevelsPage.show_floor`): nivo je `done` ako je rešen, `cur` ako je prvi nerešen (`lvl == done_count + 1`), inače `locked` (dugme onemogućeno). Znači nivoi se rešavaju **redom**.

**Kviz** (`QuizPage._pick`): tačan odgovor → zeleno, poruka „TACNO!“, prikazuje NEXT, emituje `solved`. Netačan → crveno i dugme se onemogući (može se probati ponovo).

**Provera koda – srce igre** (`TaskLab`):
1. Klik na **CHECK** → `check()`: `captured = ""`, `checking = True`, pozove `run()`.
2. Dok kernel šalje ispis, `_write()` (pregazena metoda) dodaje tekst i u `captured` i na ekran.
3. Kad kernel javi da je završio (`_set_running(False)`), poredi se `_norm(captured)` sa `_norm(expected)`.
4. `_norm` uklanja razmake na kraju svake linije i prazne linije na početku/kraju.
5. Poklapanje → „>>> TACNO!“, prikaži NEXT, emituj `solved`. Inače → „>>> JOS NE. Trazeni output: …“.

`PlayPage._solved` → `progress.mark(floor, level)`. `_next()` otvara sledeći nivo, ili vraća na listu nivoa posle 12.

**Povezivanje signala** (u `PlayPage.__init__`): npr. `hotel_page.floor_clicked → _open_floor`, `levels.level_chosen → _open_level`, `quiz.solved → _solved`, `lab.next_clicked → _next`. Ovo je ključno za odbranu: **niko ne zove nekog direktno, svi ekrani samo emituju signale, a `PlayPage` odlučuje šta dalje**.

### 6.4 `lab.py` – Code Lab

**`CodeEdit(QPlainTextEdit)`** – editor sa tri dodatka:
- `Ctrl+Enter` → signal `run_requested`.
- `Enter` zadržava uvlačenje prethodne linije, a posle `:` dodaje još 4 razmaka.
- `Tab` ubacuje 4 razmaka.

**`CodeLab(QWidget)`** – vrh: dugmad BACK/RUN/STOP/RESET; ispod tekst zadatka, editor (razmera 3), izlaz (razmera 2) i skriveno polje za `input()`.

**Kako radi izvršavanje** (Jupyter protokol):
1. `ensure_kernel()` → `start_new_kernel("python3")` pokreće **poseban proces** sa Python kernelom i vraća `km` (KernelManager – upravlja procesom) i `kc` (KernelClient – šalje i prima poruke). Kernel se pokreće **lenjo**, tek pri prvom korišćenju, i ostaje živ.
2. `run()` → `kc.execute(kod)` vraća `msg_id`.
3. `QTimer` na 40 ms zove `_poll()`:
   - čita **iopub** kanal (ispis kernela) dok ne dobije `queue.Empty`;
   - proverava **stdin** kanal za `input_request`.
4. `_handle(msg)` ignoriše poruke čiji `parent_header.msg_id` nije naš. Tipovi:
   - `stream` → običan `print` ispis;
   - `execute_result` / `display_data` → tekstualni oblik rezultata (kao u Jupyteru, poslednji izraz se ispisuje);
   - `error` → traceback (ANSI boje se uklanjaju regexom `ANSI`);
   - `status: idle` → izvršavanje gotovo, `_set_running(False)`.
5. `input()` → kernel šalje `input_request`; prikaže se `QLineEdit`, a Enter šalje `kc.input(text)`.
6. **STOP** → `km.interrupt_kernel()` (kao Ctrl+C). **RESET** → `km.restart_kernel()` (brišu se sve promenljive). Pri gašenju aplikacije (`aboutToQuit`) poziva se `shutdown()`.

**Zašto kernel, a ne `exec()`/`subprocess`?** Promenljive ostaju između pokretanja (README to garantuje), a korisnički kod ne može da sruši samu igru jer radi u drugom procesu.

### 6.5 `progress.py`
- `_solved` je skup stringova `"sprat-nivo"` (npr. `"3-5"`), učitan iz `progress.json` pri uvozu.
- `mark(f, l)` dodaje i odmah upisuje celu datoteku.
- `done_count(f)` broji **uzastopno** rešene nivoe od prvog (prekida se na prvom nerešenom) – zato se nivoi otključavaju redom.

### 6.6 `ai.py` – AI tutor „Monty Python“

- **Podešavanja**: `settings.json` (`key`, `model`); ako ključa nema, uzima se promenljiva okruženja `GEMINI_API_KEY`. Podrazumevani model `gemini-3.1-flash-lite`.
- **`SYSTEM`** je sistemska instrukcija: odgovara samo o Pythonu i temama kursa, kratko, na jeziku korisnika (podrazumevano srpski latinica), prvo savet pa rešenje.
- **`Worker(QThread)`**: mrežni poziv radi u zasebnoj niti da se prozor ne zamrzne. Emituje `chunk(str)` za svaki deo odgovora (*streaming*) i `failed(str)` pri grešci. Greške se prevode u poruke: 400/401/403 neispravan ključ, 404 model ne postoji, 429 dostignut limit.
- **`ChatWidget`**:
  - `history` (šalje se modelu, poslednjih 20 poruka, bez vodećih „assistant“ poruka) i `shown` (ono što korisnik vidi).
  - `send()` dodaje poruku, pokreće `Worker`; `_on_chunk` nadovezuje tekst i ponovo iscrtava; `_on_fail` prikazuje grešku i izbacuje pitanje iz istorije; `_on_done` čuva odgovor u `chat_history.json`.
  - `render()` pravi HTML za `QTextBrowser`.
- **`fmt(text)`**: pretvara Markdown‑sličan tekst u HTML koji Qt razume. Blok koda otvara/zatvara samo linija koja **počinje** sa ```, a nezatvoren blok (stream u toku) prikazuje se kao kod do kraja. Običan tekst: `html.escape`, `**bold**`, `` `kod` ``. `html.escape` sprečava ubacivanje HTML‑a iz odgovora.
- **`AccountPage`**: unos ključa (maskiran) i modela, dugme GET KEY otvara Google AI Studio.
- Ključ je u običnom tekstu u `settings.json` (lokalno, nije u repou).

### 6.7 `lectures.py`
- `SECTIONS`: lista (naziv grupe, [(fajl, naslov), …]); to je i izvor za spratove.
- `book_url(file)` → `https://dazdejkovic.github.io/OI_25_jb1/<fajl>`; knjiga se **čita onlajn** (nije u repou).
- `LecturesPage` (`QStackedWidget`): 0 = korice knjige (`BookCover`), 1 = lista poglavlja, 2 = čitač (`QWebEngineView`, pravi se tek pri prvom otvaranju). Otvoreno poglavlje se obeleži zeleno.

---

## 7. Web verzija

### 7.1 `docs/index.html` + `style.css`
Jedna stranica sa tri „taba“ (`#page-lectures`, `#page-play`, `#page-ai`), a unutar svakog više „pogleda“ (`.view`) od kojih je vidljiv samo jedan (`hidden` atribut). Pogledi PLAY: hotel, nivoi, kviz, lab. Ovo je isti raspored kao `QStackedWidget` u desktop verziji.

### 7.2 `docs/data.js`
Generisan: `window.HOTEL_DATA = { lessons, quiz, code, topics }`. Kod zadataka sadrži `text, expected, starter` – **bez rešenja**.

### 7.3 `docs/app.js` – delovi redom
| Deo | Šta radi |
|---|---|
| `store` | Omotač oko `localStorage` (JSON, sa `try/catch` za privatni mod) |
| `progress` | Isto što i `progress.py` (skup `"sprat-nivo"`, `doneCount`) |
| tabovi / `showView` | Prebacivanje stranica i pogleda |
| lectures | Pravi listu linkova ka onlajn knjizi (`esc()` štiti od HTML ubacivanja) |
| `sky` | Pozadina na canvasu, animacija na 60 ms |
| `hotel` | Isto crtanje kao `hotel.py`, ali na `<canvas>` uz `devicePixelRatio` (oštro na retina ekranima); klik → sprat/vrata; konfeti |
| `getTask`, `showLevels`, `loadQuiz` | Isto kao `get_task`, `LevelsPage`, `QuizPage` |
| `lab` | Upravlja Web Workerom: RUN, CHECK, STOP, RESET, `input()` |
| `sameOutput` | Poređenje ispisa; `LENIENT_NUMBERS` tretira `20` i `20.0` kao isto |
| `chat` | Gemini preko `fetch` i čitanja *Server‑Sent Events* toka |

### 7.4 `docs/pyworker.js` – Python u browseru
1. Učitava Pyodide 0.27.2 sa CDN‑a (zato treba internet pri prvom pokretanju).
2. U Pythonu postavlja `sys.stdout/stderr` na objekat `_Out` koji svaki `write` prosleđuje JavaScriptu (`_emit`), bez baferovanja.
3. `_run(src)`: parsira kod pomoću `ast`; **poslednji izraz** se izračunava posebno i ispisuje (`repr`) – ponaša se kao Jupyter. Greške se ispisuju bez internih okvira.
4. `input()`: JS ima listu linija iz polja ispod editora; `setStdin` vraća jednu po jednu liniju (kad ponestane → `EOFError`).
5. Biblioteke: `loadPackagesFromImports(kod)` sam pronađe i učita `numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib`.
6. **Grafikoni**: `__grab_figs()` svaku otvorenu matplotlib figuru sačuva kao PNG (base64) i pošalje stranici koja ih prikaže.
7. **STOP / RESET**: Pyodide se ne može prekinuti iznutra, pa se **ceo Worker ubije (`terminate`) i napravi nov** – zato STOP u browseru briše promenljive (README to navodi).

Poruke Worker ↔ stranica (`postMessage`): `status`, `ready`, `out`, `figs`, `done`, `fatal`.

### 7.5 Čet u web verziji
`fetch` ka `generativelanguage.googleapis.com/.../streamGenerateContent?alt=sse` sa zaglavljem `x-goog-api-key` (ključ nije u URL‑u). Odgovor stiže kao tok linija `data: {...}`; parsiraju se po linijama i tekst se dodaje u balon. Ključ i istorija su u `localStorage` (ključ se šalje samo Google‑u).

---

## 8. Desktop ↔ Web: poređenje

| | Desktop | Web |
|---|---|---|
| UI | PySide6 widgeti | HTML + CSS |
| Crtanje hotela | `QPainter` | `<canvas>` 2D |
| Python | Jupyter kernel (proces) | Pyodide (WASM) u Workeru |
| Biblioteke | instalirane u venv | učitavaju se po potrebi sa CDN‑a |
| STOP | prekid, promenljive ostaju | restart radnika, promenljive se brišu |
| Grafikoni | ne prikazuju se (samo tekst figure) | prikazuju se kao slike |
| Poređenje ispisa | strogo | blago (`20` = `20.0`) |
| Progres | `progress.json` | `localStorage` |
| Ključ AI | `settings.json` | `localStorage` |
| Podaci | `tasks.py` direktno | `data.js` (generisan) |

---

## 9. Izgradnja i isporuka

1. **Izmena zadataka** → `python build_web_data.py` → komituj `docs/data.js`.
2. **Web**: GitHub Pages servira fasciklu `docs/` (`.nojekyll` isključuje Jekyll obradu).
3. **Windows instaler**:
   - `python make_release.py` kopira projekat u `release/app` (izuzima `.venv`, `.git`, lične JSON fajlove…).
   - Inno Setup kompajlira `installer.iss`: instalira u `%LOCALAPPDATA%\PythonHotel` (bez admin prava), traži Python 3.12–3.14 u registru, a ako ga nema, **skida Python 3.12.10**; pravi `.venv`, radi `pip install -r requirements.txt`; pravi prečice koje pokreću `pythonw.exe main.py`.
   - ⚠ Fajl `requirements.txt` trenutno ne postoji u repou (vidi audit).

### Pokretanje iz izvornog koda (razvoj)
```bash
python -m venv .venv
.venv\Scripts\activate            # Linux/Mac: source .venv/bin/activate
pip install PySide6 jupyter_client ipykernel google-genai \
            numpy pandas scipy scikit-learn matplotlib
python main.py
```
Web lokalno: `cd docs && python -m http.server 8000` pa `http://localhost:8000`.

---

## 10. Primer od početka do kraja: igrač rešava nivo 2 na spratu 1

1. U hotelu klikne na sprat 1 → `Hotel.mousePressEvent` → `floor_clicked(1)` → `PlayPage._open_floor`.
2. `LevelsPage.show_floor(1)` crta mrežu; nivo 1 je žut (`cur`), ostali sivi.
3. Reši kviz (nivo 1) → `QuizPage._pick` → `solved` → `progress.mark(1,1)` → upis u `progress.json`; NEXT → `_next` → `_open_level(1,2)`.
4. `get_task(1,2)` vraća zadatak „Ispiši tekst: Hello, world!“; `TaskLab.load_task` postavlja `expected`.
5. Igrač upiše `print("Hello, world!")` i klikne CHECK.
6. `check()` → `run()` → `kc.execute(...)`; kernel ispisuje; `_poll` skuplja `stream` poruke u `captured`.
7. Kernel javi `idle` → `_set_running(False)` → `_norm(captured) == _norm(expected)` → „>>> TACNO!“, `solved` → `progress.mark(1,2)`, prikaz NEXT.
8. Značka na tabli sprata postaje `2/12`.

---

## 11. Pitanja koja komisija može da postavi (i odgovori)

**Zašto Jupyter kernel umesto `exec()`?**
Kod igrača radi u odvojenom procesu: ne može da sruši igru, može da se prekine (STOP) i restartuje (RESET), a promenljive ostaju između pokretanja kao u Jupyteru.

**Kako igra zna da je zadatak tačno rešen?**
Hvata ispis kernela (`stream` poruke), normalizuje ga (`_norm`) i poredi sa očekivanim ispisom. Ne proverava *kako* je rešeno, samo *šta* se ispisuje.

**Zašto su zadaci u jednom fajlu, a web ima `data.js`?**
Jedan izvor istine sprečava neslaganje. `build_web_data.py` pravi `data.js` i izbacuje rešenja.

**Zašto `QThread` za AI?**
Mrežni poziv traje; u glavnoj niti bi zamrzao prozor. Worker emituje signale (`chunk`, `failed`), a GUI ih prima u glavnoj niti (Qt to bezbedno prenosi).

**Zašto u browseru STOP briše promenljive?**
Pyodide je jednonitni WebAssembly koji se ne može prekinuti spolja; jedini način je gašenje Workera.

**Gde je API ključ i da li je bezbedan?**
Samo kod korisnika (`settings.json` / `localStorage`), šalje se isključivo Googleu. Nije enkriptovan na disku; nije u repou (`.gitignore`).

**Šta znači `UNLOCK_ALL = True`?**
Namerno: svi spratovi su otvoreni, ali su **nivoi unutar sprata** i dalje redom.

**Kako radi crtanje hotela?**
Bez slika: sve su pravougaonici (`fillRect`) u petlji; sprat se crta od indeksa `n-1-r`; crtaju se samo vidljivi spratovi.

**Šta je signal/slot?**
Qt mehanizam obaveštavanja: objekat emituje signal (`Signal`), a drugi slot (funkcija) je povezan sa `.connect`. Ekrani ne znaju jedni za druge; `PlayPage` ih spaja.

**Koje su poznate slabosti?**
Pogledaj `AUDIT.sr.md` (fali `requirements.txt`, zadaci sprata 18 prolaze bez koda, neslaganja desktop/web…). Spremno priznati je bolje nego da komisija sama otkrije.

---

## 12. Rečnik

- **Kernel** – odvojeni proces koji izvršava Python kod i vraća rezultate porukama.
- **iopub / stdin** – Jupyter kanali: izlaz kernela / zahtevi za unos.
- **Signal / Slot** – Qt mehanizam za komunikaciju među objektima.
- **Pyodide** – Python prekompajliran u WebAssembly.
- **Web Worker** – zasebna nit u browseru bez pristupa stranici (komunicira porukama).
- **SSE** – *Server‑Sent Events*, tok tekstualnih događaja preko HTTP‑a (strimovanje odgovora AI‑ja).
- **Streaming** – prikaz odgovora delimično, dok još stiže.
- **venv** – izolovano Python okruženje sa sopstvenim bibliotekama.
