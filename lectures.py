from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QStackedWidget, QVBoxLayout, QWidget,
)

BASE = Path(__file__).parent
BOOK_DIR = BASE / "book"
LESSONS_DIR = BASE / "lessons_html"


def book_url(file):
    return QUrl.fromLocalFile(str(BOOK_DIR / file))


def find_lessons():
    if not LESSONS_DIR.exists():
        return []
    return sorted(LESSONS_DIR.glob("*.html"), key=lambda f: f.name.lower())


MOODLE = find_lessons()

SECTIONS = [
    ("Knjiga", [
        ("OI_25_00_uvod.html", "Uvod"),
    ]),
    ("Osnove Pajtona", [
        ("OI_25_01_Osnove.html", "Osnove programiranja"),
        ("OI_25_02_Python_instalacija.html", "Pajton okruzenje"),
        ("OI_25_03_Elementi_Pajtona.html", "Osnovni elementi jezika"),
        ("OI_25_04_logicke_input.html", "Logicke promenljive"),
        ("OI_25_05_stringovi.html", "Stringovi"),
        ("OI_25_06_liste_uvod.html", "Liste"),
        ("OI_25_07_stringovi_liste_napredno.html", "Jos o stringovima i listama"),
        ("OI_25_08_moduli.html", "Moduli"),
        ("OI_25_09_torke_skupovi_recnici.html", "Torke, skupovi i recnici"),
        ("OI_25_10_naredbe_grananja.html", "Naredbe grananja"),
        ("OI_25_11_petlje.html", "Petlje"),
        ("OI_25_12_funkcije.html", "Funkcije"),
        ("OI_25_14_rad_sa_datotekama.html", "Rad sa datotekama"),
        ("OI_25_15_upravljanje_greskama.html", "Upravljanje greskama"),
        ("OI_25_16_klase.html", "Klase"),
        ("OI_26_01_Regularni_izrazi.html", "Regularni izrazi"),
    ]),
    ("Poslovno odlucivanje", [
        ("OI_25_17_NumPy.html", "Uvod u NumPy"),
        ("OI_25_18_Matplotlib.html", "Matplotlib"),
        ("OI_25_19_Simulacije.html", "Monte Karlo simulacije"),
        ("OI_25_20_Pandas.html", "Pandas"),
        ("OI_25_21_SciPy.html", "Optimizacija: SciPy"),
    ]),
    ("Masinsko ucenje", [
        ("ML_25_01_Uvod_1.html", "Uvod"),
        ("ML_25_02_Nadgledano_ucenje.html", "Nadgledano ucenje"),
        ("ML_25_03_Naivni_Bajes.html", "Naivni Bajesovi klasifikatori"),
        ("ML_25_04_KNN.html", "K najblizih suseda"),
        ("ML_25_05_Stabla_odlucivanja.html", "Stabla odlucivanja"),
        ("ML_25_06_Ansambl_metode.html", "Ansambl metode"),
    ]),
]

STYLE = """
QScrollArea { background: transparent; border: none; }
QScrollArea > QWidget > QWidget { background: transparent; }
QLabel#head { color: #ffffff; font-size: 11px; padding-top: 8px; }
QPushButton#cover {
    background: #4b8bbe; border: 4px solid #0d1828; border-left: 24px solid #1d2f4a;
}
QPushButton#cover:hover { background: #5a9bd0; }
QLabel#c1 { color: #ffd43b; font-size: 18px; }
QLabel#c2 { color: #ffffff; font-size: 9px; }
QLabel#c3 { color: #cfe3f7; font-size: 7px; }
QLabel#hint { color: #ffffff; font-size: 9px; }
QPushButton#lec, QPushButton#book {
    background: #f4e9c8; color: #101826; border: 4px solid #0d1828;
    padding: 14px 10px; text-align: left; font-size: 8px;
}
QPushButton#book { background: #ffd43b; }
QPushButton#lec:hover { background: #fff3c4; }
QWidget#bar { background: #1d2f4a; }
QPushButton#back {
    background: #ffd43b; color: #101826; border: none;
    padding: 10px 12px; font-size: 9px;
}
QLabel#rtitle { color: #ffffff; font-size: 9px; padding-left: 8px; }
"""


class PyLogo(QLabel):
    def __init__(self, size=36):
        super().__init__()
        pix = QPixmap(str(BASE / "assets" / "python_logo.png"))
        self.setPixmap(pix.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.setAttribute(Qt.WA_TransparentForMouseEvents)


class BookCover(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName("cover")
        self.setFixedSize(240, 320)
        self.setCursor(Qt.PointingHandCursor)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 28, 14, 24)

        row = QHBoxLayout()
        row.setSpacing(10)
        row.addStretch(1)
        row.addWidget(PyLogo(36))
        title = QLabel("PYTHON")
        title.setObjectName("c1")
        title.setAttribute(Qt.WA_TransparentForMouseEvents)
        row.addWidget(title)
        row.addStretch(1)
        lay.addLayout(row)

        for text, name in [
            (" Poslovno odlucivanje i masinsko ucenje", "c2"),
            ("Azdejkovic\n\nRadojicic\n\nStamenkovic", "c3"),
        ]:
            label = QLabel(text)
            label.setObjectName(name)
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignCenter)
            label.setAttribute(Qt.WA_TransparentForMouseEvents)
            lay.addWidget(label)


class LecturesPage(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(STYLE)
        self.reader = None
        self.back_to = 1
        self.addWidget(self._build_cover())
        self.addWidget(self._build_list())

    def _build_cover(self):
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(14, 20, 14, 20)
        lay.setSpacing(12)

        cover = BookCover()
        cover.clicked.connect(lambda: self.setCurrentIndex(1))
        lay.addWidget(cover, 0, Qt.AlignHCenter)

        hint = QLabel("CLICK TO OPEN")
        hint.setObjectName("hint")
        hint.setAlignment(Qt.AlignCenter)
        lay.addWidget(hint)

        lay.addSpacing(16)
        head = QLabel("Moodle prezentacije")
        head.setObjectName("head")
        lay.addWidget(head)

        if not MOODLE:
            empty = QLabel("Jos nema prezentacija.")
            empty.setObjectName("hint")
            lay.addWidget(empty)
        for f in MOODLE:
            title = f.stem.replace("_", " ")
            b = QPushButton(title)
            b.setObjectName("lec")
            b.setCursor(Qt.PointingHandCursor)
            b.clicked.connect(
                lambda _=False, p=f, t=title, btn=b: self.open_page(
                    QUrl.fromLocalFile(str(p)), t, btn, back=0
                )
            )
            lay.addWidget(b)

        lay.addStretch(1)
        return page

    def _build_list(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        holder = QWidget()
        lay = QVBoxLayout(holder)
        lay.setContentsMargins(14, 16, 14, 24)
        lay.setSpacing(12)

        to_book = QPushButton("< BOOK")
        to_book.setObjectName("back")
        to_book.setCursor(Qt.PointingHandCursor)
        to_book.clicked.connect(lambda: self.setCurrentIndex(0))
        lay.addWidget(to_book, 0, Qt.AlignLeft)

        n = 0
        for section, items in SECTIONS:
            head = QLabel(section)
            head.setObjectName("head")
            lay.addWidget(head)
            for file, title in items:
                b = QPushButton(f"{n}   {title}")
                b.setObjectName("book" if n == 0 else "lec")
                b.setCursor(Qt.PointingHandCursor)
                b.clicked.connect(
                    lambda _=False, f=file, t=title, btn=b: self.open_page(
                        book_url(f), t, btn, back=1
                    )
                )
                lay.addWidget(b)
                n += 1
        lay.addStretch(1)
        scroll.setWidget(holder)
        return scroll

    def open_page(self, url, title, btn, back):
        if self.reader is None:  # pravi se tek pri prvom otvaranju
            self.reader = QWidget()
            v = QVBoxLayout(self.reader)
            v.setContentsMargins(0, 0, 0, 0)
            v.setSpacing(0)

            bar = QWidget()
            bar.setObjectName("bar")
            bar.setAttribute(Qt.WA_StyledBackground, True)
            h = QHBoxLayout(bar)
            h.setContentsMargins(10, 8, 10, 8)
            back_btn = QPushButton("< BACK")
            back_btn.setObjectName("back")
            back_btn.setCursor(Qt.PointingHandCursor)
            back_btn.clicked.connect(lambda: self.setCurrentIndex(self.back_to))
            self.title_label = QLabel("")
            self.title_label.setObjectName("rtitle")
            h.addWidget(back_btn)
            h.addWidget(self.title_label, 1)

            self.web = QWebEngineView()
            v.addWidget(bar)
            v.addWidget(self.web, 1)
            self.addWidget(self.reader)

        self.back_to = back
        self.title_label.setText(title)
        self.web.setUrl(url)
        self.setCurrentWidget(self.reader)
        btn.setStyleSheet("background: #6bd16b;")  # oznaci kao otvorenu