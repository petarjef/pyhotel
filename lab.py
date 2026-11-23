"""Code Lab: editor za Python kod sa pravim Jupyter kernelom.

Kod igraca se izvrsava u ZASEBNOM procesu (kernel), pa ne moze da sruci igru, moze da se
prekine (STOP) i restartuje (RESET), a promenljive ostaju izmedju pokretanja.
Komunikacija ide porukama preko jupyter_client-a:
  iopub - ispis kernela (print, rezultati, greske, grafici, status)
  stdin - zahtevi za unos (input())
CodeLab koristi i TaskLab u play.py (dodaje dugme CHECK).
"""

import base64
import queue
import re

from jupyter_client.manager import start_new_kernel
from PySide6.QtCore import QTimer, Qt, Signal
from PySide6.QtGui import QFont, QPixmap, QTextCursor
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QScrollArea, QVBoxLayout, QWidget,
)

ANSI = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")

STYLE = """
QWidget#lab { background: #1d2f4a; }
QLabel#task {
    background: #f4e9c8; color: #101826; padding: 17px;
    font-size: 10px; border-bottom: 4px solid #0d1828;
}
QPushButton#lbtn {
    background: #ffd43b; color: #101826; border: none;
    padding: 10px 10px; font-size: 8px;
}
QPushButton#lbtn:hover { background: #ffe066; }
QPushButton#lbtn:disabled { background: #7d7a5c; color: #3b3b3b; }
QPlainTextEdit#code { background: #101826; color: #e8f1ff; border: none; padding: 8px; }
QPlainTextEdit#out { background: #0a1220; color: #9be28f; border: none; padding: 8px; }
QScrollArea#imgs { background: #0a1220; border: none; }
QWidget#imgbox { background: #0a1220; }
QLineEdit#inp {
    background: #f4e9c8; color: #101826; border: 4px solid #0d1828; padding: 8px;
}
"""


class CodeEdit(QPlainTextEdit):
    """Editor koda: Ctrl+Enter pokrece kod, Enter cuva uvlacenje (posle ':' dodaje 4 razmaka),
    Tab ubacuje 4 razmaka.
    """
    run_requested = Signal()

    def keyPressEvent(self, e):
        """Obrada tastera; sve ostalo prepusta QPlainTextEdit-u."""
        if e.key() in (Qt.Key_Return, Qt.Key_Enter):
            if e.modifiers() & Qt.ControlModifier:
                self.run_requested.emit()
                return
            line = self.textCursor().block().text()
            indent = line[: len(line) - len(line.lstrip())]
            # posle ':' (npr. if, for, def) sledeca linija se uvlaci jos 4 razmaka
            if line.rstrip().endswith(":"):
                indent += "    "
            super().keyPressEvent(e)
            self.insertPlainText(indent)
            return
        if e.key() == Qt.Key_Tab:
            self.insertPlainText("    ")
            return
        super().keyPressEvent(e)


class CodeLab(QWidget):
    """Ceo ekran Code Laba: dugmad, tekst zadatka, editor, izlaz, slike grafika i polje za unos."""
    back = Signal()

    def __init__(self):
        """Gradi izgled i povezuje dugmad. Kernel se NE pokrece ovde nego tek pri prvom koriscenju."""
        super().__init__()
        self.setObjectName("lab")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(STYLE)
        self.km = self.kc = None
        self.msg_id = None
        self.running = False
        self._quit_hooked = False

        mono = QFont("Consolas", 12)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        bar = QHBoxLayout()
        bar.setContentsMargins(8, 8, 8, 8)
        bar.setSpacing(6)
        self.bar = bar
        self.b_back = self._btn("< BACK")
        self.b_run = self._btn("RUN")
        self.b_stop = self._btn("STOP")
        self.b_reset = self._btn("RESET")
        bar.addWidget(self.b_back)
        bar.addStretch(1)
        for b in (self.b_run, self.b_stop, self.b_reset):
            bar.addWidget(b)
        lay.addLayout(bar)

        self.task = QLabel("")
        self.task.setObjectName("task")
        self.task.setWordWrap(True)
        lay.addWidget(self.task)

        self.code = CodeEdit()
        self.code.setObjectName("code")
        self.code.setFont(mono)
        self.code.setTabStopDistance(32)
        lay.addWidget(self.code, 3)

        self.out = QPlainTextEdit()
        self.out.setObjectName("out")
        self.out.setReadOnly(True)
        self.out.setFont(mono)
        lay.addWidget(self.out, 2)

        # grafici (matplotlib) se prikazuju kao slike ispod teksta, kao u web verziji
        self.img_box = QWidget()
        self.img_box.setObjectName("imgbox")
        self.img_lay = QVBoxLayout(self.img_box)
        self.img_lay.setContentsMargins(8, 8, 8, 8)
        self.img_lay.setSpacing(8)
        self.imgs = QScrollArea()
        self.imgs.setObjectName("imgs")
        self.imgs.setWidgetResizable(True)
        self.imgs.setMaximumHeight(240)
        self.imgs.setWidget(self.img_box)
        self.imgs.hide()
        lay.addWidget(self.imgs)

        self.inp = QLineEdit()
        self.inp.setObjectName("inp")
        self.inp.setFont(mono)
        self.inp.hide()
        lay.addWidget(self.inp)

        self.b_back.clicked.connect(self.back)
        self.b_run.clicked.connect(self.run)
        self.b_stop.clicked.connect(self.stop)
        self.b_reset.clicked.connect(self.reset)
        self.code.run_requested.connect(self.run)
        self.inp.returnPressed.connect(self._send_input)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._poll)
        self._set_running(False)

    def _clear_images(self):
        """Brise sve prikazane grafike (pri novom pokretanju ili RESET-u)."""
        while self.img_lay.count():
            w = self.img_lay.takeAt(0).widget()
            if w is not None:
                w.deleteLater()
        self.imgs.hide()

    def _show_image(self, b64):
        """Prikazuje PNG grafik (base64 iz poruke kernela) ispod izlaza."""
        pix = QPixmap()
        if not pix.loadFromData(base64.b64decode(b64), "PNG"):
            return
        label = QLabel()
        label.setPixmap(pix.scaledToWidth(min(pix.width(), 360), Qt.SmoothTransformation))
        self.img_lay.addWidget(label)
        self.imgs.show()

    def _btn(self, text):
        """Pravi zuto dugme istog izgleda kao ostala."""
        b = QPushButton(text)
        b.setObjectName("lbtn")
        b.setCursor(Qt.PointingHandCursor)
        return b

    # ---------- javni deo ----------
    def start(self, task_text, starter=""):
        """Postavlja tekst zadatka i pocetni kod; prvi put pokazuje 'Starting Python...'."""
        html = task_text.replace("\n", "<br>")
        self.task.setText(f'<div style="line-height: 160%;">{html}</div>')
        self.code.setPlainText(starter)
        self._clear_images()
        self.out.setPlainText("Starting Python..." if not self.kc else "")
        self.code.setFocus()
        QTimer.singleShot(40, self._boot)

    def _boot(self):
        """Pokrece kernel odmah posle prikaza ekrana, da prvo pokretanje koda ne kasni."""
        if self.ensure_kernel() and self.out.toPlainText() == "Starting Python...":
            self.out.clear()

    def ensure_kernel(self):
        """Pokrece kernel ako vec ne radi. km (KernelManager) upravlja procesom, kc (KernelClient)
        salje i prima poruke. Vraca False ako kernel ne moze da se pokrene.
        """
        if self.kc:
            return True
        try:
            self.km, self.kc = start_new_kernel(kernel_name="python3", startup_timeout=60)
        except Exception as ex:
            self.out.setPlainText(
                f"Could not start Python kernel:\n{ex}\n\nTry: pip install ipykernel jupyter_client"
            )
            return False
        if not self._quit_hooked:
            app = QApplication.instance()
            if app is not None:
                app.aboutToQuit.connect(self.shutdown)
                self._quit_hooked = True
        # tek kad kernel radi: citaj njegove poruke na svakih 40 ms
        self.timer.start(40)
        return True

    def shutdown(self):
        """Zatvara kanale i gasi kernel (poziva se i pri zatvaranju aplikacije)."""
        try:
            if self.kc:
                self.kc.stop_channels()
        except Exception:
            pass
        try:
            if self.km:
                self.km.shutdown_kernel(now=True)
        except Exception:
            pass
        self.km = self.kc = None
        self.msg_id = None
        self.running = False

    # ---------- dugmad ----------
    def run(self):
        """Salje kod kernelu. execute vraca msg_id po kome kasnije prepoznajemo odgovore."""
        if self.running or not self.ensure_kernel():
            return
        self.out.clear()
        self._clear_images()
        # msg_id vezuje odgovore kernela za OVO pokretanje
        self.msg_id = self.kc.execute(self.code.toPlainText())
        self._set_running(True)

    def stop(self):
        """Prekida izvrsavanje (kao Ctrl+C); promenljive ostaju."""
        if self.km and self.running:
            try:
                self.km.interrupt_kernel()
            except Exception:
                pass

    def reset(self):
        """Restartuje kernel: brisu se sve promenljive."""
        if not self.km:
            return
        try:
            self.km.restart_kernel(now=True)
            self.kc.wait_for_ready(timeout=60)
        except Exception as ex:
            self.out.setPlainText(f"Restart failed: {ex}\nPokusavam ponovo da pokrenem kernel...")
            self.shutdown()
            self.ensure_kernel()
            return
        self.msg_id = None
        self._set_running(False)
        self._clear_images()
        self.out.setPlainText("Python restarted. All variables are cleared.")

    def _set_running(self, on):
        """Ukljucuje/iskljucuje dugmad RUN i STOP; kad izvrsavanje stane, sakriva polje za unos."""
        self.running = on
        self.b_run.setEnabled(not on)
        self.b_stop.setEnabled(on)
        if not on:
            self.inp.hide()

    # ---------- poruke iz kernela ----------
    def _poll(self):
        """Poziva se na svakih 40 ms: ispraznjuje iopub red, pa proverava stdin za input().
        Izuzetak koji nije prazan red znaci da je kernel umro.
        """
        if not self.kc:
            return
        try:
            try:
                while True:
                    self._handle(self.kc.get_iopub_msg(timeout=0))
            except queue.Empty:
                pass
            try:
                msg = self.kc.get_stdin_msg(timeout=0)
                if msg["msg_type"] == "input_request":
                    self._write(msg["content"]["prompt"])
                    self.inp.show()
                    self.inp.setFocus()
            except queue.Empty:
                pass
        except Exception as ex:
            # kernel je verovatno umro: zaustavi polling i resetuj stanje
            self.shutdown()
            self.out.appendPlainText(f"\n[kernel se ugasio: {type(ex).__name__}]")

    def _handle(self, msg):
        """Obradjuje jednu poruku kernela. Poruke koje ne pripadaju trenutnom pokretanju
        (drugi msg_id) se ignorisu.
        """
        if msg["parent_header"].get("msg_id") != self.msg_id:
            return
        t, c = msg["msg_type"], msg["content"]
        if t == "stream":
            self._write(c["text"])
        # execute_result: vrednost poslednjeg izraza (kao u Jupyteru); display_data: slike i ostali prikazi
        elif t in ("execute_result", "display_data"):
            data = c["data"]
            if "image/png" in data:  # grafik: prikazi sliku umesto teksta "<Figure ...>"
                self._show_image(data["image/png"])
            elif data.get("text/plain"):
                self._write(data["text/plain"] + "\n")
        elif t == "error":
            # traceback dolazi sa ANSI bojama; one se uklanjaju regexom
            self._write(ANSI.sub("", "\n".join(c["traceback"])) + "\n")
        # idle znaci da je kernel zavrsio; iopub je uredjen, pa je sav ispis stigao pre ove poruke
        elif t == "status" and c.get("execution_state") == "idle":
            self._set_running(False)

    def _send_input(self):
        """Enter u polju za unos: ispisuje uneto i salje ga kernelu kao odgovor na input()."""
        text = self.inp.text()
        self.inp.clear()
        self.inp.hide()
        self._write(text + "\n")
        self.kc.input(text)

    def _write(self, text):
        """Dodaje tekst na kraj izlaza i drzi prikaz skrolovan do dna."""
        self.out.moveCursor(QTextCursor.End)
        self.out.insertPlainText(text)
        self.out.moveCursor(QTextCursor.End)