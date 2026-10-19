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