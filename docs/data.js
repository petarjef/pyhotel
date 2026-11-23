window.HOTEL_DATA = {
 "lessons": [
  "Osnove programiranja",
  "Pajton okruzenje",
  "Osnovni elementi jezika",
  "Logicke promenljive",
  "Stringovi",
  "Liste",
  "Jos o stringovima i listama",
  "Moduli",
  "Torke, skupovi i recnici",
  "Naredbe grananja",
  "Petlje",
  "Funkcije",
  "Rad sa datotekama",
  "Upravljanje greskama",
  "Klase",
  "Regularni izrazi",
  "Uvod u NumPy",
  "Matplotlib",
  "Monte Karlo simulacije",
  "Pandas",
  "Optimizacija: SciPy",
  "Nadgledano ucenje",
  "Naivni Bajesovi klasifikatori",
  "K najblizih suseda",
  "Stabla odlucivanja",
  "Ansambl metode"
 ],
 "quiz": {
  "1": [
   {
    "code": "print(\"Hello\")",
    "options": [
     "Hello",
     "\"Hello\"",
     "print Hello",
     "Greska"
    ],
    "answer": 0
   },
   {
    "code": "x = 5\ny = 3\nprint(x + y)",
    "options": [
     "8",
     "53",
     "x + y",
     "Greska"
    ],
    "answer": 0
   },
   {
    "code": "a = 5\nb = a\na = 10\nprint(a, b)",
    "options": [
     "10 5",
     "10 10",
     "5 5",
     "5 10"
    ],
    "answer": 0
   },
   {
    "code": "x = 7\nx = x // 2 + x % 2 * 3\nprint(x)",
    "options": [
     "9",
     "4",
     "6",
     "3"
    ],
    "answer": 2
   },
   {
    "code": "print(2 + 3 * 4 ** 2 / 8)",
    "options": [
     "8",
     "80.0",
     "6.0",
     "8.0"
    ],
    "answer": 3
   },
   {
    "code": "print(\"3\" * 2 + str(3 * 2))",
    "options": [
     "66",
     "336",
     "12",
     "Greska (TypeError)"
    ],
    "answer": 1
   }
  ],
  "2": [
   {
    "code": "print(\"a\", \"b\")",
    "options": [
     "a b",
     "ab",
     "a,b",
     "\"a\" \"b\""
    ],
    "answer": 0
   },
   {
    "code": "print(\"a\", \"b\", sep=\"-\")",
    "options": [
     "a-b",
     "a - b",
     "a b -",
     "ab-"
    ],
    "answer": 0
   },
   {
    "code": "print(\"a\" \"b\", \"c\")",
    "options": [
     "a b c",
     "ab, c",
     "Greska (SyntaxError)",
     "ab c"
    ],
    "answer": 3
   },
   {
    "code": "print(len(\"a\\tb\\n\"), len(r\"a\\tb\\n\"))",
    "options": [
     "4 4",
     "6 6",
     "4 6",
     "6 4"
    ],
    "answer": 2
   },
   {
    "code": "print(\"A\", end=\"\")\nprint()\nprint(\"B\", end=\"\")",
    "options": [
     "A\nB",
     "AB",
     "A B",
     "B"
    ],
    "answer": 0
   },
   {
    "code": "x = 1\n  print(x)",
    "options": [
     "1",
     "IndentationError",
     "NameError",
     "TypeError"
    ],
    "answer": 1
   }
  ],
  "3": [
   {
    "code": "print(type(3.0))",
    "options": [
     "<class 'float'>",
     "<class 'int'>",
     "float",
     "3.0"
    ],
    "answer": 0
   },
   {
    "code": "print(7 // 2)",
    "options": [
     "3.5",
     "3",
     "4",
     "1"
    ],
    "answer": 1
   },
   {
    "code": "print(-7 // 2, -7 % 2)",
    "options": [
     "-3 -1",
     "-4 -1",
     "-3 1",
     "-4 1"
    ],
    "answer": 3
   },
   {
    "code": "print(type(2 ** 3).__name__, type(2 ** -1).__name__, type(10 / 5).__name__)",
    "options": [
     "int int float",
     "int float int",
     "int float float",
     "float float float"
    ],
    "answer": 2
   },
   {
    "code": "print(round(2.5), round(3.5), round(-0.5))",
    "options": [
     "2 4 0",
     "3 4 -1",
     "3 4 0",
     "2 3 0"
    ],
    "answer": 0
   },
   {
    "code": "print(0.1 + 0.2 == 0.3, abs(0.1 + 0.2 - 0.3) < 1e-9)",
    "options": [
     "True True",
     "False True",
     "True False",
     "False False"
    ],
    "answer": 1
   }
  ],
  "4": [
   {
    "code": "print(5 > 3)",
    "options": [
     "True",
     "False",
     "5",
     "Greska"
    ],
    "answer": 0
   },
   {
    "code": "print(10 == 10.0)",
    "options": [
     "False",
     "True",
     "Greska",
     "10"
    ],
    "answer": 1
   },
   {
    "code": "print(1 and 2, 0 or 3, not 5)",
    "options": [
     "True True False",
     "1 0 True",
     "2 3 True",
     "2 3 False"
    ],
    "answer": 3
   },
   {
    "code": "print(bool(\"False\"), bool(\"\"), bool(\" \"), bool([]))",
    "options": [
     "False False False False",
     "True False False False",
     "True False True False",
     "True True True False"
    ],
    "answer": 2
   },
   {
    "code": "x = 5\nprint(1 < x < 10 == 10, 10 > x > 7)",
    "options": [
     "True True",
     "True False",
     "False False",
     "False True"
    ],
    "answer": 1
   },
   {
    "code": "a = None\nprint(a or \"x\", a and \"y\", (a is None) + 1)",
    "options": [
     "x None 2",
     "x y 2",
     "None y 2",
     "x None True"
    ],
    "answer": 0
   }
  ],
  "5": [
   {
    "code": "s = \"Python\"\nprint(s[0])",
    "options": [
     "P",
     "y",
     "Python",
     "n"
    ],
    "answer": 0
   },
   {
    "code": "print(\"Python\"[-1])",
    "options": [
     "P",
     "n",
     "o",
     "Greska"
    ],
    "answer": 1
   },
   {
    "code": "s = \"programiranje\"\nprint(s[-4:-1] + s[5:2:-1])",
    "options": [
     "anjgra",
     "anjarg",
     "anj",
     "njearg"
    ],
    "answer": 1
   },
   {
    "code": "s = \"a,b,,c\"\nprint(s.split(\",\"), len(\"a  b\".split()), len(\"a  b\".split(\" \")))",
    "options": [
     "['a', 'b', 'c'] 2 2",
     "['a', 'b', '', 'c'] 2 2",
     "['a', 'b', 'c'] 2 3",
     "['a', 'b', '', 'c'] 2 3"
    ],
    "answer": 3
   },
   {
    "code": "s = \"Python\"\nt = s.replace(\"y\", \"Y\").lower()\nprint(s, t, s is t)",
    "options": [
     "Python python False",
     "python python True",
     "PYthon python False",
     "Python Python False"
    ],
    "answer": 0
   },
   {
    "code": "print(\"abc\" < \"abd\", \"Z\" < \"a\", \"10\" < \"9\", \"abc\" < \"ab\")",
    "options": [
     "True False True False",
     "True True False True",
     "True True True False",
     "False True True False"
    ],
    "answer": 2
   }
  ],
  "6": [
   {
    "code": "a = [1, 2, 3]\nprint(a[1])",
    "options": [
     "1",
     "2",
     "3",
     "[2]"
    ],
    "answer": 1
   },
   {
    "code": "a = [1, 2, 3]\na.append(4)\nprint(a)",
    "options": [
     "[1, 2, 3, 4]",
     "[4, 1, 2, 3]",
     "[1, 2, 3]",
     "None"
    ],
    "answer": 0
   },
   {
    "code": "a = [1, 2, 3]\nb = [1, 2, 3]\nprint(a == b, a is b, a < [1, 2, 4])",
    "options": [
     "True True True",
     "False False True",
     "True False True",
     "True False False"
    ],
    "answer": 2
   },
   {
    "code": "a = [1, 2, 3, 4, 5]\nprint(a[::-2], a[-4:-1], a[10:])",
    "options": [
     "[5, 3, 1] [2, 3, 4] Greska (IndexError)",
     "[1, 3, 5] [2, 3, 4] []",
     "[5, 3, 1] [3, 4, 5] []",
     "[5, 3, 1] [2, 3, 4] []"
    ],
    "answer": 3
   },
   {
    "code": "a = [3, 1, 2]\nb = a.sort()\nprint(a, b)",
    "options": [
     "[3, 1, 2] [1, 2, 3]",
     "[1, 2, 3] None",
     "[1, 2, 3] [1, 2, 3]",
     "[3, 1, 2] None"
    ],
    "answer": 1
   },
   {
    "code": "a = [1, 2, 3, 4]\na.insert(10, 9)\na.insert(-1, 7)\nprint(a)",
    "options": [
     "[1, 2, 3, 4, 7, 9]",
     "[1, 2, 3, 4, 9, 7]",
     "Greska (IndexError)",
     "[1, 2, 3, 7, 4, 9]"
    ],
    "answer": 0
   }
  ],
  "7": [
   {
    "code": "print(\"a,b,c\".split(\",\"))",
    "options": [
     "['a', 'b', 'c']",
     "a b c",
     "['a,b,c']",
     "a,b,c"
    ],
    "answer": 0
   },
   {
    "code": "print(\"-\".join([\"x\", \"y\", \"z\"]))",
    "options": [
     "xyz",
     "x-y-z",
     "-x-y-z-",
     "['x-y-z']"
    ],
    "answer": 1
   },
   {
    "code": "a = [[0] * 2] * 2\nb = [[0] * 2 for _ in range(2)]\na[0][0] = 1\nb[0][0] = 1\nprint(a, b)",
    "options": [
     "[[1, 0], [1, 0]] [[1, 0], [0, 0]]",
     "[[1, 0], [0, 0]] [[1, 0], [0, 0]]",
     "[[1, 0], [1, 0]] [[1, 0], [1, 0]]",
     "[[1, 0], [0, 0]] [[1, 0], [1, 0]]"
    ],
    "answer": 0
   },
   {
    "code": "a = [1, [2, 3]]\nb = a.copy()\nb[1].append(4)\nb[0] = 9\nprint(a, b)",
    "options": [
     "[1, [2, 3]] [9, [2, 3, 4]]",
     "[9, [2, 3, 4]] [9, [2, 3, 4]]",
     "[1, [2, 3, 4]] [9, [2, 3, 4]]",
     "[1, [2, 3]] [9, [2, 3]]"
    ],
    "answer": 2
   },
   {
    "code": "s = \"  a-b - c  \"\nprint(s.strip().split(\"-\"))",
    "options": [
     "['a', 'b', 'c']",
     "['a', 'b ', ' c']",
     "['a', 'b', ' c']",
     "['  a', 'b ', ' c  ']"
    ],
    "answer": 1
   },
   {
    "code": "x = [1, 2, 3]\ny = x\nx += [4]\ny = y + [5]\nprint(x, y)",
    "options": [
     "[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]",
     "[1, 2, 3] [1, 2, 3, 5]",
     "[1, 2, 3, 4] [1, 2, 3, 5]",
     "[1, 2, 3, 4] [1, 2, 3, 4, 5]"
    ],
    "answer": 3
   }
  ],
  "8": [
   {
    "code": "import math\nprint(math.sqrt(16))",
    "options": [
     "4",
     "4.0",
     "16",
     "Greska"
    ],
    "answer": 1
   },
   {
    "code": "import math\nprint(math.floor(3.9))",
    "options": [
     "4",
     "3",
     "3.9",
     "3.0"
    ],
    "answer": 1
   },
   {
    "code": "import math\nprint(math.floor(-2.5), math.ceil(-2.5), int(-2.5), round(-2.5))",
    "options": [
     "-2 -3 -2 -3",
     "-3 -2 -3 -3",
     "-3 -2 -2 -2",
     "-3 -3 -2 -2"
    ],
    "answer": 2
   },
   {
    "code": "import math\nprint(math.sqrt(16) == 4, type(math.sqrt(16)).__name__, math.isqrt(17))",
    "options": [
     "True int 4",
     "True float 4.0",
     "False float 4",
     "True float 4"
    ],
    "answer": 3
   },
   {
    "code": "from math import *\nprint(pow(2, 3), math.pow(2, 3))",
    "options": [
     "8 8.0",
     "NameError",
     "8.0 8.0",
     "8 8"
    ],
    "answer": 1
   },
   {
    "code": "import math\nprint(math.comb(5, 2), math.perm(5, 2), math.gcd(12, 18), math.factorial(0))",
    "options": [
     "10 20 6 1",
     "10 10 6 0",
     "20 10 6 1",
     "10 20 36 1"
    ],
    "answer": 0
   }
  ],
  "9": [
   {
    "code": "t = (1, 2, 3)\nt[0] = 5",
    "options": [
     "(5, 2, 3)",
     "Greska (TypeError)",
     "[5, 2, 3]",
     "None"
    ],
    "answer": 1
   },
   {
    "code": "s = {1, 2, 2, 3}\nprint(len(s))",
    "options": [
     "4",
     "3",
     "2",
     "Greska"
    ],
    "answer": 1
   },
   {
    "code": "d = {1: \"a\", 1.0: \"b\", True: \"c\"}\nprint(d, len(d))",
    "options": [
     "{1: 'a', 1.0: 'b', True: 'c'} 3",
     "{1: 'a'} 1",
     "{1: 'c'} 1",
     "{1: 'c', True: 'c'} 2"
    ],
    "answer": 2
   },
   {
    "code": "a = {1, 2, 3}\nb = {3, 4}\nprint(a | b, a & b, a - b, a ^ b)",
    "options": [
     "{1, 2, 3, 4} {3} {1, 2, 3} {1, 2, 4}",
     "{1, 2, 3, 4} {3} {1, 2} {1, 2, 4}",
     "{1, 2, 3, 4} {3, 4} {1, 2} {1, 2, 4}",
     "{3} {1, 2, 3, 4} {1, 2} {1, 2, 4}"
    ],
    "answer": 1
   },
   {
    "code": "d = {\"a\": 1}\nd.setdefault(\"a\", 5)\nd.setdefault(\"b\", 7)\nd.update({\"a\": 9})\nprint(d, d.get(\"c\"), len(d))",
    "options": [
     "{'a': 9, 'b': 7} None 2",
     "{'a': 5, 'b': 7} None 2",
     "{'a': 9, 'b': 7} 0 2",
     "{'a': 1, 'b': 7} None 2"
    ],
    "answer": 0
   },
   {
    "code": "d = {}\nd[(1, 2)] = \"t\"\nd[[1, 2]] = \"l\"\nprint(d)",
    "options": [
     "{(1, 2): 't', [1, 2]: 'l'}",
     "KeyError",
     "{(1, 2): 'l'}",
     "TypeError"
    ],
    "answer": 3
   }
  ],
  "10": [
   {
    "code": "x = 5\nif x > 3:\n    print('A')\nelse:\n    print('B')",
    "options": [
     "A",
     "B",
     "A\\nB",
     "Greska"
    ],
    "answer": 0
   },
   {
    "code": "x = 10\nif x < 5:\n    print('Malo')\nelif x < 15:\n    print('Srednje')\nelse:\n    print('Veliko')",
    "options": [
     "Malo",
     "Srednje",
     "Veliko",
     "Greska"
    ],
    "answer": 1
   },
   {
    "code": "x = 15\nif x % 3 == 0:\n    print(\"A\")\nelif x % 5 == 0:\n    print(\"B\")\nif x > 10:\n    print(\"C\")\nelse:\n    print(\"D\")",
    "options": [
     "A\nB\nC",
     "A\nC",
     "A\nD",
     "B\nC"
    ],
    "answer": 1
   },
   {
    "code": "a, b = 4, 0\nprint(a > 3 or a / b > 1, b != 0 and a / b > 1)",
    "options": [
     "True False",
     "Greska (ZeroDivisionError)",
     "True True",
     "False False"
    ],
    "answer": 0
   },
   {
    "code": "x = \"\"\ny = [0]\nprint(\"A\" if x else \"B\", \"C\" if y else \"D\", \"E\" if not y[0] else \"F\")",
    "options": [
     "A C E",
     "B D F",
     "B C F",
     "B C E"
    ],
    "answer": 3
   },
   {
    "code": "n = -5\nprint(\"a\" if n > 0 else \"b\" if n > -10 else \"c\")",
    "options": [
     "a",
     "c",
     "b",
     "Greska (SyntaxError)"
    ],
    "answer": 2
   }
  ],
  "11": [
   {
    "code": "for i in range(3):\n    print(i, end=' ')",
    "options": [
     "0 1 2 ",
     "1 2 3 ",
     "0 1 2 3 ",
     "Greska"
    ],
    "answer": 0
   },
   {
    "code": "i = 0\nwhile i < 3:\n    i += 1\nprint(i)",
    "options": [
     "0",
     "2",
     "3",
     "Greska (beskonacna)"
    ],
    "answer": 2
   },
   {
    "code": "s = 0\nfor i in range(1, 10, 3):\n    s += i\nprint(i, s)",
    "options": [
     "10 12",
     "7 22",
     "7 12",
     "9 12"
    ],
    "answer": 2
   },
   {
    "code": "i = 0\nwhile i < 5:\n    i += 1\n    if i % 2 == 0:\n        continue\n    if i == 5:\n        break\n    print(i, end=\" \")\nelse:\n    print(\"kraj\")",
    "options": [
     "1 3 5 ",
     "1 3 kraj",
     "1 3 5 kraj",
     "1 3 "
    ],
    "answer": 3
   },
   {
    "code": "n = 0\nfor i in range(4):\n    for j in range(i):\n        n += 1\nprint(n)",
    "options": [
     "6",
     "10",
     "4",
     "3"
    ],
    "answer": 0
   },
   {
    "code": "for i in range(3):\n    print(i, end=\" \")\n    i = 10\nprint(i)",
    "options": [
     "0 1 2 2",
     "0 1 2 10",
     "0 10 10 10",
     "Greska (SyntaxError)"
    ],
    "answer": 1
   }
  ],
  "12": [
   {
    "code": "def f(x):\n    return x * 2\nprint(f(5))",
    "options": [
     "5",
     "10",
     "25",
     "Greska"
    ],
    "answer": 1
   },
   {
    "code": "def f(x, y=2):\n    return x + y\nprint(f(3))",
    "options": [
     "3",
     "5",
     "Greska",
     "32"
    ],
    "answer": 1
   },
   {
    "code": "def f(a, b=[]):\n    b.append(a)\n    return b\nf(1)\nf(2)\nprint(f(3))",
    "options": [
     "[3]",
     "[1, 2]",
     "[1, 2, 3, 3]",
     "[1, 2, 3]"
    ],
    "answer": 3
   },
   {
    "code": "x = 1\ndef f():\n    print(x)\n    x = 2\nf()",
    "options": [
     "UnboundLocalError",
     "1",
     "2",
     "NameError"
    ],
    "answer": 0
   },
   {
    "code": "def f(a, *args, **kw):\n    return a, len(args), sorted(kw)\nprint(f(1, 2, 3, x=4, y=5))",
    "options": [
     "(1, 3, ['x', 'y'])",
     "(1, 2, 2)",
     "(1, 2, ['x', 'y'])",
     "(1, 2, {'x': 4, 'y': 5})"
    ],
    "answer": 2
   },
   {
    "code": "def g(n):\n    if n <= 1:\n        return 1\n    return n * g(n - 1) + g(n - 2)\nprint(g(4))",
    "options": [
     "24",
     "43",
     "40",
     "46"
    ],
    "answer": 1
   }
  ],
  "13": [
   {
    "code": "# Ako fajl 'a.txt' ne postoji, sta radi open('a.txt', 'r')?",
    "options": [
     "Pravi novi fajl",
     "Baca FileNotFoundError",
     "Vraca None",
     "Vraca prazan string"
    ],
    "answer": 1
   },
   {
    "code": "# Koji mod otvara fajl za pisanje i brise prethodni sadrzaj?",
    "options": [
     "'r'",
     "'a'",
     "'w'",
     "'x'"
    ],
    "answer": 2
   },
   {
    "code": "with open(\"t.txt\", \"w\") as f:\n    f.write(\"ab\\ncd\\n\")\nwith open(\"t.txt\") as f:\n    a = f.readline()\n    b = f.read()\nprint(len(a), len(b), a.strip() + b.strip())",
    "options": [
     "3 3 abcd",
     "2 2 abcd",
     "3 2 abcd",
     "3 3 ab cd"
    ],
    "answer": 0
   },
   {
    "code": "with open(\"t.txt\", \"w\") as f:\n    f.write(\"1\\n2\\n3\")\nwith open(\"t.txt\", \"a\") as f:\n    f.write(\"4\")\nwith open(\"t.txt\") as f:\n    print(len(f.readlines()), f.read() == \"\")",
    "options": [
     "4 True",
     "3 True",
     "3 False",
     "4 False"
    ],
    "answer": 1
   },
   {
    "code": "with open(\"t.txt\", \"w\") as f:\n    f.write(\"a\")\n    f.write(\"b\")\nwith open(\"t.txt\", \"w\") as f:\n    pass\nwith open(\"t.txt\") as f:\n    print(repr(f.read()))",
    "options": [
     "'ab'",
     "'a'",
     "''",
     "Greska (FileNotFoundError)"
    ],
    "answer": 2
   },
   {
    "code": "with open(\"t.txt\", \"w\") as f:\n    f.write(\"5\\n10\\n\\n15\")\ns = 0\nwith open(\"t.txt\") as f:\n    for line in f:\n        s += int(line)\nprint(s)",
    "options": [
     "30",
     "15",
     "25",
     "ValueError"
    ],
    "answer": 3
   }
  ],
  "14": [
   {
    "code": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Greska')",
    "options": [
     "Greska",
     "0",
     "1",
     "None"
    ],
    "answer": 0
   },
   {
    "code": "try:\n    int('abc')\nexcept ValueError:\n    print('Lose')\nexcept Exception:\n    print('Sve')",
    "options": [
     "Lose",
     "Sve",
     "Greska",
     "Nista"
    ],
    "answer": 0
   },
   {
    "code": "def f():\n    try:\n        return \"A\"\n    finally:\n        return \"B\"\nprint(f())",
    "options": [
     "A",
     "AB",
     "B",
     "None"
    ],
    "answer": 2
   },
   {
    "code": "try:\n    x = int(\"5\") + int(\"a\")\nexcept (TypeError, ValueError) as e:\n    print(type(e).__name__, x)",
    "options": [
     "NameError",
     "ValueError 5",
     "ValueError None",
     "ValueError"
    ],
    "answer": 0
   },
   {
    "code": "r = []\nfor v in [\"1\", \"x\", \"3\", None]:\n    try:\n        r.append(int(v))\n    except ValueError:\n        r.append(-1)\nprint(r)",
    "options": [
     "[1, -1, 3, -1]",
     "TypeError",
     "[1, -1, 3]",
     "[1, -1, 3, None]"
    ],
    "answer": 1
   },
   {
    "code": "def f(n):\n    try:\n        if n == 0:\n            raise ValueError\n        return 10 / n\n    except ValueError:\n        return \"v\"\n    except ZeroDivisionError:\n        return \"z\"\n    else:\n        return \"e\"\n    finally:\n        print(\"f\", end=\" \")\nprint(f(0), f(5))",
    "options": [
     "f v f 2.0",
     "f f v e",
     "f f z 2.0",
     "f f v 2.0"
    ],
    "answer": 3
   }
  ],
  "15": [
   {
    "code": "class A:\n    pass\na = A()\nprint(type(a).__name__)",
    "options": [
     "A",
     "<class 'A'>",
     "object",
     "Greska"
    ],
    "answer": 0
   },
   {
    "code": "class A:\n    x = 5\n    def f(self):\n        return self.x\na = A()\nprint(a.f())",
    "options": [
     "5",
     "A",
     "Greska",
     "None"
    ],
    "answer": 0
   },
   {
    "code": "class A:\n    n = 0\n    def __init__(self):\n        A.n += 1\n        self.id = A.n\na, b = A(), A()\nprint(a.id, b.id, A.n)",
    "options": [
     "1 1 2",
     "2 2 2",
     "1 2 2",
     "1 2 1"
    ],
    "answer": 2
   },
   {
    "code": "class A:\n    x = []\n    def add(self, v):\n        self.x.append(v)\na, b = A(), A()\na.add(1)\nb.add(2)\nprint(a.x, b.x)",
    "options": [
     "[1] [2]",
     "[1, 2] [1, 2]",
     "[1, 2] [2]",
     "[1] [1, 2]"
    ],
    "answer": 1
   },
   {
    "code": "class A:\n    def f(self):\n        return \"A\"\n    def g(self):\n        return self.f()\nclass B(A):\n    def f(self):\n        return \"B\"\nprint(A().g(), B().g())",
    "options": [
     "A B",
     "A A",
     "B B",
     "B A"
    ],
    "answer": 0
   },
   {
    "code": "class P:\n    def __init__(self, v):\n        self.v = v\n    def __eq__(self, o):\n        return self.v == o.v\nprint(P(1) == P(1), P(1) is P(1), [P(1)] == [P(1)])",
    "options": [
     "False False False",
     "True True True",
     "True False False",
     "True False True"
    ],
    "answer": 3
   }
  ],
  "16": [
   {
    "code": "import re\nprint(re.findall(r'\\d+', 'a1b22c333'))",
    "options": [
     "['1', '2', '3']",
     "['1', '22', '333']",
     "['123']",
     "Greska"
    ],
    "answer": 1
   },
   {
    "code": "import re\nprint(bool(re.match(r'a', 'abc')))",
    "options": [
     "True",
     "False",
     "None",
     "Greska"
    ],
    "answer": 0
   },
   {
    "code": "import re\nprint(re.findall(r\"a.*b\", \"a1b a2b\"), re.findall(r\"a.*?b\", \"a1b a2b\"))",
    "options": [
     "['a1b', 'a2b'] ['a1b', 'a2b']",
     "['a1b a2b'] ['a1b a2b']",
     "['a1b', 'a2b'] ['a1b a2b']",
     "['a1b a2b'] ['a1b', 'a2b']"
    ],
    "answer": 3
   },
   {
    "code": "import re\nm = re.search(r\"(\\d+)-(\\d+)\", \"tel 12-345 i 6-7\")\nprint(m.group(1), m.group(2), m.group(0), m.start())",
    "options": [
     "6 7 6-7 17",
     "12 345 12-345 4",
     "12 345 12-345 0",
     "12 345 12-345 3"
    ],
    "answer": 1
   },
   {
    "code": "import re\nprint(re.sub(r\"(\\w+)@(\\w+)\", r\"\\2 at \\1\", \"ana@mail, bob@net\"))",
    "options": [
     "ana at mail, bob at net",
     "mail ana, net bob",
     "mail at ana, net at bob",
     "mail at ana, bob@net"
    ],
    "answer": 2
   },
   {
    "code": "import re\nprint(bool(re.match(r\"b\", \"abc\")), bool(re.search(r\"b\", \"abc\")), bool(re.fullmatch(r\"ab\", \"abc\")), re.split(r\"\\d\", \"a1b22c\"))",
    "options": [
     "False True False ['a', 'b', '', 'c']",
     "True True False ['a', 'b', 'c']",
     "False True True ['a', 'b', '', 'c']",
     "False True False ['a', 'b', 'c']"
    ],
    "answer": 0
   }
  ],
  "17": [
   {
    "code": "import numpy as np\na = np.array([1, 2, 3])\nprint(a * 2)",
    "options": [
     "[2, 4, 6]",
     "Greska",
     "[1, 2, 3, 1, 2, 3]",
     "[2 4 6]"
    ],
    "answer": 3
   },
   {
    "code": "import numpy as np\nprint(np.zeros(3))",
    "options": [
     "[0, 0, 0]",
     "[0. 0. 0.]",
     "Greska",
     "[0 0 0]"
    ],
    "answer": 1
   },
   {
    "code": "import numpy as np\na = np.array([1, 2, 3])\nb = a\nb[0] = 9\nc = a.copy()\nc[1] = 8\nprint(a, c)",
    "options": [
     "[1 2 3] [1 8 3]",
     "[9 2 3] [1 8 3]",
     "[9 2 3] [9 8 3]",
     "[9 8 3] [9 8 3]"
    ],
    "answer": 2
   },
   {
    "code": "import numpy as np\na = np.array([[1, 2, 3], [4, 5, 6]])\nprint(a.sum(axis=0), a.sum(axis=1), a[:, 1])",
    "options": [
     "[ 6 15] [5 7 9] [2 5]",
     "[5 7 9] [ 6 15] [4 5 6]",
     "[5 7 9] [ 6 15] [1 2 3]",
     "[5 7 9] [ 6 15] [2 5]"
    ],
    "answer": 3
   },
   {
    "code": "import numpy as np\na = np.array([1, 2, 3, 4, 5, 6])\nprint(a[a % 2 == 0] * 2, a.reshape(2, 3).shape, (a > 3).sum())",
    "options": [
     "[ 4  8 12] (2, 3) 3",
     "[2 4 6] (2, 3) 3",
     "[ 4  8 12] (3, 2) 3",
     "[ 4  8 12] (2, 3) 2"
    ],
    "answer": 0
   },
   {
    "code": "import numpy as np\na = np.array([[1], [2], [3]])\nb = np.array([10, 20])\nprint((a + b).shape, (a * b)[2])",
    "options": [
     "(3, 1) [30 60]",
     "(3, 2) [30 60]",
     "(3, 2) [3 6]",
     "Greska (ValueError)"
    ],
    "answer": 1
   }
  ],
  "18": [
   {
    "code": "import matplotlib.pyplot as plt\n# Koja funkcija crta linijski grafik?",
    "options": [
     "plt.plot()",
     "plt.line()",
     "plt.draw()",
     "plt.show()"
    ],
    "answer": 0
   },
   {
    "code": "import matplotlib.pyplot as plt\n# Koja funkcija prikazuje grafik na ekranu?",
    "options": [
     "plt.show()",
     "plt.display()",
     "plt.render()",
     "plt.plot()"
    ],
    "answer": 0
   },
   {
    "code": "import matplotlib.pyplot as plt\nfig, ax = plt.subplots(1, 3)\nprint(type(ax).__name__, len(ax))",
    "options": [
     "list 3",
     "ndarray 3",
     "Axes 3",
     "tuple 3"
    ],
    "answer": 1
   },
   {
    "code": "import matplotlib.pyplot as plt\nplt.plot([1, 2, 3])\nplt.figure()\nplt.plot([4, 5])\nplt.plot([6, 7])\nprint(len(plt.gca().lines), len(plt.get_fignums()))",
    "options": [
     "3 1",
     "3 2",
     "2 1",
     "2 2"
    ],
    "answer": 3
   },
   {
    "code": "import matplotlib.pyplot as plt\nx = [1, 2, 3]\nplt.bar(x, [5, 6, 7], label=\"A\")\nplt.bar(x, [1, 1, 1], bottom=[5, 6, 7], label=\"B\")\nplt.legend()\nprint(len(plt.gca().patches), [t.get_text() for t in plt.gca().get_legend().get_texts()])",
    "options": [
     "3 ['A', 'B']",
     "6 ['B', 'A']",
     "6 ['A', 'B']",
     "2 ['A', 'B']"
    ],
    "answer": 2
   },
   {
    "code": "import matplotlib.pyplot as plt\nplt.plot([1, 2], [3, 4])\nplt.xlim(0, 10)\nplt.title(\"T\")\nprint(plt.gca().get_xlim()[1], plt.gca().get_title())",
    "options": [
     "10.0 T",
     "2.0 T",
     "10 T",
     "10.0"
    ],
    "answer": 0
   }
  ],
  "19": [
   {
    "code": "# Cemu sluzi Monte Karlo simulacija?",
    "options": [
     "Tacnom izracunavanju",
     "Modeliranju neizvesnosti",
     "Sortiranju podataka",
     "Pravljenju grafikona"
    ],
    "answer": 1
   },
   {
    "code": "import random\nrandom.seed(42)\nprint(random.random() == random.random())",
    "options": [
     "True",
     "False",
     "Greska",
     "None"
    ],
    "answer": 1
   },
   {
    "code": "import random\nrandom.seed(1)\na = random.random()\nrandom.seed(1)\nb = random.random()\nprint(a == b, random.random() == a)",
    "options": [
     "True True",
     "True False",
     "False False",
     "False True"
    ],
    "answer": 1
   },
   {
    "code": "# Kockicu bacamo 3600 puta.\n# Koliko puta ocekujemo sesticu i sta vazi za odstupanje?",
    "options": [
     "Oko 600; relativno odstupanje opada sa vecim brojem bacanja",
     "Tacno 600 puta, ako je kockica fer",
     "Oko 600; apsolutno odstupanje opada sa vecim brojem bacanja",
     "Oko 360; odstupanje je uvek isto"
    ],
    "answer": 0
   },
   {
    "code": "import random\nrandom.seed(5)\nn = 0\nfor _ in range(1000):\n    x, y = random.random(), random.random()\n    if x * x + y * y < 1:\n        n += 1\n# Cemu je priblizno jednako n / 1000?",
    "options": [
     "pi",
     "pi / 2",
     "pi / 4",
     "1 / pi"
    ],
    "answer": 2
   },
   {
    "code": "import random\nrandom.seed(3)\nn = 0\nfor _ in range(60000):\n    if random.randint(1, 6) + random.randint(1, 6) == 7:\n        n += 1\n# Sta je najblize vrednosti n / 60000?",
    "options": [
     "0.143 (1/7)",
     "0.250 (1/4)",
     "0.083 (1/12)",
     "0.167 (1/6)"
    ],
    "answer": 3
   }
  ],
  "20": [
   {
    "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})\nprint(df.shape)",
    "options": [
     "(2, 2)",
     "(4,)",
     "2",
     "Greska"
    ],
    "answer": 0
   },
   {
    "code": "import pandas as pd\ns = pd.Series([10, 20, 30])\nprint(s.mean())",
    "options": [
     "10",
     "20.0",
     "60",
     "Greska"
    ],
    "answer": 1
   },
   {
    "code": "import pandas as pd\ns = pd.Series([10, 20, 30], index=[\"a\", \"b\", \"c\"])\nprint(s[\"b\"], s.iloc[2], s[\"a\":\"b\"].sum())",
    "options": [
     "20 30 10",
     "20 20 10",
     "10 30 30",
     "20 30 30"
    ],
    "answer": 3
   },
   {
    "code": "import pandas as pd\ndf = pd.DataFrame({\"g\": [\"x\", \"y\", \"x\", \"y\"], \"v\": [1, 2, 3, 4]})\nprint(df.groupby(\"g\")[\"v\"].sum().tolist(), df[df[\"v\"] > 1][\"g\"].nunique())",
    "options": [
     "[4, 6] 3",
     "[4, 6] 2",
     "[2, 2] 2",
     "[1, 2] 2"
    ],
    "answer": 1
   },
   {
    "code": "import pandas as pd\ndf = pd.DataFrame({\"a\": [1, None, 3], \"b\": [4, 5, None]})\nprint(df.isnull().sum().tolist(), df.dropna().shape, df.fillna(0)[\"a\"].sum())",
    "options": [
     "[1, 1] (2, 2) 4.0",
     "[2, 1] (1, 2) 4.0",
     "[1, 1] (1, 2) 4.0",
     "[1, 1] (1, 2) 4"
    ],
    "answer": 2
   },
   {
    "code": "import pandas as pd\ndf = pd.DataFrame({\"x\": [3, 1, 2]})\ndf2 = df.sort_values(\"x\")\nprint(df2.index.tolist(), df2.iloc[0, 0], df2.loc[0, \"x\"], df.index.tolist())",
    "options": [
     "[1, 2, 0] 1 3 [0, 1, 2]",
     "[1, 2, 0] 1 1 [0, 1, 2]",
     "[0, 1, 2] 1 3 [0, 1, 2]",
     "[1, 2, 0] 3 3 [1, 2, 0]"
    ],
    "answer": 0
   }
  ],
  "21": [
   {
    "code": "from scipy.optimize import minimize\n# Cemu sluzi minimize()?",
    "options": [
     "Trazenju minimuma funkcije",
     "Maksimizaciji",
     "Sortiranju",
     "Integraciji"
    ],
    "answer": 0
   },
   {
    "code": "from scipy.optimize import minimize\n# Sta je 'x0' u minimize()?",
    "options": [
     "Pocetna tacka",
     "Rezultat",
     "Funkcija",
     "Greska"
    ],
    "answer": 0
   },
   {
    "code": "from scipy.optimize import minimize\nres = minimize(lambda x: (x[0] - 1)**2 + (x[1] - 2)**2, x0=[5, 5])\nprint(round(res.x[0]), round(res.x[1]), round(res.fun), res.success)",
    "options": [
     "5 5 0 True",
     "1 2 0 True",
     "1 2 5 True",
     "2 1 0 True"
    ],
    "answer": 1
   },
   {
    "code": "from scipy.optimize import minimize\nres = minimize(lambda x: -(-x[0]**2 + 4*x[0]), x0=[0])\nprint(round(res.x[0], 1), round(-res.fun, 1))",
    "options": [
     "2.0 4.0",
     "2.0 -4.0",
     "4.0 2.0",
     "-2.0 4.0"
    ],
    "answer": 0
   },
   {
    "code": "from scipy.optimize import minimize\nres = minimize(lambda x: (x[0] - 5)**2, x0=[0], bounds=[(0, 3)])\nprint(round(res.x[0], 1), round(res.fun, 1))",
    "options": [
     "5.0 0.0",
     "3.0 0.0",
     "3.0 4.0",
     "0.0 25.0"
    ],
    "answer": 2
   },
   {
    "code": "from scipy.optimize import minimize\ncons = {\"type\": \"eq\", \"fun\": lambda v: v[0] + v[1] - 2}\nres = minimize(lambda v: v[0]**2 + v[1]**2, x0=[0, 0], constraints=cons)\nprint(round(res.x[0], 1), round(res.x[1], 1), round(res.fun, 1))",
    "options": [
     "0.0 0.0 0.0",
     "2.0 0.0 4.0",
     "1.0 1.0 1.0",
     "1.0 1.0 2.0"
    ],
    "answer": 3
   }
  ],
  "22": [
   {
    "code": "# Sta je masinsko ucenje?",
    "options": [
     "Rucno pisanje pravila",
     "Ucenje iz podataka",
     "Baza podataka",
     "Vrsta programa"
    ],
    "answer": 1
   },
   {
    "code": "# Sta je 'feature' u masinskom ucenju?",
    "options": [
     "Ciljna promenljiva",
     "Ulazna promenljiva",
     "Greska modela",
     "Algoritam"
    ],
    "answer": 1
   },
   {
    "code": "from sklearn.model_selection import train_test_split\nX = list(range(10))\ny = [i % 2 for i in X]\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=1)\nprint(len(X_tr), len(X_te), sorted(X_tr + X_te) == X)",
    "options": [
     "7 3 True",
     "3 7 True",
     "7 3 False",
     "10 3 True"
    ],
    "answer": 0
   },
   {
    "code": "# Model: 99% tacnosti na trening skupu, 62% na test skupu.\n# Sta je najverovatniji problem?",
    "options": [
     "Underfitting, jer model nije naucio podatke",
     "Overfitting: model je zapamtio trening podatke",
     "Test skup je premali da bi se racunala tacnost",
     "Model ima previse klasa za predvidjanje"
    ],
    "answer": 1
   },
   {
    "code": "# Skup: 95% primera klase A i 5% klase B.\n# Model uvek predvidja A. Koliko iznosi njegova tacnost?",
    "options": [
     "5%, jer model uvek pogadja pogresnu klasu",
     "50%, jer postoje samo dve klase",
     "100%, jer je klasa A vecinska u skupu",
     "95%, ali ne pronalazi nijedan primer klase B"
    ],
    "answer": 3
   },
   {
    "code": "# StandardScaler je fitovan na CELOM skupu pre podele na trening i test.\n# Sta je problem?",
    "options": [
     "Nema problema, skaliranje je uvek bezbedno",
     "Model ce raditi znatno sporije nego inace",
     "Curenje informacija: test podaci uticu na trening",
     "Skaliranje se sme raditi samo na test skupu"
    ],
    "answer": 2
   }
  ],
  "23": [
   {
    "code": "# Zasto se zove 'naivni' Bajes?",
    "options": [
     "Zato sto je algoritam glup",
     "Zato sto pretpostavlja nezavisnost atributa",
     "Zato sto ne radi sa brojevima",
     "Zato sto je brz"
    ],
    "answer": 1
   },
   {
    "code": "# Koja je osnovna teorema na kojoj se zasniva?",
    "options": [
     "Pitagorina",
     "Bajesova teorema",
     "Njutnova",
     "Bolcmanova"
    ],
    "answer": 1
   },
   {
    "code": "from sklearn.naive_bayes import GaussianNB\nX = [[1], [2], [8], [9]]\ny = [0, 0, 1, 1]\nclf = GaussianNB().fit(X, y)\nprint(clf.predict([[0]]), clf.predict([[10]]), clf.predict_proba([[1.5]]).argmax())",
    "options": [
     "[1] [0] 0",
     "[0] [1] 0",
     "[0] [1] 1",
     "[0] [0] 0"
    ],
    "answer": 1
   },
   {
    "code": "# P(bolest) = 0.01, P(+ | bolest) = 0.9, P(+ | zdrav) = 0.09\n# Koliko je priblizno P(bolest | +)?",
    "options": [
     "90%",
     "50%",
     "1%",
     "9%"
    ],
    "answer": 3
   },
   {
    "code": "# P(A) = P(B) = 0.5\n# P(x1|A) = 0.8, P(x2|A) = 0.5\n# P(x1|B) = 0.2, P(x2|B) = 0.4\n# Koja klasa se predvidja za (x1, x2) i s kojom verovatnocom?",
    "options": [
     "A, oko 20%",
     "B, oko 17%",
     "A, oko 83%",
     "A, oko 40%"
    ],
    "answer": 2
   },
   {
    "code": "# Naivna pretpostavka Bajesovog klasifikatora.\n# Koja formula je tacna za dva atributa x1, x2 i klasu C?",
    "options": [
     "P(x1, x2 | C) = P(x1 | C) * P(x2 | C)",
     "P(x1, x2 | C) = P(x1 | C) + P(x2 | C)",
     "P(x1, x2 | C) = P(x1) * P(x2)",
     "P(C | x1, x2) = P(C | x1) * P(C | x2)"
    ],
    "answer": 0
   }
  ],
  "24": [
   {
    "code": "# Kako KNN donosi odluku o klasi novog podatka?",
    "options": [
     "Gleda najblize susede",
     "Gleda sve podatke",
     "Koristi verovatnocu",
     "Gleda samo jedan podatak"
    ],
    "answer": 0
   },
   {
    "code": "# Sta znaci 'K' u KNN?",
    "options": [
     "Broj atributa",
     "Broj suseda",
     "Broj klasa",
     "Broj iteracija"
    ],
    "answer": 1
   },
   {
    "code": "from sklearn.neighbors import KNeighborsClassifier\nX = [[0], [1], [2], [10], [11]]\ny = [0, 0, 0, 1, 1]\nfor k in (1, 3, 5):\n    print(KNeighborsClassifier(n_neighbors=k).fit(X, y).predict([[7]])[0], end=\" \")",
    "options": [
     "1 1 1 ",
     "1 1 0 ",
     "0 0 0 ",
     "1 0 0 "
    ],
    "answer": 1
   },
   {
    "code": "# Novi primer: (starost=30, plata=50000)\n# A: (60, 50500), B: (31, 60000)\n# Euklidska razdaljina, bez skaliranja. Koji je blizi?",
    "options": [
     "A, jer plata dominira rastojanjem",
     "B, jer je starost gotovo ista",
     "Jednako su udaljeni",
     "Ne moze se izracunati bez skaliranja"
    ],
    "answer": 0
   },
   {
    "code": "# KNN sa K = broj svih primera u trening skupu.\n# Sta predvidja za bilo koji novi primer?",
    "options": [
     "Klasu koja je najblizi sused",
     "Nasumicno odabranu klasu iz skupa",
     "Klasu prvog primera u trening skupu",
     "Uvek vecinsku klasu iz trening skupa"
    ],
    "answer": 3
   },
   {
    "code": "from sklearn.neighbors import KNeighborsClassifier\nX = [[1], [2], [3], [4]]\ny = [0, 1, 0, 1]\nclf = KNeighborsClassifier(n_neighbors=1).fit(X, y)\nprint(clf.score(X, y), clf.predict([[2.4]])[0], clf.predict([[3.6]])[0])",
    "options": [
     "0.5 1 1",
     "1.0 0 1",
     "1.0 1 1",
     "1.0 1 0"
    ],
    "answer": 2
   }
  ],
  "25": [
   {
    "code": "# Sta je cvor (node) u stablu odlucivanja?",
    "options": [
     "Mesto gde se donosi odluka",
     "Krajnji rezultat",
     "Grana",
     "Podatak"
    ],
    "answer": 0
   },
   {
    "code": "# Koja metrika se cesto koristi za podelu u stablu?",
    "options": [
     "Euklidska distanca",
     "Dzinijev indeks ili informaciona dobit",
     "Kosinusna slicnost",
     "Bajes"
    ],
    "answer": 1
   },
   {
    "code": "# Cvor ima 10 primera: 6 klase A i 4 klase B.\n# Koliko iznosi Dzinijeva necistoca cvora?",
    "options": [
     "0.52",
     "0.48",
     "0.24",
     "0.40"
    ],
    "answer": 1
   },
   {
    "code": "# Roditelj: 10 primera (5 A, 5 B). Deli se na:\n# levi cvor: 4 A + 1 B, desni cvor: 1 A + 4 B.\n# Tezinski Dzini posle podele iznosi:",
    "options": [
     "0.50",
     "0.16",
     "0.32",
     "0.64"
    ],
    "answer": 2
   },
   {
    "code": "from sklearn.tree import DecisionTreeClassifier\nX = [[0], [1], [2], [3], [4], [5]]\ny = [0, 0, 0, 1, 1, 1]\nclf = DecisionTreeClassifier(max_depth=1).fit(X, y)\nprint(clf.tree_.threshold[0], clf.predict([[2.4], [2.6]]))",
    "options": [
     "3.0 [0 1]",
     "2.5 [0 0]",
     "2.0 [0 1]",
     "2.5 [0 1]"
    ],
    "answer": 3
   },
   {
    "code": "# Stablo bez ogranicenja dubine: 100% tacnosti na treningu, 70% na testu.\n# Sta najverovatnije pomaze?",
    "options": [
     "Smanjiti max_depth ili povecati min_samples_leaf",
     "Povecati max_depth da bi stablo naucilo vise",
     "Izbaciti test skup iz procene modela",
     "Dodati jos atributa koji sadrze samo sum"
    ],
    "answer": 0
   }
  ],
  "26": [
   {
    "code": "# Sta je ansambl u masinskom ucenju?",
    "options": [
     "Jedan veoma veliki model",
     "Kombinacija vise modela radi boljeg rezultata",
     "Skup podataka",
     "Vrsta greske"
    ],
    "answer": 1
   },
   {
    "code": "# Random Forest je ansambl:",
    "options": [
     "Linearnih regresija",
     "Stabla odlucivanja",
     "KNN modela",
     "Naivnih Bajesa"
    ],
    "answer": 1
   },
   {
    "code": "# Tri modela, verovatnoce za klasu A: 0.9, 0.4, 0.45.\n# Uporedi tvrdo (vecinsko) i meko (prosek verovatnoca) glasanje.",
    "options": [
     "Tvrdo daje A, meko daje B",
     "Tvrdo daje B, meko daje A",
     "Oba daju A",
     "Oba daju B"
    ],
    "answer": 1
   },
   {
    "code": "from sklearn.ensemble import RandomForestClassifier\nclf = RandomForestClassifier(n_estimators=50, random_state=0).fit([[0], [1], [2], [3]], [0, 0, 1, 1])\np = clf.predict_proba([[0]])\nprint(len(clf.estimators_), p.shape, round(p.sum(), 2))",
    "options": [
     "50 (2,) 1.0",
     "4 (1, 2) 1.0",
     "50 (1, 2) 1.0",
     "50 (1, 2) 2.0"
    ],
    "answer": 2
   },
   {
    "code": "# Bootstrap uzorak velicine n izvlaci se sa ponavljanjem iz skupa od n primera.\n# Priblizno koji deo originalnih primera se nalazi u uzorku (n veliko)?",
    "options": [
     "Oko 50%",
     "Oko 37%",
     "100%",
     "Oko 63%"
    ],
    "answer": 3
   },
   {
    "code": "# Koja tvrdnja o baggingu i boostingu je tacna?",
    "options": [
     "Bagging smanjuje varijansu (paralelno), boosting ispravlja greske (redom)",
     "Bagging trenira modele redom, a boosting ih trenira paralelno",
     "Boosting uvek trenira jedan model vise puta na istim podacima",
     "Oba metoda treniraju modele paralelno na istim podacima"
    ],
    "answer": 0
   }
  ]
 },
 "code": {
  "1": [
   {
    "text": "Ispisi tekst: Hello, world!",
    "expected": "Hello, world!",
    "starter": ""
   },
   {
    "text": "Ispisi rezultat izraza 12 + 30.",
    "expected": "42",
    "starter": ""
   },
   {
    "text": "Napravi promenljivu ime sa vrednoscu \"Ana\" i ispisi je.",
    "expected": "Ana",
    "starter": "ime = "
   },
   {
    "text": "Ispisi dva reda: Python, pa u drugom redu rocks (dva poziva print).",
    "expected": "Python\nrocks",
    "starter": ""
   },
   {
    "text": "Promenljive a = 6 i b = 9 su vec napravljene. Ispisi njihov proizvod.",
    "expected": "54",
    "starter": "a = 6\nb = 9\n"
   },
   {
    "text": "Ispisi prosek brojeva 4, 8 i 12 (koristi deljenje).",
    "expected": "8.0",
    "starter": ""
   }
  ],
  "2": [
   {
    "text": "Ispisi tekst: Ja ucim Python",
    "expected": "Ja ucim Python",
    "starter": ""
   },
   {
    "text": "Jednim pozivom print ispisi brojeve 1 2 3 odvojene razmakom (tri argumenta).",
    "expected": "1 2 3",
    "starter": ""
   },
   {
    "text": "Ispisi A-B-C koristeci parametar sep.",
    "expected": "A-B-C",
    "starter": ""
   },
   {
    "text": "Ispisi Hello World u jednom redu pomocu dva poziva print (koristi end).",
    "expected": "Hello World",
    "starter": ""
   },
   {
    "text": "Jednim pozivom print ispisi dva reda: Red, pa Blue (koristi \\n).",
    "expected": "Red\nBlue",
    "starter": ""
   },
   {
    "text": "Ispisi tekst sa navodnicima: \"Ana\"",
    "expected": "\"Ana\"",
    "starter": ""
   }
  ],
  "3": [
   {
    "text": "Ispisi ostatak pri deljenju 17 sa 5.",
    "expected": "2",
    "starter": ""
   },
   {
    "text": "Ispisi 3 na cetvrti stepen.",
    "expected": "81",
    "starter": ""
   },
   {
    "text": "Ispisi celobrojni kolicnik brojeva 25 i 4.",
    "expected": "6",
    "starter": ""
   },
   {
    "text": "Napravi promenljivu price = 19.99 i ispisi njen tip.",
    "expected": "<class 'float'>",
    "starter": ""
   },
   {
    "text": "Pretvori string \"250\" u broj i ispisi njegovu dvostruku vrednost.",
    "expected": "500",
    "starter": ""
   },
   {
    "text": "Ispisi rezultat izraza (8 + 2) * 5 - 3.",
    "expected": "47",
    "starter": ""
   }
  ],
  "4": [
   {
    "text": "Ispisi da li je 7 vece od 9.",
    "expected": "False",
    "starter": ""
   },
   {
    "text": "Ispisi True ako je 15 deljivo sa 3 (koristi %).",
    "expected": "True",
    "starter": ""
   },
   {
    "text": "Neka je x = 5. Ispisi da li je x vece od 1 i manje od 10.",
    "expected": "True",
    "starter": "x = 5\n"
   },
   {
    "text": "U jednom redu ispisi bool(0) i bool(7), odvojene razmakom.",
    "expected": "False True",
    "starter": ""
   },
   {
    "text": "Ispisi rezultat izraza not True.",
    "expected": "False",
    "starter": ""
   },
   {
    "text": "Ispisi da li su \"a\" i \"b\" razliciti (koristi !=).",
    "expected": "True",
    "starter": ""
   }
  ],
  "5": [
   {
    "text": "Ispisi prvo slovo reci \"Beograd\".",
    "expected": "B",
    "starter": ""
   },
   {
    "text": "Ispisi poslednje slovo reci \"Beograd\".",
    "expected": "d",
    "starter": ""
   },
   {
    "text": "Ispisi \"banana\" velikim slovima.",
    "expected": "BANANA",
    "starter": ""
   },
   {
    "text": "Ispisi rec \"hello\" ponovljenu 3 puta, bez razmaka.",
    "expected": "hellohellohello",
    "starter": ""
   },
   {
    "text": "Promenljive name i age su vec napravljene. Pomocu f-stringa ispisi: Ana ima 20 godina",
    "expected": "Ana ima 20 godina",
    "starter": "name = \"Ana\"\nage = 20\n"
   },
   {
    "text": "Ispisi duzinu reci \"programiranje\".",
    "expected": "13",
    "starter": ""
   }
  ],
  "6": [
   {
    "text": "Ispisi listu [4, 8, 15].",
    "expected": "[4, 8, 15]",
    "starter": ""
   },
   {
    "text": "Lista a = [1, 2, 3] je napravljena. Dodaj joj broj 10 i ispisi listu.",
    "expected": "[1, 2, 3, 10]",
    "starter": "a = [1, 2, 3]\n"
   },
   {
    "text": "Ispisi zbir elemenata liste [5, 10, 15, 20].",
    "expected": "50",
    "starter": ""
   },
   {
    "text": "Ispisi najveci broj u listi [3, 9, 2, 7].",
    "expected": "9",
    "starter": ""
   },
   {
    "text": "Ispisi listu [5, 2, 9, 1] sortiranu rastuce.",
    "expected": "[1, 2, 5, 9]",
    "starter": "a = [5, 2, 9, 1]\n"
   },
   {
    "text": "Ispisi poslednji element liste [10, 20, 30, 40].",
    "expected": "40",
    "starter": ""
   }
  ],
  "7": [
   {
    "text": "Razdvoji \"jabuka,kruska,sljiva\" po zarezu i ispisi dobijenu listu.",
    "expected": "['jabuka', 'kruska', 'sljiva']",
    "starter": ""
   },
   {
    "text": "Spoji listu [\"a\", \"b\", \"c\"] razmakom i ispisi rezultat.",
    "expected": "a b c",
    "starter": ""
   },
   {
    "text": "Ispisi \"  Beograd  \" bez razmaka sa strana (koristi strip).",
    "expected": "Beograd",
    "starter": ""
   },
   {
    "text": "Lista m = [[1, 2], [3, 4]] je napravljena. Ispisi broj 4.",
    "expected": "4",
    "starter": "m = [[1, 2], [3, 4]]\n"
   },
   {
    "text": "Ispisi rec \"programiranje\" unazad (isecanjem).",
    "expected": "ejnarimargorp",
    "starter": ""
   },
   {
    "text": "Iz liste [1, 2, 3, 4, 5, 6] ispisi svaki drugi element (isecanje sa korakom).",
    "expected": "[1, 3, 5]",
    "starter": "a = [1, 2, 3, 4, 5, 6]\n"
   }
  ],
  "8": [
   {
    "text": "Uvezi math i ispisi kvadratni koren iz 81.",
    "expected": "9.0",
    "starter": ""
   },
   {
    "text": "Ispisi 7.8 zaokruzeno nadole pomocu math.floor.",
    "expected": "7",
    "starter": ""
   },
   {
    "text": "Ispisi 6! (faktorijel) pomocu modula math.",
    "expected": "720",
    "starter": ""
   },
   {
    "text": "Ispisi na koliko nacina se mogu izabrati 2 stvari od 5 (math.comb).",
    "expected": "10",
    "starter": ""
   },
   {
    "text": "Ispisi broj pi iz modula math zaokruzen na 3 decimale.",
    "expected": "3.142",
    "starter": ""
   },
   {
    "text": "Uvezi math pod imenom m i ispisi m.ceil(4.2).",
    "expected": "5",
    "starter": ""
   }
  ],
  "9": [
   {
    "text": "Napravi torku sa brojevima 5, 10, 15 i ispisi njen drugi element.",
    "expected": "10",
    "starter": ""
   },
   {
    "text": "Data je lista a = [1, 2, 2, 3, 4, 4, 4]. Pretvori je u skup i ispisi duzinu tog skupa.",
    "expected": "4",
    "starter": "a = [1, 2, 2, 3, 4, 4, 4]\n"
   },
   {
    "text": "Recnik d = {'ime': 'Ana', 'godine': 20} je napravljen. Ispisi vrednost za kljuc 'godine'.",
    "expected": "20",
    "starter": "d = {'ime': 'Ana', 'godine': 20}\n"
   },
   {
    "text": "Napravi dva skupa a = {1, 2, 3} i b = {3, 4, 5}. Ispisi njihov presek (zajednicke elemente).",
    "expected": "{3}",
    "starter": "a = {1, 2, 3}\nb = {3, 4, 5}\n"
   },
   {
    "text": "Data su dva recnika: d1 = {'a': 1} i d2 = {'b': 2}. Spoji ih u jedan i ispisi.",
    "expected": "{'a': 1, 'b': 2}",
    "starter": "d1 = {'a': 1}\nd2 = {'b': 2}\n"
   },
   {
    "text": "Data je lista reci ['ja', 'ucim', 'pajton']. Koristi skup da ispises sve jedinstvene duzine tih reci sortirane rastuce.",
    "expected": "[2, 4, 6]",
    "starter": "reci = ['ja', 'ucim', 'pajton']\n"
   }
  ],
  "10": [
   {
    "text": "Neka je broj = 7. Ako je broj paran ispisi 'Parno', inace ispisi 'Neparno'.",
    "expected": "Neparno",
    "starter": "broj = 7\n"
   },
   {
    "text": "Data su dva broja a = 15 i b = 20. Ispisi veci od njih koristeci if/else.",
    "expected": "20",
    "starter": "a = 15\nb = 20\n"
   },
   {
    "text": "Ocena je 85. Ako je >= 90 ispisi 'A', ako je >= 80 ispisi 'B', inace 'C'.",
    "expected": "B",
    "starter": "ocena = 85\n"
   },
   {
    "text": "Koristi terarni operator da u jednoj liniji ispises 'Punoletan' ako je godine >= 18, inace 'Maloletan'. (godine = 20)",
    "expected": "Punoletan",
    "starter": "godine = 20\n"
   },
   {
    "text": "Data je promenljiva x = 10. Ispisi 'U opsegu' ako je x izmedju 5 i 15 (ukljucujuci granice).",
    "expected": "U opsegu",
    "starter": "x = 10\n"
   },
   {
    "text": "Data je lista brojeva [1, 5, 8, 12, 3]. Koristi if/else da ispises 'Ima parnih' ako u listi postoji bar jedan paran broj, inace 'Nema'.",
    "expected": "Ima parnih",
    "starter": "brojevi = [1, 5, 8, 12, 3]\n"
   }
  ],
  "11": [
   {
    "text": "Koristi for petlju i range da ispises brojeve od 1 do 5 u jednom redu odvojene razmakom.",
    "expected": "1 2 3 4 5",
    "starter": ""
   },
   {
    "text": "Koristi while petlju da ispises brojeve od 5 do 1 u jednom redu odvojene razmakom.",
    "expected": "5 4 3 2 1",
    "starter": ""
   },
   {
    "text": "Data je lista ['a', 'b', 'c']. Koristi for petlju da ispises svaki element u novom redu.",
    "expected": "a\nb\nc",
    "starter": "lista = ['a', 'b', 'c']\n"
   },
   {
    "text": "Ispisi sumu svih parnih brojeva od 1 do 10 koristeci for petlju i if.",
    "expected": "30",
    "starter": ""
   },
   {
    "text": "Data je rec 'Pajton'. Koristi for petlju da ispises svako slovo u novom redu.",
    "expected": "P\na\nj\nt\no\nn",
    "starter": "rec = 'Pajton'\n"
   },
   {
    "text": "Koristi for petlju i funkciju enumerate da ispises indekse i elemente liste ['x', 'y'] u formatu '0: x' i '1: y' (svaki u novom redu).",
    "expected": "0: x\n1: y",
    "starter": "lista = ['x', 'y']\n"
   }
  ],
  "12": [
   {
    "text": "Napravi funkciju kvadriraj(x) koja vraca x na kvadrat. Ispisi kvadriraj(4).",
    "expected": "16",
    "starter": ""
   },
   {
    "text": "Napravi funkciju pozdrav(ime) koja vraca string 'Zdravo, [ime]!'. Ispisi pozdrav('Ana').",
    "expected": "Zdravo, Ana!",
    "starter": ""
   },
   {
    "text": "Napravi funkciju saberi(a, b=10) koja vraca njihov zbir. Ispisi saberi(5) i saberi(5, 2) u dva reda.",
    "expected": "15\n7",
    "starter": ""
   },
   {
    "text": "Napravi funkciju prosek(lista) koja vraca prosek elemenata. Ispisi prosek([2, 4, 6]).",
    "expected": "4.0",
    "starter": ""
   },
   {
    "text": "Napravi funkciju broj_slova(rec) koja vraca broj slova u reci. Ispisi broj_slova('Pajton').",
    "expected": "6",
    "starter": ""
   },
   {
    "text": "Napravi funkciju maksimum(a, b) koja vraca veci broj bez koriscenja max(). Ispisi maksimum(7, 3).",
    "expected": "7",
    "starter": ""
   }
  ],
  "13": [
   {
    "text": "U fajl 'test.txt' upisi tekst 'Zdravo'. Zatim otvori fajl i ispisi njegov sadrzaj.",
    "expected": "Zdravo",
    "starter": ""
   },
   {
    "text": "U fajl 'brojevi.txt' upisi brojeve 1, 2, 3 svaki u novom redu. Zatim ispisi sadrzaj.",
    "expected": "1\n2\n3",
    "starter": ""
   },
   {
    "text": "U fajl 'recenica.txt' upisi 'Python je zabavan'. Zatim ispisi broj karaktera u fajlu.",
    "expected": "17",
    "starter": ""
   },
   {
    "text": "U fajl 'linije.txt' upisi 'A\\nB\\nC'. Zatim ispisi broj linija u fajlu koristeci readlines().",
    "expected": "3",
    "starter": ""
   },
   {
    "text": "U fajl 'dodaj.txt' upisi 'Prva'. Zatim otvori u modu 'a' i dodaj 'Druga'. Ispisi ceo sadrzaj.",
    "expected": "PrvaDruga",
    "starter": ""
   },
   {
    "text": "U fajl 'reci.txt' upisi 'jabuka\\nkruska'. Zatim ispisi svaku liniju velikim slovima (jedna ispod druge).",
    "expected": "JABUKA\nKRUSKA",
    "starter": ""
   }
  ],
  "14": [
   {
    "text": "Koristi try/except da uhvatis deljenje nulom. Ako se desi greska, ispisi 'Deljenje nulom!'. (x = 10, y = 0)",
    "expected": "Deljenje nulom!",
    "starter": "x = 10\ny = 0\n"
   },
   {
    "text": "Data je lista ['a', 'b']. Koristi try/except IndexError da pokusas da pristupis elementu na indeksu 5. Ako ne uspe, ispisi 'Nema elementa'.",
    "expected": "Nema elementa",
    "starter": "lista = ['a', 'b']\n"
   },
   {
    "text": "Koristi try/except ValueError i finally da ispises 'Kraj' bez obzira na sve, nakon sto pokusas int('abc').",
    "expected": "Kraj",
    "starter": ""
   },
   {
    "text": "Koristi try/except KeyError da uhvatis pristup nepostojecem kljucu 'c' u recniku {'a': 1}. Ispisi 'Nema kljuca'.",
    "expected": "Nema kljuca",
    "starter": "d = {'a': 1}\n"
   },
   {
    "text": "Napisi funkciju bezbedno_deli(a, b) koja vraca a/b, ali ako je b=0 vraca None. Ispisi bezbedno_deli(10, 0).",
    "expected": "None",
    "starter": ""
   },
   {
    "text": "Koristi raise ValueError('Greska') unutar try bloka i uhvati ga da ispises 'Uhvaceno'.",
    "expected": "Uhvaceno",
    "starter": ""
   }
  ],
  "15": [
   {
    "text": "Napravi klasu Pas sa metodom __init__ koja postavlja ime, i metodom laj() koja vraca 'Av Av'. Napravi psa sa imenom 'Reks' i ispisi laj().",
    "expected": "Av Av",
    "starter": ""
   },
   {
    "text": "Napravi klasu Krug sa atributom r. Dodaj metod povrsina() koji vraca 3.14 * r * r. Ispisi povrsinu za r=2.",
    "expected": "12.56",
    "starter": ""
   },
   {
    "text": "Napravi klasu Student sa atributima ime i ocena. Napravi dva studenta i ispisi ime onog sa vecom ocenom.",
    "expected": "Ana",
    "starter": ""
   },
   {
    "text": "Napravi klasu BankovniRacun sa atributom stanje (pocetno 0). Dodaj metod uplati(suma). Uplati 500 i ispisi stanje.",
    "expected": "500",
    "starter": ""
   },
   {
    "text": "Napravi klasu Tacka sa x i y koordinatama. Dodaj metod __str__ koji vraca format '(x, y)'. Ispisi Tacka(3, 4).",
    "expected": "(3, 4)",
    "starter": ""
   },
   {
    "text": "Napravi klasu Vozilo sa metodom kreci() koja vraca 'Vozim'. Napravi klasu Auto koja nasledjuje Vozilo i dodaje metod trubi() koji vraca 'Bip'. Ispisi oba za Auto().",
    "expected": "Vozim\nBip",
    "starter": ""
   }
  ],
  "16": [
   {
    "text": "Koristi re.findall da pronadjes sve brojeve u stringu 'abc123def45'. Ispisi listu.",
    "expected": "['123', '45']",
    "starter": "import re\ns = 'abc123def45'\n"
   },
   {
    "text": "Koristi re.sub da zamenis sve samoglasnike (a, e, i, o, u) zvezdicom u stringu 'programiranje'. Ispisi rezultat.",
    "expected": "pr*gr*m*r*nj*",
    "starter": "import re\ns = 'programiranje'\n"
   },
   {
    "text": "Koristi re.match da proveris da li string 'Pajton' pocinje velikim slovom (A-Z). Ispisi True ili False.",
    "expected": "True",
    "starter": "import re\ns = 'Pajton'\n"
   },
   {
    "text": "Koristi re.split da razdvojis string 'jabuka, kruska; sljiva' po zapeti ILI tacka-zapeti (sa razmakom ili bez). Ispisi listu.",
    "expected": "['jabuka', 'kruska', 'sljiva']",
    "starter": "import re\ns = 'jabuka, kruska; sljiva'\n"
   },
   {
    "text": "Koristi re.findall da pronadjes sve reci koje imaju tacno 4 slova u stringu 'ja ucim da programiram'. Ispisi listu.",
    "expected": "['ucim']",
    "starter": "import re\ns = 'ja ucim da programiram'\n"
   },
   {
    "text": "Proveri da li je string 'test@mail.com' validan email pomocu re.match (prosto: slova, @, slova, tacka, slova). Ispisi True ili False.",
    "expected": "True",
    "starter": "import re\ns = 'test@mail.com'\n"
   }
  ],
  "17": [
   {
    "text": "Uvezi numpy kao np. Napravi niz [10, 20, 30] i ispisi njegov prosek.",
    "expected": "20.0",
    "starter": "import numpy as np\n"
   },
   {
    "text": "Napravi numpy niz od 5 nula i ispisi ga.",
    "expected": "[0. 0. 0. 0. 0.]",
    "starter": "import numpy as np\n"
   },
   {
    "text": "Napravi numpy niz brojeva od 0 do 5 (ne ukljucujuci 5) i ispisi ga.",
    "expected": "[0 1 2 3 4]",
    "starter": "import numpy as np\n"
   },
   {
    "text": "Napravi 2D numpy niz [[1, 2], [3, 4]] i ispisi njegovu sumu svih elemenata.",
    "expected": "10",
    "starter": "import numpy as np\n"
   },
   {
    "text": "Napravi numpy niz [1, 2, 3, 4, 5]. Ispisi sve elemente vece od 2.",
    "expected": "[3 4 5]",
    "starter": "import numpy as np\n"
   },
   {
    "text": "Uvezi numpy kao np. Napravi niz od 3 elementa [1, 2, 3] i ispisi njegov oblik (shape).",
    "expected": "(3,)",
    "starter": "import numpy as np\n"
   }
  ],
  "18": [
   {
    "text": "Uvezi matplotlib.pyplot kao plt. Napravi linijski grafik za x = [1, 2, 3] i y = [2, 4, 6]. (Samo napravi, ne moras da prikazes).",
    "expected": "",
    "starter": "import matplotlib.pyplot as plt\n"
   },
   {
    "text": "Napravi grafik koji prikazuje y = [5, 3, 8]. Postavi naslov na 'Moj grafik'.",
    "expected": "",
    "starter": "import matplotlib.pyplot as plt\n"
   },
   {
    "text": "Napravi scatter grafik sa tackama x = [1, 2, 3] i y = [4, 5, 6].",
    "expected": "",
    "starter": "import matplotlib.pyplot as plt\n"
   },
   {
    "text": "Napravi stubasti grafik (bar) za kategorije ['A', 'B'] i vrednosti [10, 20].",
    "expected": "",
    "starter": "import matplotlib.pyplot as plt\n"
   },
   {
    "text": "Napravi grafik y = [1, 4, 9, 16]. Postavi oznaku x-ose na 'Vreme' i y-ose na 'Vrednost'.",
    "expected": "",
    "starter": "import matplotlib.pyplot as plt\n"
   },
   {
    "text": "Napravi grafik sa dve linije: y1 = [1, 2, 3] i y2 = [3, 2, 1]. Dodaj legendu sa imenima 'Rast' i 'Pad'.",
    "expected": "",
    "starter": "import matplotlib.pyplot as plt\n"
   }
  ],
  "19": [
   {
    "text": "Uvezi random. Postavi random.seed(42), pa baci kockicu 1000 puta (random.randint(1, 6)) i ispisi prosek zaokruzen na 1 decimalu.",
    "expected": "3.5",
    "starter": "import random\n"
   },
   {
    "text": "Postavi random.seed(42), pa simuliraj 100 bacanja novcica (random.choice([0, 1])). Ispisi broj dobijenih jedinica.",
    "expected": "44",
    "starter": "import random\n"
   },
   {
    "text": "Uvezi random. Postavi random.seed(42), pa napravi listu od 10 slucajnih brojeva izmedju 1 i 10 (random.randint) i ispisi je.",
    "expected": "[2, 1, 5, 4, 4, 3, 2, 9, 2, 10]",
    "starter": "import random\n"
   },
   {
    "text": "Postavi random.seed(42), pa simuliraj 1000 bacanja dve kockice (dva poziva random.randint(1, 6) po bacanju). Ispisi koliko puta je zbir bio 7.",
    "expected": "160",
    "starter": "import random\n"
   },
   {
    "text": "Uvezi random. Postavi seed na 42. Ispisi prvi slucajni broj (random.random()).",
    "expected": "0.6394267984578837",
    "starter": "import random\n"
   },
   {
    "text": "Postavi random.seed(42) i izracunaj pribliznu vrednost broja pi Monte Karlo metodom: 1000 tacaka, x i y iz random.uniform(-1, 1) (prvo x, pa y). Ispisi zaokruzeno na 2 decimale.",
    "expected": "3.18",
    "starter": "import random\n"
   }
  ],
  "20": [
   {
    "text": "Uvezi pandas kao pd. Napravi DataFrame sa kolonom 'ime': ['Ana', 'Marko'] i ispisi ga.",
    "expected": "     ime\n0    Ana\n1  Marko",
    "starter": "import pandas as pd\n"
   },
   {
    "text": "Napravi Series [10, 20, 30] i ispisi njegov zbir.",
    "expected": "60",
    "starter": "import pandas as pd\n"
   },
   {
    "text": "Napravi DataFrame sa kolonama 'a' i 'b' ([1, 2], [3, 4]). Ispisi samo kolonu 'a' kao Series.",
    "expected": "0    1\n1    2\nName: a, dtype: int64",
    "starter": "import pandas as pd\n"
   },
   {
    "text": "Data je lista [5, 10, 15]. Napravi DataFrame i ispisi red gde je vrednost veca od 5.",
    "expected": "   0\n1  10\n2  15",
    "starter": "import pandas as pd\n"
   },
   {
    "text": "Napravi DataFrame sa kolonom 'x': [1, 2, 3]. Dodaj novu kolonu 'y' koja je x * 2. Ispisi ceo DataFrame.",
    "expected": "   x  y\n0  1  2\n1  2  4\n2  3  6",
    "starter": "import pandas as pd\n"
   },
   {
    "text": "Napravi DataFrame sa kolonom 'ocena': [8, 9, 7]. Ispisi prosecnu ocenu.",
    "expected": "8.0",
    "starter": "import pandas as pd\n"
   }
  ],
  "21": [
   {
    "text": "Uvezi minimize iz scipy.optimize. Minimizuj funkciju (x - 5)^2. Ispisi res.x[0].",
    "expected": "5.0",
    "starter": "from scipy.optimize import minimize\n"
   },
   {
    "text": "Minimizuj funkciju x^2 + 2x + 1. Ispisi x u minimumu.",
    "expected": "-1.0",
    "starter": "from scipy.optimize import minimize\n"
   },
   {
    "text": "Minimizuj funkciju (x-2)^2 + (y-3)^2. Ispisi x i y.",
    "expected": "x=2.0, y=3.0",
    "starter": "from scipy.optimize import minimize\n"
   },
   {
    "text": "Minimizuj funkciju x^2 gde je x ogranicen da bude >= 5. Ispisi x.",
    "expected": "5.0",
    "starter": "from scipy.optimize import minimize\n"
   },
   {
    "text": "Minimizuj funkciju (x-1)^2 + (y+2)^2. Ispisi res.success.",
    "expected": "True",
    "starter": "from scipy.optimize import minimize\n"
   },
   {
    "text": "Minimizuj funkciju 2x^2 - 4x + 1. Ispisi vrednost funkcije u minimumu (res.fun), zaokruzeno na 2 decimale.",
    "expected": "-1.0",
    "starter": "from scipy.optimize import minimize\n"
   }
  ],
  "22": [
   {
    "text": "Napravi jednostavnu listu 'X' sa osobinama [1, 2, 3] i listu 'y' sa ciljevima [0, 1, 0]. Ispisi duzinu liste X.",
    "expected": "3",
    "starter": ""
   },
   {
    "text": "Uvezi train_test_split iz sklearn.model_selection. Podeli X = [1, 2, 3, 4] i y = [0, 1, 0, 1] na trening i test (test_size=0.5, random_state=42). Ispisi duzinu X_train.",
    "expected": "2",
    "starter": "from sklearn.model_selection import train_test_split\n"
   },
   {
    "text": "Uvezi numpy kao np. Napravi X = np.array([[1, 2], [3, 4], [5, 6]]). Ispisi oblik (shape) matrice X.",
    "expected": "(3, 2)",
    "starter": "import numpy as np\n"
   },
   {
    "text": "Data je lista y = [1, 1, 0, 0, 1]. Ispisi koliko ima jedinica (klasa 1).",
    "expected": "3",
    "starter": ""
   },
   {
    "text": "Uvezi numpy kao np. Napravi niz y = np.array([1, 0, 1]). Ispisi srednju vrednost (mean) niza.",
    "expected": "0.6666666666666666",
    "starter": "import numpy as np\n"
   },
   {
    "text": "Uvezi train_test_split. Podeli X = [[1], [2], [3], [4]] i y = [0, 1, 0, 1]. Ispisi duzinu X_test.",
    "expected": "2",
    "starter": "from sklearn.model_selection import train_test_split\n"
   }
  ],
  "23": [
   {
    "text": "Uvezi GaussianNB. Napravi model, istreniraj ga na X = [[1], [2], [3], [4]] i y = [0, 0, 1, 1] i ispisi predikciju za [[2.5]].",
    "expected": "[0]",
    "starter": "from sklearn.naive_bayes import GaussianNB\n"
   },
   {
    "text": "Uvezi GaussianNB. Treniraj na X = [[1], [2], [8], [9]] i y = [0, 0, 1, 1]. Ispisi predikciju za [[8.5]].",
    "expected": "[1]",
    "starter": "from sklearn.naive_bayes import GaussianNB\n"
   },
   {
    "text": "Uvezi GaussianNB. Treniraj na X = [[1, 2], [2, 3], [3, 4]] i y = [0, 0, 1]. Ispisi predikciju za [[2, 3]].",
    "expected": "[0]",
    "starter": "from sklearn.naive_bayes import GaussianNB\n"
   },
   {
    "text": "Uvezi GaussianNB. Treniraj model na X = [[1], [2]] i y = [1, 0]. Ispisi predikciju za dve tacke: [[1], [2]].",
    "expected": "[1 0]",
    "starter": "from sklearn.naive_bayes import GaussianNB\n"
   },
   {
    "text": "Uvezi GaussianNB. Treniraj na X = [[1], [2], [3]] i y = [1, 1, 0]. Ispisi predikciju za [[10]].",
    "expected": "[1]",
    "starter": "from sklearn.naive_bayes import GaussianNB\n"
   },
   {
    "text": "Uvezi GaussianNB. Treniraj na X = [[1], [2], [3]] i y = [1, 0, 1]. Ispisi tacnost (score) na istim podacima (X, y).",
    "expected": "1.0",
    "starter": "from sklearn.naive_bayes import GaussianNB\n"
   }
  ],
  "24": [
   {
    "text": "Uvezi KNeighborsClassifier sa K=3. Treniraj na X = [[1], [2], [3], [4]] i y = [0, 0, 1, 1]. Ispisi predikciju za [[2.5]].",
    "expected": "[0]",
    "starter": "from sklearn.neighbors import KNeighborsClassifier\n"
   },
   {
    "text": "Uvezi KNeighborsClassifier sa K=1. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[2.1]].",
    "expected": "[0]",
    "starter": "from sklearn.neighbors import KNeighborsClassifier\n"
   },
   {
    "text": "Uvezi KNeighborsClassifier sa K=1. Treniraj na X = [[1, 1], [2, 2], [3, 3]] i y = [0, 0, 1]. Ispisi predikciju za [[2, 2]].",
    "expected": "[0]",
    "starter": "from sklearn.neighbors import KNeighborsClassifier\n"
   },
   {
    "text": "Uvezi KNeighborsClassifier sa K=3. Treniraj na X = [[1], [2], [3]] i y = [1, 0, 1]. Ispisi predikciju za dve tacke: [[2], [3]].",
    "expected": "[1 1]",
    "starter": "from sklearn.neighbors import KNeighborsClassifier\n"
   },
   {
    "text": "Uvezi StandardScaler iz sklearn.preprocessing. Skaliraj listu [[10], [20], [30]] i ispisi transformisane podatke zaokruzene na 1 decimalu.",
    "expected": "[[-1.2]\n [ 0. ]\n [ 1.2]]",
    "starter": "from sklearn.preprocessing import StandardScaler\n"
   },
   {
    "text": "Uvezi KNeighborsClassifier sa K=1. Treniraj na X = [[1], [2], [3], [4]] i y = [0, 1, 0, 1]. Ispisi tacnost (score) na istim podacima.",
    "expected": "1.0",
    "starter": "from sklearn.neighbors import KNeighborsClassifier\n"
   }
  ],
  "25": [
   {
    "text": "Uvezi DecisionTreeClassifier. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[2.5]].",
    "expected": "[0]",
    "starter": "from sklearn.tree import DecisionTreeClassifier\n"
   },
   {
    "text": "Uvezi DecisionTreeClassifier. Treniraj na X = [[1], [2]] i y = [1, 0]. Ispisi predikciju za [[1.5]].",
    "expected": "[1]",
    "starter": "from sklearn.tree import DecisionTreeClassifier\n"
   },
   {
    "text": "Uvezi DecisionTreeClassifier sa max_depth=1. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[1]].",
    "expected": "[0]",
    "starter": "from sklearn.tree import DecisionTreeClassifier\n"
   },
   {
    "text": "Uvezi DecisionTreeClassifier. Treniraj na X = [[1, 2], [2, 3], [3, 4]] i y = [0, 0, 1]. Ispisi predikciju za [[2, 3]].",
    "expected": "[0]",
    "starter": "from sklearn.tree import DecisionTreeClassifier\n"
   },
   {
    "text": "Uvezi DecisionTreeClassifier. Treniraj na X = [[1], [2], [3], [4]] i y = [0, 1, 0, 1]. Ispisi tacnost (score) na istim podacima.",
    "expected": "1.0",
    "starter": "from sklearn.tree import DecisionTreeClassifier\n"
   },
   {
    "text": "Uvezi DecisionTreeClassifier sa max_depth=1. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[3]].",
    "expected": "[1]",
    "starter": "from sklearn.tree import DecisionTreeClassifier\n"
   }
  ],
  "26": [
   {
    "text": "Uvezi RandomForestClassifier. Treniraj na X = [[1], [2], [3]] i y = [0, 0, 1]. Ispisi predikciju za [[2.5]].",
    "expected": "[0]",
    "starter": "from sklearn.ensemble import RandomForestClassifier\n"
   },
   {
    "text": "Uvezi RandomForestClassifier. Treniraj na X = [[1], [2]] i y = [1, 0]. Ispisi predikciju za [[1.5]].",
    "expected": "[1]",
    "starter": "from sklearn.ensemble import RandomForestClassifier\n"
   },
   {
    "text": "Uvezi RandomForestClassifier. Treniraj na X = [[1, 2], [2, 3], [3, 4]] i y = [0, 0, 1]. Ispisi predikciju za [[2, 3]].",
    "expected": "[0]",
    "starter": "from sklearn.ensemble import RandomForestClassifier\n"
   },
   {
    "text": "Uvezi RandomForestClassifier. Treniraj na X = [[1], [2], [3], [4]] i y = [0, 1, 0, 1]. Ispisi tacnost (score) na istim podacima.",
    "expected": "1.0",
    "starter": "from sklearn.ensemble import RandomForestClassifier\n"
   },
   {
    "text": "Uvezi RandomForestClassifier sa n_estimators=10. Treniraj na X = [[1], [2], [3]] i y = [1, 0, 1]. Ispisi koliko stabala ima u sumi (len(clf.estimators_)).",
    "expected": "10",
    "starter": "from sklearn.ensemble import RandomForestClassifier\n"
   },
   {
    "text": "Uvezi RandomForestClassifier. Treniraj model i ispisi broj stabala u sumi (n_estimators) za default model.",
    "expected": "100",
    "starter": "from sklearn.ensemble import RandomForestClassifier\n"
   }
  ]
 },
 "topics": [
  {
   "title": "Knjiga",
   "items": [
    {
     "file": "OI_25_00_uvod.html",
     "title": "Uvod"
    }
   ]
  },
  {
   "title": "Osnove Pajtona",
   "items": [
    {
     "file": "OI_25_01_Osnove.html",
     "title": "Osnove programiranja"
    },
    {
     "file": "OI_25_02_Python_instalacija.html",
     "title": "Pajton okruzenje"
    },
    {
     "file": "OI_25_03_Elementi_Pajtona.html",
     "title": "Osnovni elementi jezika"
    },
    {
     "file": "OI_25_04_logicke_input.html",
     "title": "Logicke promenljive"
    },
    {
     "file": "OI_25_05_stringovi.html",
     "title": "Stringovi"
    },
    {
     "file": "OI_25_06_liste_uvod.html",
     "title": "Liste"
    },
    {
     "file": "OI_25_07_stringovi_liste_napredno.html",
     "title": "Jos o stringovima i listama"
    },
    {
     "file": "OI_25_08_moduli.html",
     "title": "Moduli"
    },
    {
     "file": "OI_25_09_torke_skupovi_recnici.html",
     "title": "Torke, skupovi i recnici"
    },
    {
     "file": "OI_25_10_naredbe_grananja.html",
     "title": "Naredbe grananja"
    },
    {
     "file": "OI_25_11_petlje.html",
     "title": "Petlje"
    },
    {
     "file": "OI_25_12_funkcije.html",
     "title": "Funkcije"
    },
    {
     "file": "OI_25_14_rad_sa_datotekama.html",
     "title": "Rad sa datotekama"
    },
    {
     "file": "OI_25_15_upravljanje_greskama.html",
     "title": "Upravljanje greskama"
    },
    {
     "file": "OI_25_16_klase.html",
     "title": "Klase"
    },
    {
     "file": "OI_26_01_Regularni_izrazi.html",
     "title": "Regularni izrazi"
    }
   ]
  },
  {
   "title": "Poslovno odlucivanje",
   "items": [
    {
     "file": "OI_25_17_NumPy.html",
     "title": "Uvod u NumPy"
    },
    {
     "file": "OI_25_18_Matplotlib.html",
     "title": "Matplotlib"
    },
    {
     "file": "OI_25_19_Simulacije.html",
     "title": "Monte Karlo simulacije"
    },
    {
     "file": "OI_25_20_Pandas.html",
     "title": "Pandas"
    },
    {
     "file": "OI_25_21_SciPy.html",
     "title": "Optimizacija: SciPy"
    }
   ]
  },
  {
   "title": "Masinsko ucenje",
   "items": [
    {
     "file": "ML_25_01_Uvod_1.html",
     "title": "Uvod"
    },
    {
     "file": "ML_25_02_Nadgledano_ucenje.html",
     "title": "Nadgledano ucenje"
    },
    {
     "file": "ML_25_03_Naivni_Bajes.html",
     "title": "Naivni Bajesovi klasifikatori"
    },
    {
     "file": "ML_25_04_KNN.html",
     "title": "K najblizih suseda"
    },
    {
     "file": "ML_25_05_Stabla_odlucivanja.html",
     "title": "Stabla odlucivanja"
    },
    {
     "file": "ML_25_06_Ansambl_metode.html",
     "title": "Ansambl metode"
    }
   ]
  }
 ]
};
