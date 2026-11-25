# Python Hotel – izveštaj o auditu (srpski)

Datum: 2026-11-23 · Stanje repozitorijuma: grana `janjula/busy-mendel-r29paa`, poslednji komit `c832bd8`.
**U kodu projekta ništa nije menjano.** Svi testovi su radili iz privremenog okruženja van repoa.
English version: `AUDIT.en.md`.

## 1. Kratak zaključak

Igra **radi**: desktop i web verzija prošle su sve funkcionalne provere koje su mogle da se izvedu. Svih 156 programerskih zadataka i 122 od 156 kviz pitanja automatski su potvrđeni izvršavanjem koda; preostalih 34 (konceptualna pitanja) pregledana su ručno i tačna su. Najozbiljniji problem je **nedostajući `requirements.txt`**, zbog kog bi Windows instaler pao. Ostalo su manje greške i nedoslednosti. **Odeljak 3 opisuje stanje pre popravki; šta je od toga popravljeno vidi se u odeljku 4.**

## 2. Šta je proveravano i kako

| # | Provera | Metod | Rezultat |
|---|---|---|---|
| 1 | 156 programerskih zadataka | Izvršeno svako „primer rešenje“ i poređen ispis sa `expected` (Python 3.13) | **156/156 prolazi** |
| 2 | 156 kviz pitanja | Izvršen kod pitanja, ispis poređen sa 4 opcije | **122 tačno (jednoznačno)**, 34 konceptualna → ručno pregledana, **sve tačno** |
| 3 | Zadaci sa `random` (sprat 19) i ostali bez biblioteka | Isti test na **Pythonu 3.12.7 (Pyodide)** | Isti rezultati |
| 4 | `docs/data.js` ažuran? | Ponovo generisan `build_web_data.py` i upoređen | **Identičan** (26 spratova, 156 + 156) |
| 5 | Desktop aplikacija | Pokrenuta headless (offscreen) i programski „kliknuta“: tabovi, otvaranje sprata, kviz, CHECK, čuvanje promenljivih, `input()`, STOP, RESET | **Sve radi** |
| 6 | Web aplikacija | Chromium (Playwright): lekcije, hotel, klik na sprat, kviz, CHECK (tačno/netačno), promenljive ostaju, izraz `1+2`, greška, `input()`, STOP, posle STOP promenljive brišu | **Sve radi** (Pyodide lokalno preusmeren jer je CDN blokiran u testnom okruženju) |
| 7 | Greške u konzoli browsera | Praćeno tokom testa | **Nema** |

### Šta NIJE moglo da se proveri (treba ručno pre odbrane)
- Adrese knjige `dazdejkovic.github.io/OI_25_jb1/...` (mreža iz testnog okruženja je blokirana) – proveri da otvaraju.
- Stvarni poziv ka **Gemini API‑ju** (nema ključa) – čet je čitan samo iz koda.
- **Windows instaler** (Inno Setup, registar, preuzimanje Pythona) – samo pregled skripte.
- Izgled na ekranu (piksel‑art) – nije pregledan vizuelno.
- Učitavanje **NumPy/Pandas/SciPy/scikit‑learn u Pyodide‑u** na webu (zahteva CDN).
- Kviz/zadaci sprata 20–26 na verzijama biblioteka koje instalira instaler (vidi nalaz N6).

## 3. Nalazi

Ozbiljnost: **Visoka** (pokvari rad), **Srednja** (loš doživljaj / nedoslednost), **Niska** (kozmetika / čišćenje).

### Visoka

**N1. Nedostaje `requirements.txt`.**
`installer.iss` radi `pip install -r "{app}\requirements.txt"`, a fajla nema u repou. Instaler ne može da instalira biblioteke; igra se ne pokreće. Isto važi za svakoga ko želi da pokrene iz izvornog koda.
*Predlog:* dodati `requirements.txt` (PySide6, jupyter_client, ipykernel, google-genai, numpy, pandas, scipy, scikit-learn, matplotlib), po mogućstvu sa fiksiranim verzijama.

### Srednja

**N2. Šest zadataka sprata 18 (Matplotlib) prolazi bez ijednog napisanog reda.**
Očekivani ispis je `""`, a početni kod je samo `import matplotlib.pyplot as plt`, pa CHECK odmah javlja „TACNO“ (nivoi 2, 4, 6, 8, 10, 12). Provereno programski.
*Predlog:* proveravati stanje figure (npr. broj linija, naslov) umesto ispisa, ili zahtevati ispis (`print(len(plt.gca().lines))`).

**N3. Web čet: istorija može da počne porukom modela → verovatna greška od Gemini API‑ja.**
`app.js` šalje `history.slice(-30)`. Istorija se smenjuje user/assistant, a posle dodavanja pitanja ima neparan broj stavki, pa kad ima više od 30 stavki prvi element isečka je odgovor modela. Desktop verzija to rešava (`while msgs[0].role != "user": pop`), web ne. Mislim da API odbija takav razgovor, a greška 400 bi se prikazala kao „Ključ nije ispravan“ (zbunjujuće). *Nisam mogao da testiram na pravom API‑ju.*
*Predlog:* isti `while` ispravak u `app.js`.

**N4. Desktop ne prikazuje grafikone.**
Za `plt.show()` kernel šalje sliku, a `lab.py` ispisuje samo `text/plain` (npr. `<Figure size 1280x960 with 1 Axes>`). Web verzija prikazuje slike. Za sprat 18 to znači da igrač na desktopu ne vidi šta je nacrtao.
*Predlog:* prikazati `image/png` iz `display_data` ili bar objasniti u zadatku.

**N5. Desktop i web strože/blaže porede ispis.**
Web ima `LENIENT_NUMBERS` (`20` = `20.0`), desktop ne. Isto rešenje može da prođe na webu, a na desktopu ne.
*Predlog:* ujednačiti (ili isključiti blagost na webu, ili dodati u `_norm` na desktopu).

**N6. Verzije biblioteka nisu fiksirane.**
Zadaci sprata 20–26 (pandas, scikit‑learn, scipy) i neki kvizovi zavise od tačnog ispisa/ponašanja biblioteka. Testirano sa pandas 3.1.1, scikit‑learn 1.9.1, scipy 1.18.1, numpy 2.5.5. Instaler će instalirati „najnovije“ u trenutku instalacije, a web koristi verzije iz Pyodide 0.27.2 (drugačije). Buduće verzije mogu da promene ispis i „pokvare“ zadatke.
*Predlog:* fiksirati verzije u `requirements.txt` i proveriti zadatke i na Pyodide‑u.

**N7. Naslov „Sta ispisuje ovaj kod?“ na svim kviz pitanjima (desktop).**
28 kviz pitanja nema kod koji se ispisuje (npr. „Cemu sluzi Monte Karlo simulacija?“), a ipak stoji gornji naslov.
*Predlog:* izbaciti naslov ili ga prikazati samo kad pitanje sadrži `print`.

**N8. Zajednički kernel između nivoa.**
Promenljive prelaze iz nivoa u nivo (README to navodi kao funkciju). Posledica: igrač može da „prođe“ zadatak koji samo ispisuje promenljivu koja je ostala od ranije. Namerno ponašanje, ali vredi znati za odbranu.

### Niska

**N9. `make_release.py` i README se ne slažu.**
Skripta upozorava ako nema fascikli `book` i `lessons_html`, a README kaže da knjiga nije u repou ni instaleru. `EXCLUDE_FILES` navodi fajlove koji ne postoje (`make_zip.py`, `convert_lessons.py`, `start.bat`). U instaler se kopira i `docs/` (web verzija) koja tamo nije potrebna.

**N10. Mrtav kod:** `DONE_FLOORS`, `PROGRESS` (`hotel.py`), `self.blink` (postavlja se, nikad ne čita), neiskorišćena promenljiva `extra` u `_paint_plate`, grana `locked` u `LevelsPage` nikad se ne izvrši jer je `UNLOCK_ALL = True`, dva odvojena importa iz `PySide6.QtGui` u `main.py`, `api_key.txt` u `.gitignore` (fajl se nigde ne koristi).

**N11. `main.py` pokreće aplikaciju pri uvozu** (nema `if __name__ == "__main__":`).

**N12. Podaci se pišu pored koda** (`progress.json`, `settings.json`, `chat_history.json`). U `%LOCALAPPDATA%` radi, ali bi pucalo u fascikli bez prava pisanja. `progress.mark` i `ai.save_settings` ne hvataju grešku pri upisu (čitanje je zaštićeno, upis nije).

**N13. Široki `except` blokovi** u `lab._poll`, `ai.load_*`, `ai.save_history` guraju greške „pod tepih“; olakšavaju stabilnost ali otežavaju otklanjanje grešaka.

**N14. Čet se pri svakom delu odgovora iscrtava ceo iznova** (`ChatWidget._on_chunk → render()`): sporo za dugačke razgovore.

**N15. Mešanje jezika i pravopis.** Poruke su i na srpskom i na engleskom; srpski tekst je bez dijakritika (verovatno namerno). Greška u zadatku 10 (nivo 8): „terarni operator“ → „ternarni“.

**N16. Bezbednost / privatnost (informativno).** API ključ je u običnom tekstu (`settings.json`, `localStorage`). Jupyter kernel komunicira preko lokalnog TCP‑a bez enkripcije (upozorenje u konzoli) – samo localhost. Prikaz teksta iz AI odgovora je pravilno „escape“‑ovan (nema HTML ubacivanja).

**N17. Moguća trka u `lab._poll`** (ostatak ispisa posle `idle`): nije primećena u testovima; pominjem jer bi CHECK tada mogao pogrešno da javi „JOS NE“.

**N18. Dupliran kod** između `hotel.py` i `app.js` (crtanje, provera). Svaka izmena pravila mora da se unese na dva mesta.

## 4. Status popravki

Svi nalazi su obrađeni. Posle popravki ponovo su pokrenuti: `verify_tasks.py` (156 zadataka, 121 kviz sa ispisom, `data.js` – sve u redu), desktop test (offscreen) i web test (Chromium).

| Nalaz | Status | Šta je urađeno |
|---|---|---|
| N1 | ✅ popravljeno | Dodat `requirements.txt` sa fiksiranim, testiranim verzijama; `make_release.py` odbija rad bez njega |
| N2 | ✅ popravljeno | Zadaci sprata 18 sada traže ispis stanja grafika (broj linija, naslov, oznake, legenda); starter više ne prolazi sam; `verify_tasks.py` to proverava |
| N3 | ✅ popravljeno | `app.js` izbacuje vodeće poruke modela iz istorije; testirano lažnim odgovorom (poslato 29 poruka, prva je korisnikova) |
| N4 | ✅ popravljeno | Desktop prikazuje `image/png` grafike ispod izlaza (testirano) |
| N5 | ✅ popravljeno | Desktop dobio isto blago poređenje brojeva kao web (`same_output`), prema nameri iz komita „fix output check“ |
| N6 | ⚠ delimično | Verzije fiksirane u `requirements.txt`. Provera sprata 20–26 u Pyodide‑u i dalje nije moguća bez pristupa CDN‑u; testiraj ručno u browseru |
| N7 | ✅ popravljeno | Naslov „Sta ispisuje ovaj kod?“ sakriven kad je pitanje u komentaru (35 pitanja bez `print`, naslov se krije za 34; samo pitanje sa `t[0]=5` ga zadržava) |
| N8 | ➖ bez izmene | Namerno ponašanje (README); ostaje dokumentovano |
| N9 | ✅ popravljeno | `make_release.py` očišćen: nema nepostojećih fajlova, ne kopira `docs/`, `documentation/`, alate |
| N10 | ✅ popravljeno | Uklonjeni `DONE_FLOORS`, `PROGRESS`, `blink`, `extra`, dupli import, `api_key.txt`. Grana `locked` ostaje jer zavisi od `UNLOCK_ALL` |
| N11 | ✅ popravljeno | `if __name__ == "__main__":` u `main.py` |
| N12 | ✅ popravljeno | `progress.mark` i `ai.save_settings` hvataju greške upisa; ACCOUNT prikazuje poruku |
| N13 | ✅ popravljeno | `except Exception` zamenjen užim izuzecima u `ai.py`; `lab._poll` ima jedan jasan blok koji javlja tip greške |
| N14 | ✅ popravljeno | Iscrtavanje četa ograničeno na jednom u 80 ms (200 delića → 1 iscrtavanje) |
| N15 | ⚠ delimično | Ispravljeno „terarni“ → „ternarni“. Mešanje srpskog i engleskog ostaje (odluka autora) |
| N16 | ➖ bez izmene | Informativno |
| N17 | ➖ nije greška | Jupyter šalje izlaz i `idle` kroz isti iopub kanal, redosled je zagarantovan; trka nije moguća na tom putu |
| N18 | ⚠ delimično | Duplirana logika desktop/web je neizbežna; dodat `verify_tasks.py` koji čuva podatke usklađenim |

### Kako ponovo proveriti
```bash
pip install -r requirements.txt
python verify_tasks.py
```

