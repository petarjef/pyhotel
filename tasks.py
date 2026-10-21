"""Zadaci za spratove hotela.

Svaki sprat ima 12 nivoa:
  neparni nivoi (1, 3, 5, ...)  -> pitanja sa 4 ponudjena odgovora (QUIZ)
  parni nivoi   (2, 4, 6, ...)  -> pisanje koda koji ispisuje trazeni output (CODE)

QUIZ[sprat] = lista od 6: (kod, [4 odgovora], index tacnog)
CODE[sprat] = lista od 6: (tekst zadatka, ocekivani output, pocetni kod, primer resenja)
"""

S = ""

QUIZ = {
    # ---- 1. Osnove programiranja ----
    1: [
        ('print("Hello")', ["Hello", '"Hello"', "print Hello", "Greska"], 0),
        ("x = 5\ny = 3\nprint(x + y)", ["8", "53", "x + y", "Greska"], 0),
        ('# print("A")\nprint("B")', ["A", "B", "A\nB", "Nista"], 1),
        ("a = 2\na = a + 3\nprint(a)", ["2", "3", "5", "23"], 2),
        ("print(10 / 4)", ["2", "2.5", "2.0", "3"], 1),
        ('print("5" + "5")', ["10", "55", "Greska", "5 5"], 1),
    ],
    # ---- 2. Pajton okruzenje ----
    2: [
        ('print("a", "b")', ["a b", "ab", "a,b", '"a" "b"'], 0),
        ('print("a", "b", sep="-")', ["a-b", "a - b", "a b -", "ab-"], 0),
        ('print("Hi", end="!")\nprint("Bye")', ["Hi!Bye", "Hi!\nBye", "Hi Bye!", "Hi!Bye!"], 0),
        ('print("Line1\\nLine2")', ["Line1\\nLine2", "Line1\nLine2", "Line1 Line2", "Greska"], 1),
        ('print("Hi"', ["SyntaxError", "Hi", 'Hi"', "Nista"], 0),
        ('print("Python", 3)', ["Python 3", "Python3", '"Python" 3', "Greska"], 0),
    ],
    # ---- 3. Osnovni elementi jezika ----
    3: [
        ("print(type(3.0))", ["<class 'float'>", "<class 'int'>", "float", "3.0"], 0),
        ("print(7 // 2)", ["3.5", "3", "4", "1"], 1),
        ("print(7 % 2)", ["3", "1", "0", "3.5"], 1),
        ("print(2 ** 5)", ["10", "25", "32", "7"], 2),
        ('print(int("12") + 3)', ["123", "15", "Greska", "12 3"], 1),
        ("print(int(7.9))", ["8", "7.9", "7", "Greska"], 2),
    ],
    # ---- 4. Logicke promenljive ----
    4: [
        ("print(5 > 3)", ["True", "False", "5", "Greska"], 0),
        ("print(10 == 10.0)", ["False", "True", "Greska", "10"], 1),
        ("print(True and False)", ["True", "False", "None", "Greska"], 1),
        ("print(not (3 < 2))", ["False", "True", "3", "Greska"], 1),
        ("print(bool(0))", ["True", "False", "0", "Greska"], 1),
        ("print(int(True) + int(True))", ["1", "True", "2", "TrueTrue"], 2),
    ],
    # ---- 5. Stringovi ----
    5: [
        ('s = "Python"\nprint(s[0])', ["P", "y", "Python", "n"], 0),
        ('print("Python"[-1])', ["P", "n", "o", "Greska"], 1),
        ('print("Python"[1:4])', ["Pyt", "yth", "ytho", "Pyth"], 1),
        ('print(len("hello"))', ["4", "5", "6", "hello"], 1),
        ('print("ab" * 3)', ["ab3", "ababab", "ab ab ab", "Greska"], 1),
        ('print("Hello".upper())', ["Hello", "hello", "HELLO", "Greska"], 2),
    ],
    # ---- 6. Liste ----
    6: [
        ("a = [1, 2, 3]\nprint(a[1])", ["1", "2", "3", "[2]"], 1),
        ("a = [1, 2, 3]\na.append(4)\nprint(a)", ["[1, 2, 3, 4]", "[4, 1, 2, 3]", "[1, 2, 3]", "None"], 0),
        ("print(len([5, 6, 7, 8]))", ["3", "4", "8", "26"], 1),
        ("a = [10, 20, 30]\nprint(a[-1])", ["10", "20", "30", "-1"], 2),
        ("a = [3, 1, 2]\na.sort()\nprint(a)", ["[3, 1, 2]", "[1, 2, 3]", "[3, 2, 1]", "None"], 1),
        ("a = [1, 2, 3, 4, 5]\nprint(a[1:3])", ["[1, 2, 3]", "[2, 3]", "[2, 3, 4]", "[1, 2]"], 1),
    ],
    # ---- 7. Jos o stringovima i listama ----
    7: [
        ('print("a,b,c".split(","))', ["['a', 'b', 'c']", "a b c", "['a,b,c']", "a,b,c"], 0),
        ('print("-".join(["x", "y", "z"]))', ["xyz", "x-y-z", "-x-y-z-", "['x-y-z']"], 1),
        ('print("[" + "  hi  ".strip() + "]")', ["[hi]", "[  hi  ]", "[ hi ]", "hi"], 0),
        ("a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)", ["[1, 2, 3]", "[1, 2, 3, 4]", "[4]", "Greska"], 1),
        ("a = [1, 2, 3]\nb = a.copy()\nb.append(4)\nprint(a)", ["[1, 2, 3, 4]", "[1, 2, 3]", "[4]", "Greska"], 1),
        ('print("banana".count("a"))', ["1", "2", "3", "6"], 2),
    ],
    # ---- 8. Moduli ----
    8: [
        ("import math\nprint(math.sqrt(16))", ["4", "4.0", "16", "Greska"], 1),
        ("import math\nprint(math.floor(3.9))", ["4", "3", "3.9", "3.0"], 1),
        ("import math\nprint(math.ceil(3.1))", ["3", "4", "3.1", "4.0"], 1),
        ("from math import factorial\nprint(factorial(5))", ["25", "120", "15", "5"], 1),
        ("import math as m\nprint(m.pi > 3)", ["3", "True", "False", "Greska"], 1),
        ("import math\nprint(round(math.pi, 2))", ["3.1", "3.14", "3.15", "3.142"], 1),
    ],
        # ---- 9. Torke, skupovi i recnici ----
    9: [
        ("t = (1, 2, 3)\nt[0] = 5", ["(5, 2, 3)", "Greska (TypeError)", "[5, 2, 3]", "None"], 1),
        ("s = {1, 2, 2, 3}\nprint(len(s))", ["4", "3", "2", "Greska"], 1),
        ("d = {'a': 1, 'b': 2}\nprint(d.get('c', 0))", ["None", "0", "Greska (KeyError)", "'c'"], 1),
        ("print(set([1, 2]) == set([2, 1]))", ["False", "True", "Greska", "None"], 1),
        ("d = {'x': 10}\nd['y'] = 20\nprint(d)", ["{'x': 10}", "{'x': 10, 'y': 20}", "Greska", "{'y': 20}"], 1),
        ("a = (1, [2, 3])\na[1].append(4)\nprint(a)", ["Greska", "(1, [2, 3, 4])", "(1, [2, 3])", "(1, [4])"], 1),
    ],
    # ---- 10. Naredbe grananja ----
    10: [
        ("x = 5\nif x > 3:\n    print('A')\nelse:\n    print('B')", ["A", "B", "A\\nB", "Greska"], 0),
        ("x = 10\nif x < 5:\n    print('Malo')\nelif x < 15:\n    print('Srednje')\nelse:\n    print('Veliko')", ["Malo", "Srednje", "Veliko", "Greska"], 1),
        ("print(10 if 5 > 3 else 20)", ["10", "20", "True", "Greska"], 0),
        ("x = 0\nif x:\n    print('Da')\nelse:\n    print('Ne')", ["Da", "Ne", "0", "Greska"], 1),
        ("a = 5\nb = 10\nif a > 3 and b < 15:\n    print('OK')", ["OK", "Nista", "Greska", "False"], 0),
        ("x = 5\nif x > 10:\n    print('A')\nif x > 3:\n    print('B')", ["A", "B", "A\\nB", "Greska"], 1),
    ],
    # ---- 11. Petlje ----
    11: [
        ("for i in range(3):\n    print(i, end=' ')", ["0 1 2 ", "1 2 3 ", "0 1 2 3 ", "Greska"], 0),
        ("i = 0\nwhile i < 3:\n    i += 1\nprint(i)", ["0", "2", "3", "Greska (beskonacna)"], 2),
        ("for i in range(2, 6, 2):\n    print(i, end=' ')", ["2 3 4 5 ", "2 4 ", "2 4 6 ", "Greska"], 1),
        ("for i in range(3):\n    pass\nelse:\n    print('Kraj')", ["Kraj", "Nista", "Greska", "0 1 2"], 0),
        ("x = [1, 2, 3]\nfor i in x:\n    if i == 2:\n        break\n    print(i)", ["1", "1\\n2", "1\\n2\\n3", "Greska"], 0),
        ("for i in range(3):\n    if i == 1:\n        continue\n    print(i)", ["0\\n1\\n2", "0\\n2", "1", "Greska"], 1),
    ],
    # ---- 12. Funkcije ----
    12: [
        ("def f(x):\n    return x * 2\nprint(f(5))", ["5", "10", "25", "Greska"], 1),
        ("def f(x, y=2):\n    return x + y\nprint(f(3))", ["3", "5", "Greska", "32"], 1),
        ("def f():\n    pass\nprint(f())", ["None", "Nista", "Greska", "0"], 0),
        ("x = 10\ndef f():\n    x = 5\nf()\nprint(x)", ["5", "10", "Greska", "None"], 1),
        ("def f(*args):\n    return len(args)\nprint(f(1, 2, 3))", ["1", "3", "6", "Greska"], 1),
        ("def f(a, b):\n    return a - b\nprint(f(b=2, a=5))", ["3", "-3", "7", "Greska"], 0),
    ],
    # ---- 13. Rad sa datotekama ----
    13: [
        ("# Ako fajl 'a.txt' ne postoji, sta radi open('a.txt', 'r')?", ["Pravi novi fajl", "Baca FileNotFoundError", "Vraca None", "Vraca prazan string"], 1),
        ("# Koji mod otvara fajl za pisanje i brise prethodni sadrzaj?", ["'r'", "'a'", "'w'", "'x'"], 2),
        ("with open('a.txt', 'w') as f:\n    f.write('Hi')\n# Da li se fajl automatski zatvara?", ["Da", "Ne", "Samo na Windowsu", "Greska"], 0),
        ("# Koji metod cita sve linije fajla u listu stringova?", ["read()", "readline()", "readlines()", "readall()"], 2),
        ("with open('a.txt', 'w') as f:\n    f.write('A\\nB')\nwith open('a.txt') as f:\n    print(len(f.readlines()))", ["1", "2", "3", "Greska"], 1),
        ("# Sta radi mod 'a'?", ["Cita fajl", "Pise na pocetak", "Dodaje na kraj", "Brise fajl"], 2),
    ],
        # ---- 14. Upravljanje greskama ----
    14: [
        ("try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Greska')", ["Greska", "0", "1", "None"], 0),
        ("try:\n    int('abc')\nexcept ValueError:\n    print('Lose')\nexcept Exception:\n    print('Sve')", ["Lose", "Sve", "Greska", "Nista"], 0),
        ("try:\n    print('A')\nfinally:\n    print('B')", ["A", "B", "A\\nB", "Greska"], 2),
        ("# Koji blok se izvrsava bez obzira na to da li je doslo do greske?", ["try", "except", "else", "finally"], 3),
        ("try:\n    raise ValueError('Greska')\nexcept ValueError as e:\n    print(type(e).__name__)", ["ValueError", "Greska", "Exception", "Greska('Greska')"], 0),
        ("def f():\n    try:\n        return 1\n    finally:\n        print('Kraj')\nprint(f())", ["1\\nKraj", "Kraj\\n1", "1", "Kraj"], 1),
    ],
    # ---- 15. Klase ----
    15: [
        ("class A:\n    pass\na = A()\nprint(type(a).__name__)", ["A", "<class 'A'>", "object", "Greska"], 0),
        ("class A:\n    x = 5\n    def f(self):\n        return self.x\na = A()\nprint(a.f())", ["5", "A", "Greska", "None"], 0),
        ("class A:\n    def __init__(self, v):\n        self.v = v\na = A(10)\nprint(a.v)", ["10", "v", "Greska", "None"], 0),
        ("class A:\n    def __init__(self):\n        self.x = 1\na = A()\na.x = 2\nb = A()\nprint(b.x)", ["1", "2", "Greska", "None"], 0),
        ("class A:\n    def __str__(self):\n        return 'Ja sam A'\nprint(A())", ["Ja sam A", "<__main__.A object>", "A", "Greska"], 0),
        ("class A:\n    def f(self):\n        return 1\nclass B(A):\n    def f(self):\n        return 2\nprint(B().f())", ["1", "2", "Greska", "None"], 1),
    ],
    # ---- 16. Regularni izrazi ----
    16: [
        ("import re\nprint(re.findall(r'\\d+', 'a1b22c333'))", ["['1', '2', '3']", "['1', '22', '333']", "['123']", "Greska"], 1),
        ("import re\nprint(bool(re.match(r'a', 'abc')))", ["True", "False", "None", "Greska"], 0),
        ("import re\nprint(re.sub(r'\\s', '-', 'a b c'))", ["a-b-c", "a b c", "a--b--c", "abc"], 0),
        ("import re\nprint(re.search(r'\\d', 'abc123').group())", ["1", "123", "a", "None"], 0),
        ("# Sta znaci r'^\\w+$'?", ["Pocinje slovom", "Samо slova i brojevi", "Bilo koji karakter", "Prazan string"], 1),
        ("import re\nprint(len(re.findall(r'[aeiou]', 'programiranje')))", ["4", "5", "6", "7"], 1),
    ],
    # ---- 17. Uvod u NumPy ----
    17: [
        ("import numpy as np\na = np.array([1, 2, 3])\nprint(a * 2)", ["[2, 4, 6]", "Greska", "[1, 2, 3, 1, 2, 3]", "[2 4 6]"], 3),
        ("import numpy as np\nprint(np.zeros(3))", ["[0, 0, 0]", "[0. 0. 0.]", "Greska", "[0 0 0]"], 1),
        ("import numpy as np\na = np.array([1, 2, 3])\nprint(a.shape)", ["(3,)", "[3]", "3", "Greska"], 0),
        ("import numpy as np\na = np.array([[1, 2], [3, 4]])\nprint(a.shape)", ["(2, 2)", "(4,)", "2", "Greska"], 0),
        ("import numpy as np\na = np.arange(3)\nprint(a)", ["[0 1 2]", "[1 2 3]", "[0, 1, 2]", "Greska"], 0),
        ("import numpy as np\na = np.array([1, 2, 3])\nprint(a.mean())", ["2.0", "2", "6", "Greska"], 0),
    ],
    # ---- 18. Matplotlib ----
    18: [
        ("import matplotlib.pyplot as plt\n# Koja funkcija crta linijski grafik?", ["plt.plot()", "plt.line()", "plt.draw()", "plt.show()"], 0),
        ("import matplotlib.pyplot as plt\n# Koja funkcija prikazuje grafik na ekranu?", ["plt.show()", "plt.display()", "plt.render()", "plt.plot()"], 0),
        ("import matplotlib.pyplot as plt\n# Koja funkcija pravi grafik sa tackama (scatter)?", ["plt.scatter()", "plt.dots()", "plt.points()", "plt.plot()"], 0),
        ("import matplotlib.pyplot as plt\n# Cemu sluzi plt.xlabel()?", ["Naslov grafika", "Oznaka x-ose", "Oznaka y-ose", "Legenda"], 1),
        ("import matplotlib.pyplot as plt\nplt.plot([1, 2], [3, 4])\n# Koliko tacaka ce biti nacrtano?", ["1", "2", "3", "4"], 1),
        ("import matplotlib.pyplot as plt\n# Kako se cuva grafik u fajl?", ["plt.save()", "plt.savefig()", "plt.export()", "plt.write()"], 1),
    ],
        # ---- 19. Monte Karlo simulacije ----
    19: [
        ("# Cemu sluzi Monte Karlo simulacija?", ["Tacnom izracunavanju", "Modeliranju neizvesnosti", "Sortiranju podataka", "Pravljenju grafikona"], 1),
        ("import random\nrandom.seed(42)\nprint(random.random() == random.random())", ["True", "False", "Greska", "None"], 1),
        ("import random\n# Koja funkcija vraca ceo broj izmedju 1 i 6 (ukljucujuci)?", ["random.random(1, 6)", "random.randint(1, 6)", "random.choice(6)", "random.uniform(1, 6)"], 1),
        ("# Ako simulaciju pokrenemo vise puta (npr. 10000), sta se desava sa rezultatom?", ["Postaje tacniji", "Postaje netacniji", "Ostaje isti", "Baca gresku"], 0),
        ("import random\nprint(random.choice([1, 2, 3]) in [1, 2, 3])", ["True", "False", "None", "Greska"], 0),
        ("# Koji zakon kaze da se prosekom mnogo simulacija priblizavamo ocekivanoj vrednosti?", ["Zakon velikih brojeva", "Pitagorina teorema", "Zakon verovatnoce", "Njutnov zakon"], 0),
    ],
    # ---- 20. Pandas ----
    20: [
        ("import pandas as pd\ndf = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})\nprint(df.shape)", ["(2, 2)", "(4,)", "2", "Greska"], 0),
        ("import pandas as pd\ns = pd.Series([10, 20, 30])\nprint(s.mean())", ["10", "20.0", "60", "Greska"], 1),
        ("import pandas as pd\ndf = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})\nprint(df['x'].sum())", ["6", "15", "3", "Greska"], 0),
        ("import pandas as pd\ndf = pd.DataFrame({'A': [1, 2, 3]})\nprint(df[df['A'] > 1])", ["Redove gde je A=2 i A=3", "Samo A=1", "Greska", "None"], 0),
        ("# Koja metoda daje brz pregled prvih 5 redova?", ["df.head()", "df.top()", "df.first()", "df.preview()"], 0),
        ("import pandas as pd\ndf = pd.DataFrame({'A': [1, None, 3]})\nprint(df.isnull().sum().sum())", ["0", "1", "2", "3"], 1),
    ],
    # ---- 21. Optimizacija: SciPy ----
    21: [
        ("from scipy.optimize import minimize\n# Cemu sluzi minimize()?", ["Trazenju minimuma funkcije", "Maksimizaciji", "Sortiranju", "Integraciji"], 0),
        ("from scipy.optimize import minimize\n# Sta je 'x0' u minimize()?", ["Pocetna tacka", "Rezultat", "Funkcija", "Greska"], 0),
        ("from scipy.optimize import minimize\nres = minimize(lambda x: (x-3)**2, x0=0)\nprint(round(res.x[0]))", ["0", "3", "-3", "9"], 1),
        ("from scipy.optimize import minimize\n# Sta vraca uspesna minimize() funkcija?", ["Samo broj", "Objekat sa atributima x i fun", "Listu", "Nista"], 1),
        ("from scipy.optimize import minimize\nres = minimize(lambda x: x**2, x0=10)\nprint(res.success)", ["True", "False", "10", "Greska"], 0),
        ("# Zasto je SciPy koristan u poslovnom odlucivanju?", ["Za optimizaciju resursa", "Za crtanje", "Za baze podataka", "Za igrice"], 0),
    ],
    # ---- 22. Masinsko ucenje: Uvod ----
    22: [
        ("# Sta je masinsko ucenje?", ["Rucno pisanje pravila", "Ucenje iz podataka", "Baza podataka", "Vrsta programa"], 1),
        ("# Sta je 'feature' u masinskom ucenju?", ["Ciljna promenljiva", "Ulazna promenljiva", "Greska modela", "Algoritam"], 1),
        ("# Nadgledano ucenje zahteva:", ["Samo ulazne podatke", "Ulazne i izlazne podatke", "Samo izlazne podatke", "Nista"], 1),
        ("# Sta radimo u fazi 'treniranja' modela?", ["Cuvamo model", "Podesavamo parametre", "Brisemo podatke", "Crtamo grafike"], 1),
        ("# Sta je klasifikacija?", ["Predvidjanje broja", "Predvidjanje kategorije", "Grupisanje", "Ciscenje podataka"], 1),
        ("# Zasto delimo podatke na trening i test skup?", ["Da bude brze", "Da proverimo generalizaciju", "Da smanjimo podatke", "Da bude lepse"], 1),
    ],
        # ---- 23. Naivni Bajesovi klasifikatori ----
    23: [
        ("# Zasto se zove 'naivni' Bajes?", ["Zato sto je algoritam glup", "Zato sto pretpostavlja nezavisnost atributa", "Zato sto ne radi sa brojevima", "Zato sto je brz"], 1),
        ("# Koja je osnovna teorema na kojoj se zasniva?", ["Pitagorina", "Bajesova teorema", "Njutnova", "Bolcmanova"], 1),
        ("from sklearn.naive_bayes import GaussianNB\n# Za koje tipove podataka se koristi GaussianNB?", ["Tekstualne", "Kontinualne (brojeve)", "Kategoricke", "Slike"], 1),
        ("# U cemu je prednost Naivnog Bajesa?", ["Najtacniji je uvek", "Veoma je brz i dobar za velike skupove", "Ne zahteva podatke", "Radi samo sa slikama"], 1),
        ("# Ako se u test skupu pojavi rec koja nije vidjena u treningu, kako Naivni Bajes to resi?", ["Puca sa greskom", "Ignorise rec", "Koristi Laplasovo izglađivanje", "Odbacuje ceo red"], 2),
        ("from sklearn.naive_bayes import GaussianNB\nclf = GaussianNB()\n# Sta radi metoda fit()?", ["Predvidja", "Trenira model na podacima", "Cisti podatke", "Crtа grafik"], 1),
    ],
    # ---- 24. K najblizih suseda ----
    24: [
        ("# Kako KNN donosi odluku o klasi novog podatka?", ["Gleda najblize susede", "Gleda sve podatke", "Koristi verovatnocu", "Gleda samo jedan podatak"], 0),
        ("# Sta znaci 'K' u KNN?", ["Broj atributa", "Broj suseda", "Broj klasa", "Broj iteracija"], 1),
        ("# Zasto je skaliranje podataka (npr. StandardScaler) obavezno kod KNN?", ["Da bi algoritam bio brzi", "Zato sto racuna razdaljinu, a veliki brojevi dominiraju", "Da bi bio lepsi grafik", "Ne treba skalirati"], 1),
        ("# Ako je K=1, kakav model dobijamo?", ["Veoma gladak", "Sklon overfittingu (preprilagodjavanju)", "Sklon underfittingu", "Nista"], 1),
        ("from sklearn.neighbors import KNeighborsClassifier\nclf = KNeighborsClassifier(n_neighbors=3)\n# Sta radi metoda predict()?", ["Trenira model", "Vraca predvidjene klase za nove podatke", "Ispisuje tacnost", "Brіse model"], 1),
        ("# KNN spada u koju vrstu ucenja?", ["Nadgledano", "Nenadgledano", "Potkrepljujuce", "Polunadgledano"], 0),
    ],
    # ---- 25. Stabla odlucivanja ----
    25: [
        ("# Sta je cvor (node) u stablu odlucivanja?", ["Mesto gde se donosi odluka", "Krajnji rezultat", "Grana", "Podatak"], 0),
        ("# Koja metrika se cesto koristi za podelu u stablu?", ["Euklidska distanca", "Dzinijev indeks ili informaciona dobit", "Kosinusna slicnost", "Bajes"], 1),
        ("# Ako stablo raste bez ogranicenja, sta se moze desiti?", ["Bice veoma precizno na treningu, a lose na testu (overfitting)", "Bice beskorisno", "Nece raditi", "Nista"], 0),
        ("# Kako se zove tehnika kresanja stabla da se spreči overfitting?", ["Boosting", "Pruning (kresanje)", "Bagging", "Scaling"], 1),
        ("# Stabla odlucivanja su dobra jer su:", ["Lako interpretabilna (razumljiva coveku)", "Uvek najtacnija", "Ne zahtevaju podatke", "Veoma spora"], 0),
        ("from sklearn.tree import DecisionTreeClassifier\n# Kako se zove parametar koji ogranicava dubinu stabla?", ["max_depth", "max_leafs", "depth", "tree_size"], 0),
    ],
    # ---- 26. Ansambl metode ----
    26: [
        ("# Sta je ansambl u masinskom ucenju?", ["Jedan veoma veliki model", "Kombinacija vise modela radi boljeg rezultata", "Skup podataka", "Vrsta greske"], 1),
        ("# Random Forest je ansambl:", ["Linearnih regresija", "Stabla odlucivanja", "KNN modela", "Naivnih Bajesa"], 1),
        ("# Kako radi Bagging (npr. Random Forest)?", ["Trenira modele paralelno na slucajnim podskupovima", "Trenira modele redom na greskama", "Ne trenira uopste", "Koristi samo jedan model"], 0),
        ("# Kako radi Boosting (npr. Gradient Boosting)?", ["Trenira modele paralelno", "Trenira modele redom, ispravljajuci greske prethodnih", "Brise lose modele", "Koristi samo jedan model"], 1),
        ("# Zasto su ansambl metode popularne u praksi?", ["Zato sto su jednostavne", "Zato sto daju visoku tacnost i robustne su", "Zato sto ne zahtevaju podatke", "Zato sto su spore"], 1),
        ("from sklearn.ensemble import RandomForestClassifier\n# Sta radi metoda predict_proba()?", ["Vraca tacnost", "Vraca verovatnoce za svaku klasu", "Trenira model", "Cisti podatke"], 1),
    ],
}

CODE = {
    1: [
        ("Ispisi tekst: Hello, world!", "Hello, world!", S, 'print("Hello, world!")'),
        ("Ispisi rezultat izraza 12 + 30.", "42", S, "print(12 + 30)"),
        ('Napravi promenljivu ime sa vrednoscu "Ana" i ispisi je.', "Ana", S + "ime = ", 'ime = "Ana"\nprint(ime)'),
        ("Ispisi dva reda: Python, pa u drugom redu rocks (dva poziva print).", "Python\nrocks", S, 'print("Python")\nprint("rocks")'),
        ("Promenljive a = 6 i b = 9 su vec napravljene. Ispisi njihov proizvod.", "54", "a = 6\nb = 9\n", "a = 6\nb = 9\nprint(a * b)"),
        ("Ispisi prosek brojeva 4, 8 i 12 (koristi deljenje).", "8.0", S, "print((4 + 8 + 12) / 3)"),
    ],
    2: [
        ("Ispisi tekst: Ja ucim Python", "Ja ucim Python", S, 'print("Ja ucim Python")'),
        ("Jednim pozivom print ispisi brojeve 1 2 3 odvojene razmakom (tri argumenta).", "1 2 3", S, "print(1, 2, 3)"),
        ("Ispisi A-B-C koristeci parametar sep.", "A-B-C", S, 'print("A", "B", "C", sep="-")'),
        ("Ispisi Hello World u jednom redu pomocu dva poziva print (koristi end).", "Hello World", S, 'print("Hello", end=" ")\nprint("World")'),
        ("Jednim pozivom print ispisi dva reda: Red, pa Blue (koristi \\n).", "Red\nBlue", S, 'print("Red\\nBlue")'),
        ('Ispisi tekst sa navodnicima: "Ana"', '"Ana"', S, "print('\"Ana\"')"),
    ],
    3: [
        ("Ispisi ostatak pri deljenju 17 sa 5.", "2", S, "print(17 % 5)"),
        ("Ispisi 3 na cetvrti stepen.", "81", S, "print(3 ** 4)"),
        ("Ispisi celobrojni kolicnik brojeva 25 i 4.", "6", S, "print(25 // 4)"),
        ("Napravi promenljivu price = 19.99 i ispisi njen tip.", "<class 'float'>", S, "price = 19.99\nprint(type(price))"),
        ('Pretvori string "250" u broj i ispisi njegovu dvostruku vrednost.', "500", S, 'print(int("250") * 2)'),
        ("Ispisi rezultat izraza (8 + 2) * 5 - 3.", "47", S, "print((8 + 2) * 5 - 3)"),
    ],
    4: [
        ("Ispisi da li je 7 vece od 9.", "False", S, "print(7 > 9)"),
        ("Ispisi True ako je 15 deljivo sa 3 (koristi %).", "True", S, "print(15 % 3 == 0)"),
        ("Neka je x = 5. Ispisi da li je x vece od 1 i manje od 10.", "True", "x = 5\n", "x = 5\nprint(x > 1 and x < 10)"),
        ("U jednom redu ispisi bool(0) i bool(7), odvojene razmakom.", "False True", S, "print(bool(0), bool(7))"),
        ("Ispisi rezultat izraza not True.", "False", S, "print(not True)"),
        ('Ispisi da li su "a" i "b" razliciti (koristi !=).', "True", S, 'print("a" != "b")'),
    ],
    5: [
        ('Ispisi prvo slovo reci "Beograd".', "B", S, 'print("Beograd"[0])'),
        ('Ispisi poslednje slovo reci "Beograd".', "d", S, 'print("Beograd"[-1])'),
        ('Ispisi "banana" velikim slovima.', "BANANA", S, 'print("banana".upper())'),
        ('Ispisi rec "hello" ponovljenu 3 puta, bez razmaka.', "hellohellohello", S, 'print("hello" * 3)'),
        ("Promenljive name i age su vec napravljene. Pomocu f-stringa ispisi: Ana ima 20 godina", "Ana ima 20 godina",
         'name = "Ana"\nage = 20\n', 'name = "Ana"\nage = 20\nprint(f"{name} ima {age} godina")'),
        ('Ispisi duzinu reci "programiranje".', "13", S, 'print(len("programiranje"))'),
    ],
    6: [
        ("Ispisi listu [4, 8, 15].", "[4, 8, 15]", S, "print([4, 8, 15])"),
        ("Lista a = [1, 2, 3] je napravljena. Dodaj joj broj 10 i ispisi listu.", "[1, 2, 3, 10]",
         "a = [1, 2, 3]\n", "a = [1, 2, 3]\na.append(10)\nprint(a)"),
        ("Ispisi zbir elemenata liste [5, 10, 15, 20].", "50", S, "print(sum([5, 10, 15, 20]))"),
        ("Ispisi najveci broj u listi [3, 9, 2, 7].", "9", S, "print(max([3, 9, 2, 7]))"),
        ("Ispisi listu [5, 2, 9, 1] sortiranu rastuce.", "[1, 2, 5, 9]",
         "a = [5, 2, 9, 1]\n", "a = [5, 2, 9, 1]\na.sort()\nprint(a)"),
        ("Ispisi poslednji element liste [10, 20, 30, 40].", "40", S, "print([10, 20, 30, 40][-1])"),
    ],
    7: [
        ('Razdvoji "jabuka,kruska,sljiva" po zarezu i ispisi dobijenu listu.', "['jabuka', 'kruska', 'sljiva']",
         S, 'print("jabuka,kruska,sljiva".split(","))'),
        ('Spoji listu ["a", "b", "c"] razmakom i ispisi rezultat.', "a b c", S, 'print(" ".join(["a", "b", "c"]))'),
        ('Ispisi "  Beograd  " bez razmaka sa strana (koristi strip).', "Beograd", S, 'print("  Beograd  ".strip())'),
        ("Lista m = [[1, 2], [3, 4]] je napravljena. Ispisi broj 4.", "4",
         "m = [[1, 2], [3, 4]]\n", "m = [[1, 2], [3, 4]]\nprint(m[1][1])"),
        ('Ispisi rec "programiranje" unazad (isecanjem).', "ejnarimargorp", S, 'print("programiranje"[::-1])'),
        ("Iz liste [1, 2, 3, 4, 5, 6] ispisi svaki drugi element (isecanje sa korakom).", "[1, 3, 5]",
         "a = [1, 2, 3, 4, 5, 6]\n", "a = [1, 2, 3, 4, 5, 6]\nprint(a[::2])"),
    ],
    8: [
        ("Uvezi math i ispisi kvadratni koren iz 81.", "9.0", S, "import math\nprint(math.sqrt(81))"),
        ("Ispisi 7.8 zaokruzeno nadole pomocu math.floor.", "7", S, "import math\nprint(math.floor(7.8))"),
        ("Ispisi 6! (faktorijel) pomocu modula math.", "720", S, "import math\nprint(math.factorial(6))"),
        ("Ispisi na koliko nacina se mogu izabrati 2 stvari od 5 (math.comb).", "10", S, "import math\nprint(math.comb(5, 2))"),
        ("Ispisi broj pi iz modula math zaokruzen na 3 decimale.", "3.142", S, "import math\nprint(round(math.pi, 3))"),
        ("Uvezi math pod imenom m i ispisi m.ceil(4.2).", "5", S, "import math as m\nprint(m.ceil(4.2))"),
    ],
        9: [
        ("Napravi torku sa brojevima 5, 10, 15 i ispisi njen drugi element.", "10", S, "t = (5, 10, 15)\nprint(t[1])"),
        ("Data je lista a = [1, 2, 2, 3, 4, 4, 4]. Pretvori je u skup i ispisi duzinu tog skupa.", "4", "a = [1, 2, 2, 3, 4, 4, 4]\n", "a = [1, 2, 2, 3, 4, 4, 4]\nprint(len(set(a)))"),
        ("Recnik d = {'ime': 'Ana', 'godine': 20} je napravljen. Ispisi vrednost za kljuc 'godine'.", "20", "d = {'ime': 'Ana', 'godine': 20}\n", "d = {'ime': 'Ana', 'godine': 20}\nprint(d['godine'])"),
        ("Napravi dva skupa a = {1, 2, 3} i b = {3, 4, 5}. Ispisi njihov presek (zajednicke elemente).", "{3}", "a = {1, 2, 3}\nb = {3, 4, 5}\n", "a = {1, 2, 3}\nb = {3, 4, 5}\nprint(a & b)"),
        ("Data su dva recnika: d1 = {'a': 1} i d2 = {'b': 2}. Spoji ih u jedan i ispisi.", "{'a': 1, 'b': 2}", "d1 = {'a': 1}\nd2 = {'b': 2}\n", "d1 = {'a': 1}\nd2 = {'b': 2}\nd1.update(d2)\nprint(d1)"),
        ("Data je lista reci ['ja', 'ucim', 'pajton']. Koristi skup da ispises sve jedinstvene duzine tih reci sortirane rastuce.", "[2, 5, 6]", "reci = ['ja', 'ucim', 'pajton']\n", "reci = ['ja', 'ucim', 'pajton']\nprint(sorted(set(len(r) for r in reci)))"),
    ],
    10: [
        ("Neka je broj = 7. Ako je broj paran ispisi 'Parno', inace ispisi 'Neparno'.", "Neparno", "broj = 7\n", "broj = 7\nif broj % 2 == 0:\n    print('Parno')\nelse:\n    print('Neparno')"),
        ("Data su dva broja a = 15 i b = 20. Ispisi veci od njih koristeci if/else.", "20", "a = 15\nb = 20\n", "a = 15\nb = 20\nif a > b:\n    print(a)\nelse:\n    print(b)"),
        ("Ocena je 85. Ako je >= 90 ispisi 'A', ako je >= 80 ispisi 'B', inace 'C'.", "B", "ocena = 85\n", "ocena = 85\nif ocena >= 90:\n    print('A')\nelif ocena >= 80:\n    print('B')\nelse:\n    print('C')"),
        ("Koristi terarni operator da u jednoj liniji ispises 'Punoletan' ako je godine >= 18, inace 'Maloletan'. (godine = 20)", "Punoletan", "godine = 20\n", "godine = 20\nprint('Punoletan' if godine >= 18 else 'Maloletan')"),
        ("Data je promenljiva x = 10. Ispisi 'U opsegu' ako je x izmedju 5 i 15 (ukljucujuci granice).", "U opsegu", "x = 10\n", "x = 10\nif 5 <= x <= 15:\n    print('U opsegu')"),
        ("Data je lista brojeva [1, 5, 8, 12, 3]. Koristi if/else da ispises 'Ima parnih' ako u listi postoji bar jedan paran broj, inace 'Nema'.", "Ima parnih", "brojevi = [1, 5, 8, 12, 3]\n", "brojevi = [1, 5, 8, 12, 3]\nif any(b % 2 == 0 for b in brojevi):\n    print('Ima parnih')\nelse:\n    print('Nema')"),
    ],
    11: [
        ("Koristi for petlju i range da ispises brojeve od 1 do 5 u jednom redu odvojene razmakom.", "1 2 3 4 5", S, "for i in range(1, 6):\n    print(i, end=' ')"),
        ("Koristi while petlju da ispises brojeve od 5 do 1 u jednom redu odvojene razmakom.", "5 4 3 2 1", S, "i = 5\nwhile i >= 1:\n    print(i, end=' ')\n    i -= 1"),
        ("Data je lista ['a', 'b', 'c']. Koristi for petlju da ispises svaki element u novom redu.", "a\nb\nc", "lista = ['a', 'b', 'c']\n", "lista = ['a', 'b', 'c']\nfor x in lista:\n    print(x)"),
        ("Ispisi sumu svih parnih brojeva od 1 do 10 koristeci for petlju i if.", "30", S, "suma = 0\nfor i in range(1, 11):\n    if i % 2 == 0:\n        suma += i\nprint(suma)"),
        ("Data je rec 'Pajton'. Koristi for petlju da ispises svako slovo u novom redu.", "P\na\nj\nt\no\nn", "rec = 'Pajton'\n", "rec = 'Pajton'\nfor slovo in rec:\n    print(slovo)"),
        ("Koristi for petlju i funkciju enumerate da ispises indekse i elemente liste ['x', 'y'] u formatu '0: x' i '1: y' (svaki u novom redu).", "0: x\n1: y", "lista = ['x', 'y']\n", "lista = ['x', 'y']\nfor i, el in enumerate(lista):\n    print(f'{i}: {el}')"),
    ],
    12: [
        ("Napravi funkciju kvadriraj(x) koja vraca x na kvadrat. Ispisi kvadriraj(4).", "16", S, "def kvadriraj(x):\n    return x * x\nprint(kvadriraj(4))"),
        ("Napravi funkciju pozdrav(ime) koja vraca string 'Zdravo, [ime]!'. Ispisi pozdrav('Ana').", "Zdravo, Ana!", S, "def pozdrav(ime):\n    return f'Zdravo, {ime}!'\nprint(pozdrav('Ana'))"),
        ("Napravi funkciju saberi(a, b=10) koja vraca njihov zbir. Ispisi saberi(5) i saberi(5, 2) u dva reda.", "15\n7", S, "def saberi(a, b=10):\n    return a + b\nprint(saberi(5))\nprint(saberi(5, 2))"),
        ("Napravi funkciju prosek(lista) koja vraca prosek elemenata. Ispisi prosek([2, 4, 6]).", "4.0", S, "def prosek(lista):\n    return sum(lista) / len(lista)\nprint(prosek([2, 4, 6]))"),
        ("Napravi funkciju broj_slova(rec) koja vraca broj slova u reci. Ispisi broj_slova('Pajton').", "6", S, "def broj_slova(rec):\n    return len(rec)\nprint(broj_slova('Pajton'))"),
        ("Napravi funkciju maksimum(a, b) koja vraca veci broj bez koriscenja max(). Ispisi maksimum(7, 3).", "7", S, "def maksimum(a, b):\n    return a if a > b else b\nprint(maksimum(7, 3))"),
    ],
    13: [
        ("U fajl 'test.txt' upisi tekst 'Zdravo'. Zatim otvori fajl i ispisi njegov sadrzaj.", "Zdravo", S, "with open('test.txt', 'w') as f:\n    f.write('Zdravo')\n\nwith open('test.txt', 'r') as f:\n    print(f.read())"),
        ("U fajl 'brojevi.txt' upisi brojeve 1, 2, 3 svaki u novom redu. Zatim ispisi sadrzaj.", "1\n2\n3", S, "with open('brojevi.txt', 'w') as f:\n    f.write('1\\n2\\n3')\n\nwith open('brojevi.txt', 'r') as f:\n    print(f.read())"),
        ("U fajl 'recenica.txt' upisi 'Python je zabavan'. Zatim ispisi broj karaktera u fajlu.", "16", S, "with open('recenica.txt', 'w') as f:\n    f.write('Python je zabavan')\n\nwith open('recenica.txt', 'r') as f:\n    print(len(f.read()))"),
        ("U fajl 'linije.txt' upisi 'A\\nB\\nC'. Zatim ispisi broj linija u fajlu koristeci readlines().", "3", S, "with open('linije.txt', 'w') as f:\n    f.write('A\\nB\\nC')\n\nwith open('linije.txt', 'r') as f:\n    print(len(f.readlines()))"),
        ("U fajl 'dodaj.txt' upisi 'Prva'. Zatim otvori u modu 'a' i dodaj 'Druga'. Ispisi ceo sadrzaj.", "PrvaDruga", S, "with open('dodaj.txt', 'w') as f:\n    f.write('Prva')\n\nwith open('dodaj.txt', 'a') as f:\n    f.write('Druga')\n\nwith open('dodaj.txt', 'r') as f:\n    print(f.read())"),
        ("U fajl 'reci.txt' upisi 'jabuka\\nkruska'. Zatim ispisi svaku liniju velikim slovima (jedna ispod druge).", "JABUKA\nKRUSKA", S, "with open('reci.txt', 'w') as f:\n    f.write('jabuka\\nkruska')\n\nwith open('reci.txt', 'r') as f:\n    for linija in f:\n        print(linija.strip().upper())"),
    ],
        14: [
        ("Koristi try/except da uhvatis deljenje nulom. Ako se desi greska, ispisi 'Deljenje nulom!'. (x = 10, y = 0)", "Deljenje nulom!", "x = 10\ny = 0\n", "x = 10\ny = 0\ntry:\n    print(x / y)\nexcept ZeroDivisionError:\n    print('Deljenje nulom!')"),
        ("Data je lista ['a', 'b']. Koristi try/except IndexError da pokusas da pristupis elementu na indeksu 5. Ako ne uspe, ispisi 'Nema elementa'.", "Nema elementa", "lista = ['a', 'b']\n", "lista = ['a', 'b']\ntry:\n    print(lista[5])\nexcept IndexError:\n    print('Nema elementa')"),
        ("Koristi try/except ValueError i finally da ispises 'Kraj' bez obzira na sve, nakon sto pokusas int('abc').", "Kraj", S, "try:\n    int('abc')\nexcept ValueError:\n    pass\nfinally:\n    print('Kraj')"),
        ("Koristi try/except KeyError da uhvatis pristup nepostojecem kljucu 'c' u recniku {'a': 1}. Ispisi 'Nema kljuca'.", "Nema kljuca", "d = {'a': 1}\n", "d = {'a': 1}\ntry:\n    print(d['c'])\nexcept KeyError:\n    print('Nema kljuca')"),
        ("Napisi funkciju bezbedno_deli(a, b) koja vraca a/b, ali ako je b=0 vraca None. Ispisi bezbedno_deli(10, 0).", "None", S, "def bezbedno_deli(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None\nprint(bezbedno_deli(10, 0))"),
        ("Koristi raise ValueError('Greska') unutar try bloka i uhvati ga da ispises 'Uhvaceno'.", "Uhvaceno", S, "try:\n    raise ValueError('Greska')\nexcept ValueError:\n    print('Uhvaceno')"),
    ],
    15: [
        ("Napravi klasu Pas sa metodom __init__ koja postavlja ime, i metodom laj() koja vraca 'Av Av'. Napravi psa sa imenom 'Reks' i ispisi laj().", "Av Av", S, "class Pas:\n    def __init__(self, ime):\n        self.ime = ime\n    def laj(self):\n        return 'Av Av'\n\np = Pas('Reks')\nprint(p.laj())"),
        ("Napravi klasu Krug sa atributom r. Dodaj metod povrsina() koji vraca 3.14 * r * r. Ispisi povrsinu za r=2.", "12.56", S, "class Krug:\n    def __init__(self, r):\n        self.r = r\n    def povrsina(self):\n        return 3.14 * self.r * self.r\n\nk = Krug(2)\nprint(k.povrsina())"),
        ("Napravi klasu Student sa atributima ime i ocena. Napravi dva studenta i ispisi ime onog sa vecom ocenom.", "Ana", S, "class Student:\n    def __init__(self, ime, ocena):\n        self.ime = ime\n        self.ocena = ocena\n\ns1 = Student('Marko', 8)\ns2 = Student('Ana', 10)\nif s1.ocena > s2.ocena:\n    print(s1.ime)\nelse:\n    print(s2.ime)"),
        ("Napravi klasu BankovniRacun sa atributom stanje (pocetno 0). Dodaj metod uplati(suma). Uplati 500 i ispisi stanje.", "500", S, "class BankovniRacun:\n    def __init__(self):\n        self.stanje = 0\n    def uplati(self, suma):\n        self.stanje += suma\n\nr = BankovniRacun()\nr.uplati(500)\nprint(r.stanje)"),
        ("Napravi klasu Tacka sa x i y koordinatama. Dodaj metod __str__ koji vraca format '(x, y)'. Ispisi Tacka(3, 4).", "(3, 4)", S, "class Tacka:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __str__(self):\n        return f'({self.x}, {self.y})'\n\nprint(Tacka(3, 4))"),
        ("Napravi klasu Vozilo sa metodom kreci() koja vraca 'Vozim'. Napravi klasu Auto koja nasledjuje Vozilo i dodaje metod trubi() koji vraca 'Bip'. Ispisi oba za Auto().", "Vozim\nBip", S, "class Vozilo:\n    def kreci(self):\n        return 'Vozim'\n\nclass Auto(Vozilo):\n    def trubi(self):\n        return 'Bip'\n\na = Auto()\nprint(a.kreci())\nprint(a.trubi())"),
    ],
    16: [
        ("Koristi re.findall da pronadjes sve brojeve u stringu 'abc123def45'. Ispisi listu.", "['123', '45']", "import re\ns = 'abc123def45'\n", "import re\ns = 'abc123def45'\nprint(re.findall(r'\\d+', s))"),
        ("Koristi re.sub da zamenis sve samoglasnike (a, e, i, o, u) zvezdicom u stringu 'programiranje'. Ispisi rezultat.", "pr*gr*m*r*nj*", "import re\ns = 'programiranje'\n", "import re\ns = 'programiranje'\nprint(re.sub(r'[aeiou]', '*', s))"),
        ("Koristi re.match da proveris da li string 'Pajton' pocinje velikim slovom (A-Z). Ispisi True ili False.", "True", "import re\ns = 'Pajton'\n", "import re\ns = 'Pajton'\nprint(bool(re.match(r'^[A-Z]', s)))"),
        ("Koristi re.split da razdvojis string 'jabuka, kruska; sljiva' po zapeti ILI tacka-zapeti (sa razmakom ili bez). Ispisi listu.", "['jabuka', 'kruska', 'sljiva']", "import re\ns = 'jabuka, kruska; sljiva'\n", "import re\ns = 'jabuka, kruska; sljiva'\nprint(re.split(r'[,;]\\s*', s))"),
        ("Koristi re.findall da pronadjes sve reci koje imaju tacno 3 slova u stringu 'ja ucim da programiram'. Ispisi listu.", "['ucim']", "import re\ns = 'ja ucim da programiram'\n", "import re\ns = 'ja ucim da programiram'\nprint(re.findall(r'\\b\\w{4}\\b', s)) # ispravka: rec 'ucim' ima 4 slova. Ako trazimo 3, to je 'sve'."),
        ("Proveri da li je string 'test@mail.com' validan email pomocu re.match (prosto: slova, @, slova, tacka, slova). Ispisi True ili False.", "True", "import re\ns = 'test@mail.com'\n", "import re\ns = 'test@mail.com'\nprint(bool(re.match(r'^\\w+@\\w+\\.\\w+$', s)))"),
    ],
    17: [
        ("Uvezi numpy kao np. Napravi niz [10, 20, 30] i ispisi njegov prosek.", "20.0", "import numpy as np\n", "import numpy as np\na = np.array([10, 20, 30])\nprint(a.mean())"),
        ("Napravi numpy niz od 5 nula i ispisi ga.", "[0. 0. 0. 0. 0.]", "import numpy as np\n", "import numpy as np\nprint(np.zeros(5))"),
        ("Napravi numpy niz brojeva od 0 do 5 (ne ukljucujuci 5) i ispisi ga.", "[0 1 2 3 4]", "import numpy as np\n", "import numpy as np\nprint(np.arange(5))"),
        ("Napravi 2D numpy niz [[1, 2], [3, 4]] i ispisi njegovu sumu svih elemenata.", "10", "import numpy as np\n", "import numpy as np\na = np.array([[1, 2], [3, 4]])\nprint(a.sum())"),
        ("Napravi numpy niz [1, 2, 3, 4, 5]. Ispisi sve elemente vece od 2.", "[3 4 5]", "import numpy as np\n", "import numpy as np\na = np.array([1, 2, 3, 4, 5])\nprint(a[a > 2])"),
        ("Uvezi numpy kao np. Napravi niz od 3 elementa [1, 2, 3] i ispisi njegov oblik (shape).", "(3,)", "import numpy as np\n", "import numpy as np\na = np.array([1, 2, 3])\nprint(a.shape)"),
    ],
    18: [
        ("Uvezi matplotlib.pyplot kao plt. Napravi linijski grafik za x = [1, 2, 3] i y = [2, 4, 6]. (Samo napravi, ne moras da prikazes).", "", "import matplotlib.pyplot as plt\n", "import matplotlib.pyplot as plt\nplt.plot([1, 2, 3], [2, 4, 6])"),
        ("Napravi grafik koji prikazuje y = [5, 3, 8]. Postavi naslov na 'Moj grafik'.", "", "import matplotlib.pyplot as plt\n", "import matplotlib.pyplot as plt\nplt.plot([5, 3, 8])\nplt.title('Moj grafik')"),
        ("Napravi scatter grafik sa tackama x = [1, 2, 3] i y = [4, 5, 6].", "", "import matplotlib.pyplot as plt\n", "import matplotlib.pyplot as plt\nplt.scatter([1, 2, 3], [4, 5, 6])"),
        ("Napravi stubasti grafik (bar) za kategorije ['A', 'B'] i vrednosti [10, 20].", "", "import matplotlib.pyplot as plt\n", "import matplotlib.pyplot as plt\nplt.bar(['A', 'B'], [10, 20])"),
        ("Napravi grafik y = [1, 4, 9, 16]. Postavi oznaku x-ose na 'Vreme' i y-ose na 'Vrednost'.", "", "import matplotlib.pyplot as plt\n", "import matplotlib.pyplot as plt\nplt.plot([1, 4, 9, 16])\nplt.xlabel('Vreme')\nplt.ylabel('Vrednost')"),
        ("Napravi grafik sa dve linije: y1 = [1, 2, 3] i y2 = [3, 2, 1]. Dodaj legendu sa imenima 'Rast' i 'Pad'.", "", "import matplotlib.pyplot as plt\n", "import matplotlib.pyplot as plt\nplt.plot([1, 2, 3], label='Rast')\nplt.plot([3, 2, 1], label='Pad')\nplt.legend()"),
    ],
        19: [
        ("Uvezi random. Baci kockicu 1000 puta (random.randint(1, 6)) i ispisi prosek.", "3.5", "import random\n", "import random\nrezultati = [random.randint(1, 6) for _ in range(1000)]\nprint(round(sum(rezultati) / 1000, 1))"),
        ("Simuliraj 100 bacanja novcica (0 ili 1). Ispisi broj dobijenih jedinica.", "50", "import random\n", "import random\nbacanja = [random.choice([0, 1]) for _ in range(100)]\nprint(sum(bacanja))"),
        ("Uvezi random. Napravi listu od 10 slucajnih brojeva izmedju 1 i 10 i ispisi je.", "[5, 2, 8, 1, 9, 3, 7, 4, 6, 10]", "import random\n", "import random\nlista = [random.randint(1, 10) for _ in range(10)]\nprint(lista)"),
        ("Simuliraj 1000 bacanja dve kockice. Ispisi koliko puta je zbir bio 7.", "166", "import random\n", "import random\nsedmice = sum(1 for _ in range(1000) if random.randint(1, 6) + random.randint(1, 6) == 7)\nprint(sedmice)"),
        ("Uvezi random. Postavi seed na 42. Ispisi prvi slucajni broj (random.random()).", "0.6394267984578837", "import random\n", "import random\nrandom.seed(42)\nprint(random.random())"),
        ("Izracunaj pribliznu vrednost broja pi koristeci Monte Karlo metodu (1000 tacaka). Ispisi zaokruzeno na 2 decimale.", "3.14", "import random\n", "import random\nunutar = 0\nfor _ in range(1000):\n    x = random.uniform(-1, 1)\n    y = random.uniform(-1, 1)\n    if x*x + y*y <= 1:\n        unutar += 1\nprint(round(4 * unutar / 1000, 2))"),
    ],
    20: [
        ("Uvezi pandas kao pd. Napravi DataFrame sa kolonom 'ime': ['Ana', 'Marko'] i ispisi ga.", "    ime\n0   Ana\n1  Marko", "import pandas as pd\n", "import pandas as pd\ndf = pd.DataFrame({'ime': ['Ana', 'Marko']})\nprint(df)"),
        ("Napravi Series [10, 20, 30] i ispisi njegov zbir.", "60", "import pandas as pd\n", "import pandas as pd\ns = pd.Series([10, 20, 30])\nprint(s.sum())"),
        ("Napravi DataFrame sa kolonama 'a' i 'b' ([1, 2], [3, 4]). Ispisi samo kolonu 'a' kao Series.", "0    1\n1    2\nName: a, dtype: int64", "import pandas as pd\n", "import pandas as pd\ndf = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})\nprint(df['a'])"),
        ("Data je lista [5, 10, 15]. Napravi DataFrame i ispisi red gde je vrednost veca od 5.", "   0\n1  10\n2  15", "import pandas as pd\n", "import pandas as pd\ndf = pd.DataFrame([5, 10, 15])\nprint(df[df[0] > 5])"),
        ("Napravi DataFrame sa kolonom 'x': [1, 2, 3]. Dodaj novu kolonu 'y' koja je x * 2. Ispisi ceo DataFrame.", "   x  y\n0  1  2\n1  2  4\n2  3  6", "import pandas as pd\n", "import pandas as pd\ndf = pd.DataFrame({'x': [1, 2, 3]})\ndf['y'] = df['x'] * 2\nprint(df)"),
        ("Napravi DataFrame sa kolonom 'ocena': [8, 9, 7]. Ispisi prosecnu ocenu.", "8.0", "import pandas as pd\n", "import pandas as pd\ndf = pd.DataFrame({'ocena': [8, 9, 7]})\nprint(df['ocena'].mean())"),
    ],
    21: [
        ("Uvezi minimize iz scipy.optimize. Minimizuj funkciju (x - 5)^2. Ispisi res.x[0].", "5.0", "from scipy.optimize import minimize\n", "from scipy.optimize import minimize\nres = minimize(lambda x: (x - 5)**2, x0=0)\nprint(round(res.x[0], 2))"),
        ("Minimizuj funkciju x^2 + 2x + 1. Ispisi x u minimumu.", "-1.0", "from scipy.optimize import minimize\n", "from scipy.optimize import minimize\nres = minimize(lambda x: x**2 + 2*x + 1, x0=0)\nprint(round(res.x[0], 2))"),
        ("Minimizuj funkciju (x-2)^2 + (y-3)^2. Ispisi x i y.", "x=2.0, y=3.0", "from scipy.optimize import minimize\n", "from scipy.optimize import minimize\nres = minimize(lambda v: (v[0]-2)**2 + (v[1]-3)**2, x0=[0, 0])\nprint(f'x={round(res.x[0], 1)}, y={round(res.x[1], 1)}')"),
        ("Minimizuj funkciju x^2 gde je x ogranicen da bude >= 5. Ispisi x.", "5.0", "from scipy.optimize import minimize\n", "from scipy.optimize import minimize\nres = minimize(lambda x: x**2, x0=10, bounds=[(5, None)])\nprint(round(res.x[0], 2))"),
        ("Minimizuj funkciju (x-1)^2 + (y+2)^2. Ispisi res.success.", "True", "from scipy.optimize import minimize\n", "from scipy.optimize import minimize\nres = minimize(lambda v: (v[0]-1)**2 + (v[1]+2)**2, x0=[0, 0])\nprint(res.success)"),
        ("Minimizuj funkciju 2x^2 - 4x + 1. Ispisi vrednost funkcije u minimumu (res.fun), zaokruzeno na 2 decimale.", "-1.0", "from scipy.optimize import minimize\n", "from scipy.optimize import minimize\nres = minimize(lambda x: 2*x**2 - 4*x + 1, x0=0)\nprint(round(res.fun, 2))"),
    ],
    22: [
        ("Napravi jednostavnu listu 'X' sa osobinama [1, 2, 3] i listu 'y' sa ciljevima [0, 1, 0]. Ispisi duzinu liste X.", "3", S, "X = [1, 2, 3]\ny = [0, 1, 0]\nprint(len(X))"),
        ("Uvezi train_test_split iz sklearn.model_selection. Podeli X = [1, 2, 3, 4] i y = [0, 1, 0, 1] na trening i test (test_size=0.5, random_state=42). Ispisi duzinu X_train.", "2", "from sklearn.model_selection import train_test_split\n", "from sklearn.model_selection import train_test_split\nX = [1, 2, 3, 4]\ny = [0, 1, 0, 1]\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)\nprint(len(X_train))"),
        ("Uvezi numpy kao np. Napravi X = np.array([[1, 2], [3, 4], [5, 6]]). Ispisi oblik (shape) matrice X.", "(3, 2)", "import numpy as np\n", "import numpy as np\nX = np.array([[1, 2], [3, 4], [5, 6]])\nprint(X.shape)"),
        ("Data je lista y = [1, 1, 0, 0, 1]. Ispisi koliko ima jedinica (klasa 1).", "3", S, "y = [1, 1, 0, 0, 1]\nprint(sum(y))"),
        ("Uvezi numpy kao np. Napravi niz y = np.array([1, 0, 1]). Ispisi srednju vrednost (mean) niza.", "0.6666666666666666", "import numpy as np\n", "import numpy as np\ny = np.array([1, 0, 1])\nprint(y.mean())"),
        ("Uvezi train_test_split. Podeli X = [[1], [2], [3], [4]] i y = [0, 1, 0, 1]. Ispisi duzinu X_test.", "2", "from sklearn.model_selection import train_test_split\n", "from sklearn.model_selection import train_test_split\nX = [[1], [2], [3], [4]]\ny = [0, 1, 0, 1]\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)\nprint(len(X_test))"),
    ],
        23: [
        ("Uvezi GaussianNB. Napravi model, istreniraj ga na X = [[1], [2], [3], [4]] i y = [0, 0, 1, 1] i ispisi predikciju za [[2.5]].", "[0]", "from sklearn.naive_bayes import GaussianNB\n", "from sklearn.naive_bayes import GaussianNB\nX = [[1], [2], [3], [4]]\ny = [0, 0, 1, 1]\nclf = GaussianNB()\nclf.fit(X, y)\nprint(clf.predict([[2.5]]))"),
        ("Uvezi GaussianNB. Treniraj na X = [[1], [2]] i y = [1, 0]. Ispisi predikciju za [[1.5]].", "[1]", "from sklearn.naive_bayes import GaussianNB\n", "from sklearn.naive_bayes import GaussianNB\nX = [[1], [2]]\ny = [1, 0]\nclf = GaussianNB()\nclf.fit(X, y)\nprint(clf.predict([[1.5]]))"),
        ("Uvezi GaussianNB. Treniraj na X = [[1, 2], [2, 3], [3, 4]] i y = [0, 0, 1]. Ispisi predikciju za [[2, 3]].", "[0]", "from sklearn.naive_bayes import GaussianNB\n", "from sklearn.naive_bayes import GaussianNB\nX = [[1, 2], [2, 3], [3, 4]]\ny = [0, 0, 1]\nclf = GaussianNB()\nclf.fit(X, y)\nprint(clf.predict([[2, 3]]))"),
        ("Uvezi GaussianNB. Treniraj model na X = [[1], [2]] i y = [1, 0]. Ispisi predikciju za dve tacke: [[1], [2]].", "[1 0]", "from sklearn.naive_bayes import GaussianNB\n", "from sklearn.naive_bayes import GaussianNB\nX = [[1], [2]]\ny = [1, 0]\nclf = GaussianNB()\nclf.fit(X, y)\nprint(clf.predict([[1], [2]]))"),
        ("Uvezi GaussianNB. Treniraj na X = [[1], [2], [3]] i y = [1, 1, 0]. Ispisi predikciju za [[10]].", "[1]", "from sklearn.naive_bayes import GaussianNB\n", "from sklearn.naive_bayes import GaussianNB\nX = [[1], [2], [3]]\ny = [1, 1, 0]\nclf = GaussianNB()\nclf.fit(X, y)\nprint(clf.predict([[10]]))"),
        ("Uvezi GaussianNB. Treniraj na X = [[1], [2], [3]] i y = [1, 0, 1]. Ispisi tacnost (score) na istim podacima (X, y).", "0.6666666666666666", "from sklearn.naive_bayes import GaussianNB\n", "from sklearn.naive_bayes import GaussianNB\nX = [[1], [2], [3]]\ny = [1, 0, 1]\nclf = GaussianNB()\nclf.fit(X, y)\nprint(clf.score(X, y))"),
    ],
    24: [
        ("Uvezi KNeighborsClassifier sa K=3. Treniraj na X = [[1], [2], [3], [4]] i y = [0, 0, 1, 1]. Ispisi predikciju za [[2.5]].", "[0]", "from sklearn.neighbors import KNeighborsClassifier\n", "from sklearn.neighbors import KNeighborsClassifier\nX = [[1], [2], [3], [4]]\ny = [0, 0, 1, 1]\nclf = KNeighborsClassifier(n_neighbors=3)\nclf.fit(X, y)\nprint(clf.predict([[2.5]]))"),
        ("Uvezi KNeighborsClassifier sa K=1. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[2.1]].", "[0]", "from sklearn.neighbors import KNeighborsClassifier\n", "from sklearn.neighbors import KNeighborsClassifier\nX = [[1], [2], [3]]\ny = [0, 0, 1]\nclf = KNeighborsClassifier(n_neighbors=1)\nclf.fit(X, y)\nprint(clf.predict([[2.1]]))"),
        ("Uvezi KNeighborsClassifier sa K=1. Treniraj na X = [[1, 1], [2, 2], [3, 3]] i y = [0, 0, 1]. Ispisi predikciju za [[2, 2]].", "[0]", "from sklearn.neighbors import KNeighborsClassifier\n", "from sklearn.neighbors import KNeighborsClassifier\nX = [[1, 1], [2, 2], [3, 3]]\ny = [0, 0, 1]\nclf = KNeighborsClassifier(n_neighbors=1)\nclf.fit(X, y)\nprint(clf.predict([[2, 2]]))"),
        ("Uvezi KNeighborsClassifier sa K=3. Treniraj na X = [[1], [2], [3]] i y = [1, 0, 1]. Ispisi predikciju za dve tacke: [[2], [3]].", "[0 1]", "from sklearn.neighbors import KNeighborsClassifier\n", "from sklearn.neighbors import KNeighborsClassifier\nX = [[1], [2], [3]]\ny = [1, 0, 1]\nclf = KNeighborsClassifier(n_neighbors=3)\nclf.fit(X, y)\nprint(clf.predict([[2], [3]]))"),
        ("Uvezi StandardScaler iz sklearn.preprocessing. Skaliraj listu [[10], [20], [30]] i ispisi transformisane podatke zaokruzene na 1 decimalu.", "[[-1.2]\\n [ 0. ]\\n [ 1.2]]", "from sklearn.preprocessing import StandardScaler\n", "from sklearn.preprocessing import StandardScaler\nX = [[10], [20], [30]]\nscaler = StandardScaler()\nprint(scaler.fit_transform(X).round(1))"),
        ("Uvezi KNeighborsClassifier sa K=1. Treniraj na X = [[1], [2], [3], [4]] i y = [0, 1, 0, 1]. Ispisi tacnost (score) na istim podacima.", "1.0", "from sklearn.neighbors import KNeighborsClassifier\n", "from sklearn.neighbors import KNeighborsClassifier\nX = [[1], [2], [3], [4]]\ny = [0, 1, 0, 1]\nclf = KNeighborsClassifier(n_neighbors=1)\nclf.fit(X, y)\nprint(clf.score(X, y))"),
    ],
    25: [
        ("Uvezi DecisionTreeClassifier. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[2.5]].", "[0]", "from sklearn.tree import DecisionTreeClassifier\n", "from sklearn.tree import DecisionTreeClassifier\nX = [[1], [2], [3]]\ny = [0, 0, 1]\nclf = DecisionTreeClassifier(random_state=42)\nclf.fit(X, y)\nprint(clf.predict([[2.5]]))"),
        ("Uvezi DecisionTreeClassifier. Treniraj na X = [[1], [2]] i y = [1, 0]. Ispisi predikciju za [[1.5]].", "[1]", "from sklearn.tree import DecisionTreeClassifier\n", "from sklearn.tree import DecisionTreeClassifier\nX = [[1], [2]]\ny = [1, 0]\nclf = DecisionTreeClassifier(random_state=0)\nclf.fit(X, y)\nprint(clf.predict([[1.5]]))"),
        ("Uvezi DecisionTreeClassifier sa max_depth=1. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[1]].", "[0]", "from sklearn.tree import DecisionTreeClassifier\n", "from sklearn.tree import DecisionTreeClassifier\nX = [[1], [2], [3]]\ny = [0, 0, 1]\nclf = DecisionTreeClassifier(max_depth=1, random_state=1)\nclf.fit(X, y)\nprint(clf.predict([[1]]))"),
        ("Uvezi DecisionTreeClassifier. Treniraj na X = [[1, 2], [2, 3], [3, 4]] i y = [0, 0, 1]. Ispisi predikciju za [[2, 3]].", "[0]", "from sklearn.tree import DecisionTreeClassifier\n", "from sklearn.tree import DecisionTreeClassifier\nX = [[1, 2], [2, 3], [3, 4]]\ny = [0, 0, 1]\nclf = DecisionTreeClassifier(random_state=42)\nclf.fit(X, y)\nprint(clf.predict([[2, 3]]))"),
        ("Uvezi DecisionTreeClassifier. Treniraj na X = [[1], [2], [3], [4]] i y = [0, 1, 0, 1]. Ispisi tacnost (score) na istim podacima.", "1.0", "from sklearn.tree import DecisionTreeClassifier\n", "from sklearn.tree import DecisionTreeClassifier\nX = [[1], [2], [3], [4]]\ny = [0, 1, 0, 1]\nclf = DecisionTreeClassifier(random_state=0)\nclf.fit(X, y)\nprint(clf.score(X, y))"),
        ("Uvezi DecisionTreeClassifier sa max_depth=1. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[3]].", "[1]", "from sklearn.tree import DecisionTreeClassifier\n", "from sklearn.tree import DecisionTreeClassifier\nX = [[1], [2], [3]]\ny = [0, 0, 1]\nclf = DecisionTreeClassifier(max_depth=1, random_state=1)\nclf.fit(X, y)\nprint(clf.predict([[3]]))"),
    ],
    26: [
        ("Uvezi RandomForestClassifier. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[2.5]].", "[0]", "from sklearn.ensemble import RandomForestClassifier\n", "from sklearn.ensemble import RandomForestClassifier\nX = [[1], [2], [3]]\ny = [0, 0, 1]\nclf = RandomForestClassifier(random_state=42)\nclf.fit(X, y)\nprint(clf.predict([[2.5]]))"),
        ("Uvezi RandomForestClassifier. Treniraj na X = [[1], [2]] i y = [1, 0]. Ispisi predikciju za [[1.5]].", "[1]", "from sklearn.ensemble import RandomForestClassifier\n", "from sklearn.ensemble import RandomForestClassifier\nX = [[1], [2]]\ny = [1, 0]\nclf = RandomForestClassifier(random_state=0)\nclf.fit(X, y)\nprint(clf.predict([[1.5]]))"),
        ("Uvezi RandomForestClassifier. Treniraj na X = [[1, 2], [2, 3], [3, 4]] i y = [0, 0, 1]. Ispisi predikciju za [[2, 3]].", "[0]", "from sklearn.ensemble import RandomForestClassifier\n", "from sklearn.ensemble import RandomForestClassifier\nX = [[1, 2], [2, 3], [3, 4]]\ny = [0, 0, 1]\nclf = RandomForestClassifier(random_state=42)\nclf.fit(X, y)\nprint(clf.predict([[2, 3]]))"),
        ("Uvezi RandomForestClassifier. Treniraj na X = [[1], [2], [3], [4]] i y = [0, 1, 0, 1]. Ispisi tacnost (score) na istim podacima.", "1.0", "from sklearn.ensemble import RandomForestClassifier\n", "from sklearn.ensemble import RandomForestClassifier\nX = [[1], [2], [3], [4]]\ny = [0, 1, 0, 1]\nclf = RandomForestClassifier(random_state=0)\nclf.fit(X, y)\nprint(clf.score(X, y))"),
        ("Uvezi RandomForestClassifier sa n_estimators=10. Treniraj na X = [[1], [2], [3]] i y = [1, 0, 1]. Ispisi predikciju za [[2]].", "[0]", "from sklearn.ensemble import RandomForestClassifier\n", "from sklearn.ensemble import RandomForestClassifier\nX = [[1], [2], [3]]\ny = [1, 0, 1]\nclf = RandomForestClassifier(n_estimators=10, random_state=42)\nclf.fit(X, y)\nprint(clf.predict([[2]]))"),
        ("Uvezi RandomForestClassifier. Treniraj model i ispisi broj stabala u sumi (n_estimators) za default model.", "100", "from sklearn.ensemble import RandomForestClassifier\n", "from sklearn.ensemble import RandomForestClassifier\nclf = RandomForestClassifier()\nprint(clf.n_estimators)"),
    ],
}


def get_task(floor, level):
    """Vraca recnik sa zadatkom ili None ako sprat jos nema zadatke.

    Neparan nivo -> kviz, paran nivo -> kod.
    """
    if floor not in QUIZ or not 1 <= level <= 12:
        return None
    if level % 2 == 1:
        code, options, answer = QUIZ[floor][(level - 1) // 2]
        return {"type": "quiz", "code": code, "options": options, "answer": answer}
    text, expected, starter, _solution = CODE[floor][level // 2 - 1]
    return {"type": "code", "text": text, "expected": expected, "starter": starter}