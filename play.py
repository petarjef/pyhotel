"""Tok igre: hotel -> lista nivoa -> kviz ili zadatak sa kodom (TaskLab).

PlayPage drzi sve ekrane u jednom QStackedWidget-u i povezuje ih signalima:
ekrani samo javljaju sta se desilo, a PlayPage odlucuje sta se dalje prikazuje.
Podaci o zadacima su u tasks.py, a progres u progress.py.
"""

import re

from PySide6.QtCore import QTimer, Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QGridLayout, QLabel, QPlainTextEdit, QPushButton,
    QStackedWidget, QVBoxLayout, QWidget,
)

import hotel
import progress
import tasks
from hotel import HotelPage
from lab import CodeLab

LEVELS_STYLE = """
QWidget#levels { background: #4672a8; }
QLabel#ltitle { color: #ffffff; font-size: 11px; }
QLabel#lnote { color: #ffffff; font-size: 9px; }
QPushButton#back {
    background: #ffd43b; color: #101826; border: none; padding: 10px 12px; font-size: 9px;
}
QPushButton#lv_done, QPushButton#lv_cur, QPushButton#lv_locked {
    border: 4px solid #0d1828; font-size: 14px; color: #101826;
}
QPushButton#lv_done { background: #6bd16b; }
QPushButton#lv_cur { background: #ffd43b; }
QPushButton#lv_locked { background: #aab0ba; color: #6c7380; }
"""

QUIZ_STYLE = """
QWidget#quiz { background: #4672a8; }
QLabel#qt { color: #ffffff; font-size: 10px; }
QLabel#qq { color: #ffd43b; font-size: 9px; }
QLabel#qmsg { color: #ffffff; font-size: 10px; }
QPlainTextEdit#qcode {
    background: #101826; color: #e8f1ff; border: 4px solid #0d1828; padding: 8px;
}
QPushButton#back {
    background: #ffd43b; color: #101826; border: none; padding: 10px 12px; font-size: 9px;
}
QPushButton#opt {
    background: #f4e9c8; color: #101826; border: 4px solid #0d1828;
    padding: 12px; text-align: left;
}
QPushButton#opt:hover { background: #fff3c4; }
QPushButton#opt:disabled { color: #101826; }
"""


class LevelsPage(QWidget):
    """Ekran sa 12 dugmadi (nivoa) za izabrani sprat."""
    back = Signal()
    level_chosen = Signal(int, int)  # sprat, nivo

    def __init__(self):
        """Pravi dugme < HOTEL, naslov i prazno mesto za mrezu nivoa (puni je show_floor)."""
        super().__init__()
        self.setObjectName("levels")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(LEVELS_STYLE)
        self.lay = QVBoxLayout(self)
        self.lay.setContentsMargins(14, 14, 14, 14)
        self.lay.setSpacing(16)

        b = QPushButton("< HOTEL")
        b.setObjectName("back")
        b.setCursor(Qt.PointingHandCursor)
        b.clicked.connect(self.back)
        self.lay.addWidget(b, 0, Qt.AlignLeft)

        self.title = QLabel("")
        self.title.setObjectName("ltitle")
        self.title.setWordWrap(True)
        self.lay.addWidget(self.title)

        self.grid_holder = QWidget()
        self.lay.addWidget(self.grid_holder)
        self.lay.addStretch(1)

    def show_floor(self, n):
        """Prikazuje nivoe sprata n. Stanje dugmeta: done (resen), cur (prvi nereseni)
        ili locked (onemogucen), pa se nivoi resavaju redom.
        """
        i = n - 1
        self.title.setText(f"Floor {n}: {hotel.LESSONS[i]}")
        locked = hotel.floor_state(i) == "locked"
        done = progress.done_count(n)

        # stara mreza se brise i pravi se nova, jer se stanje nivoa menja
        self.grid_holder.deleteLater()
        self.grid_holder = QWidget()
        if n not in tasks.QUIZ:
            box = QVBoxLayout(self.grid_holder)
            note = QLabel("Zadaci za ovaj sprat stizu uskoro.")
            note.setObjectName("lnote")
            note.setWordWrap(True)
            box.addWidget(note)
        else:
            grid = QGridLayout(self.grid_holder)
            grid.setSpacing(12)
            for k in range(hotel.LEVELS):
                lvl = k + 1
                if locked:
                    st = "locked"
                elif progress.is_solved(n, lvl):
                    st = "done"
                elif lvl == done + 1:
                    st = "cur"
                else:
                    st = "locked"
                btn = QPushButton(str(lvl))
                btn.setObjectName("lv_" + st)
                btn.setFixedSize(76, 76)
                if st == "locked":
                    btn.setEnabled(False)
                else:
                    btn.setCursor(Qt.PointingHandCursor)
                    btn.clicked.connect(lambda _=False, l=lvl: self.level_chosen.emit(n, l))
                grid.addWidget(btn, k // 3, k % 3)
        # mesto 2: ispod dugmeta nazad (0) i naslova (1)
        self.lay.insertWidget(2, self.grid_holder)


class QuizPage(QWidget):
    """Kviz: kod ili pitanje i 4 ponudjena odgovora. Tacan odgovor emituje solved,
    netacan onemogucuje samo to dugme (moze se probati ponovo).
    """
    back = Signal()
    solved = Signal()
    next_clicked = Signal()

    def __init__(self):
        """Gradi dugme nazad, naslov, polje sa kodom (samo za citanje), 4 dugmeta odgovora i NEXT."""
        super().__init__()
        self.setObjectName("quiz")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(QUIZ_STYLE)
        self.answer = 0
        self.done = False
        mono = QFont("Consolas", 12)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(14, 14, 14, 14)
        lay.setSpacing(12)

        b = QPushButton("< BACK")
        b.setObjectName("back")
        b.setCursor(Qt.PointingHandCursor)
        b.clicked.connect(self.back)
        lay.addWidget(b, 0, Qt.AlignLeft)

        self.title = QLabel("")
        self.title.setObjectName("qt")
        lay.addWidget(self.title)

        self.question = QLabel("Sta ispisuje ovaj kod?")
        self.question.setObjectName("qq")
        lay.addWidget(self.question)

        self.code = QPlainTextEdit()
        self.code.setObjectName("qcode")
        self.code.setReadOnly(True)
        self.code.setFont(mono)
        self.code.setFixedHeight(150)
        lay.addWidget(self.code)

        self.buttons = []
        for k in range(4):
            btn = QPushButton("")
            btn.setObjectName("opt")
            btn.setFont(mono)
            btn.setMinimumHeight(52)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda _=False, k=k: self._pick(k))
            lay.addWidget(btn)
            self.buttons.append(btn)

        self.msg = QLabel("")
        self.msg.setObjectName("qmsg")
        lay.addWidget(self.msg)

        self.next_btn = QPushButton("NEXT >")
        self.next_btn.setObjectName("back")
        self.next_btn.setCursor(Qt.PointingHandCursor)
        self.next_btn.clicked.connect(self.next_clicked)
        self.next_btn.hide()
        lay.addWidget(self.next_btn, 0, Qt.AlignRight)
        lay.addStretch(1)

    def load(self, title, code, options, answer):
        """Postavlja pitanje, odgovore i indeks tacnog. Naslov 'Sta ispisuje ovaj kod?' se
        sakriva kod konceptualnih pitanja (pitanje je u komentaru).
        """
        self.title.setText(title)
        self.code.setPlainText(code)
        # konceptualna pitanja imaju pitanje u komentaru; tada naslov "Sta ispisuje..." ne vazi
        lines = [l.strip() for l in code.splitlines() if l.strip()]
        asks = any(l.startswith("#") and ("?" in l or l.endswith(":")) for l in lines) or all(
            l.startswith(("#", "import ", "from ")) for l in lines)
        self.question.setVisible(not asks)
        self.answer = answer
        self.done = False
        self.msg.setText("")
        self.next_btn.hide()
        for btn, text in zip(self.buttons, options):
            btn.setText(text)
            btn.setEnabled(True)
            btn.setStyleSheet("")

    def _pick(self, k):
        """Obradjuje klik na odgovor k: tacan -> zeleno, poruka i signal solved; netacan -> crveno."""
        if self.done:
            return
        btn = self.buttons[k]
        if k == self.answer:
            self.done = True
            btn.setStyleSheet("background: #6bd16b;")
            self.msg.setText("TACNO!")
            self.next_btn.show()
            self.solved.emit()
        else:
            btn.setStyleSheet("background: #e86a6a;")
            btn.setEnabled(False)
            self.msg.setText("Netacno, probaj ponovo.")


def _norm(s):
    """Priprema ispis za poredjenje: skida razmake na kraju linija i prazne linije
    na pocetku i kraju.
    """
    return "\n".join(line.rstrip() for line in s.strip().splitlines())


_NUM = re.compile(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\w.])")


def _canon_nums(s):
    """20 i 20.0 su isti broj (isto kao LENIENT_NUMBERS u docs/app.js)."""
    def fix(m):
        """Ceo broj zapisan sa decimalom (20.0) postaje 20; ostali brojevi ostaju kanonski."""
        v = float(m.group(0))
        if v.is_integer():
            return str(int(v)) if abs(v) < 2 ** 53 else m.group(0)
        return repr(v)
    return _NUM.sub(fix, s)


def same_output(got, expected):
    """True ako se ispis poklapa sa ocekivanim. Poredi se tekst, a zatim i tekst sa
    kanonskim brojevima (20 i 20.0 su isto, kao LENIENT_NUMBERS u docs/app.js).
    """
    a, b = _norm(got), _norm(expected)
    return a == b or _canon_nums(a) == _canon_nums(b)


class TaskLab(CodeLab):
    """Code Lab sa dugmetom CHECK koje poredi output sa ocekivanim."""
    solved = Signal()
    next_clicked = Signal()

    def __init__(self):
        """Dodaje dugmad CHECK i NEXT u traku iznad editora. layout().itemAt(0) je
        horizontalni layout sa dugmadima koji pravi CodeLab.
        """
        super().__init__()
        self.expected = None
        self.checking = False
        self.captured = ""
        self.b_check = self._btn("CHECK")
        self.layout().itemAt(0).layout().addWidget(self.b_check)
        self.b_check.clicked.connect(self.check)
        self.b_next = self._btn("NEXT >")
        self.b_next.hide()
        self.layout().itemAt(0).layout().addWidget(self.b_next)
        self.b_next.clicked.connect(self.next_clicked)

    def load_task(self, text, starter, expected):
        """Otvara zadatak: postavlja ocekivani ispis i pocetni kod."""
        self.expected = expected
        self.b_check.show()
        self.b_next.hide()
        self.start(text, starter)

    def load_free(self):
        """Otvara slobodan Code Lab (bez provere, CHECK je sakriven)."""
        self.expected = None
        self.b_check.hide()
        self.b_next.hide()
        self.start("CODE LAB: pisi Python i pritisni RUN (ili Ctrl+Enter).", "")

    def check(self):
        """Pokrece kod i usput hvata ispis (captured). Poredjenje sa ocekivanim se radi tek
        kad se izvrsavanje zavrsi (vidi _set_running).
        """
        if self.running or self.expected is None:
            return
        self.captured = ""
        self.checking = True
        self.run()
        if not self.running:
            self.checking = False

    def _write(self, text):
        """Dok traje CHECK, ispis se pored ekrana skuplja i u captured."""
        if self.checking:
            self.captured += text
        super()._write(text)

    def _set_running(self, on):
        """Kad se izvrsavanje zavrsi tokom CHECK-a, poredi captured sa expected i, ako se
        poklapaju, prikazuje NEXT i emituje solved. hasattr/getattr su potrebni jer se
        metoda prvi put poziva iz CodeLab.__init__, pre nego sto ova polja postoje.
        """
        super()._set_running(on)
        if hasattr(self, "b_check"):
            self.b_check.setEnabled(not on)
        if not on and getattr(self, "checking", False):
            self.checking = False
            if same_output(self.captured, self.expected):
                self.out.appendPlainText("\n>>> TACNO!")
                self.b_next.show()
                self.solved.emit()
            else:
                self.out.appendPlainText("\n>>> JOS NE. Trazeni output:\n" + self.expected)


class PlayPage(QStackedWidget):
    """Upravljac ekrana. Indeksi u stack-u: 0 hotel, 1 nivoi, 2 kviz, 3 lab."""
    def __init__(self):
        """Pravi ekrane i povezuje signale (ekrani ne znaju jedan za drugog)."""
        super().__init__()
        self.hotel_page = HotelPage()
        self.levels = LevelsPage()
        self.quiz = QuizPage()
        self.lab = TaskLab()
        for w in (self.hotel_page, self.levels, self.quiz, self.lab):
            self.addWidget(w)
        self.floor = 1
        self.level = 1
        # odakle je lab otvoren: 0 = hotel (slobodan lab), 1 = lista nivoa
        self.lab_from = 0

        # povezivanje signala: sta se desi kad ekran nesto javi
        self.hotel_page.floor_clicked.connect(self._open_floor)
        self.hotel_page.open_lab.connect(self._open_free_lab)
        self.levels.back.connect(lambda: self.setCurrentIndex(0))
        self.levels.level_chosen.connect(self._open_level)
        self.quiz.back.connect(self._to_levels)
        self.quiz.solved.connect(self._solved)
        self.lab.back.connect(self._leave_lab)
        self.lab.solved.connect(self._solved)
        self.quiz.next_clicked.connect(self._next)
        self.lab.next_clicked.connect(self._next)

    def _open_floor(self, n):
        """Klik na sprat u hotelu: pamti sprat i prikazuje listu nivoa."""
        self.floor = n
        self._to_levels()

    def _to_levels(self):
        """Osvezava i prikazuje listu nivoa trenutnog sprata."""
        self.levels.show_floor(self.floor)
        self.setCurrentIndex(1)

    def _open_free_lab(self):
        """Vrata u prizemlju: slobodan Code Lab."""
        self.lab_from = 0
        self.lab.load_free()
        self.setCurrentIndex(3)

    def _leave_lab(self):
        """Dugme nazad u labu: vraca se tamo odakle je lab otvoren."""
        if self.lab_from == 1:
            self._to_levels()
        else:
            self.setCurrentIndex(0)

    def _open_level(self, floor, level):
        """Otvara kviz ili zadatak sa kodom, zavisno od tipa koji vraca tasks.get_task."""
        self.floor, self.level = floor, level
        t = tasks.get_task(floor, level)
        title = f"Floor {floor} - Level {level}"
        if t["type"] == "quiz":
            self.quiz.load(title, t["code"], t["options"], t["answer"])
            self.setCurrentIndex(2)
        else:
            self.lab_from = 1
            text = f"{title}  ({hotel.LESSONS[floor - 1]})\n{t['text']}"
            self.lab.load_task(text, t["starter"], t["expected"])
            self.setCurrentIndex(3)

    def _solved(self):
        """Nivo je resen: upisi u progress."""
        progress.mark(self.floor, self.level)

    def _next(self):
        """NEXT: sledeci nivo, a posle 12. nivoa povratak na listu nivoa."""
        if self.level < hotel.LEVELS:
            self._open_level(self.floor, self.level + 1)
        else:
            self._to_levels()

