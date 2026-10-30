# PyHotel - beleške

## Odluke
- Knjiga i Moodle slajdovi NISU u repou radi zaštite autorskih prava (javni repo, sprečavanje krađe materijala).
- Otključani svi spratovi (`UNLOCK_ALL = True`): Namerna odluka jer je za 100% i konfete i dalje potrebno proći sve spratove.

## Pregled projekta i strukture
Python Hotel je edukativna desktop igrica za učenje Python-a (PySide6) sa 26 spratova/lekcija:
- Svaki sprat ima 12 nivoa (kombinacija kvizova i zadataka u Code Lab-u).
- Pokriva teme od osnova programiranja, preko NumPy, Pandas, Matplotlib i SciPy biblioteka, do mašinskog učenja.
- Sadrži ugrađeni Jupyter kernel za izvršavanje koda, Moodle prezentacije/knjigu i AI tutora ("Monty Python").

## Problemi i plan za fiksiranje (Bugs & Fixes)

1. **Stroga provera tipova u Code Lab-u (`play.py`)**
   - **Problem:** Funkcija `_norm` uklanja samo prazne prostore na kraju linija, pa je provera izlaza strogo tekstualna. Ako zadatak vrati ceo broj `20`, a očekuje se float `20.0` (ili obrnuto), provera prijavljuje grešku iako je rezultat tačan.
   - **Rešenje:** U metodi za proveru u `TaskLab` klasi potrebno je unaprediti normalizaciju izlaza. Implementirati pomoćnu funkciju koja pre poređenja pokušava da konvertuje tekstualne brojeve u `float`. Na taj način se izbegava razlika između `20` i `20.0`, dok se netekstualni izlazi i dalje porede u standardnom formatu.

2. **Rizik kod Markdown parsiranja i strimovanja AI odgovora (`ai.py`)**
   - **Problem:** Uslov `text.count("```") % 2` u funkciji `fmt` proverava parnost trostrukih navodnika kako bi automatski zatvorio blok tokom strimovanja odgovora od Gemini modela. Ako model pošalje neparan broj navodnika u običnom tekstu, ceo preostali deo poruke se pogrešno prikazuje kao kodni blok.
   - **Rešenje:** Izmeniti logiku u `fmt` tako da se izbegne prosto prebrojavanje navodnika u celom stringu. Umesto toga, primeniti parsiranje koje identifikuje isključivo linije koje počinju sa ```` ``` ```` za otvaranje i zatvaranje bloka koda, čime se sprečava prelivanje stila na običan tekst u slučaju greške u strimovanju.

## Sledeće
1. Bug fixes (ispravka tipova u Code Lab-u i Markdown parsera)
2. Web aplikacija preko GitHub Pages