import queue
import re

from jupyter_client.manager import start_new_kernel
from PySide6.QtCore import QTimer, Qt, Signal
from PySide6.QtGui import QFont, QTextCursor
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QVBoxLayout, QWidget,
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
QLineEdit#inp {
    background: #f4e9c8; color: #101826; border: 4px solid #0d1828; padding: 8px;
}
"""


class CodeEdit(QPlainTextEdit):
    run_requested = Signal()

    def keyPressEvent(self, e):
        if e.key() in (Qt.Key_Return, Qt.Key_Enter):
            if e.modifiers() & Qt.ControlModifier:
                self.run_requested.emit()
                return
            line = self.textCursor().block().text()
            indent = line[: len(line) - len(line.lstrip())]
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
    back = Signal()

    def __init__(self):
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

    def _btn(self, text):
        b = QPushButton(text)
        b.setObjectName("lbtn")
        b.setCursor(Qt.PointingHandCursor)
        return b

    # ---------- javni deo ----------
    def start(self, task_text, starter=""):
        html = task_text.replace("\n", "<br>")
        self.task.setText(f'<div style="line-height: 160%;">{html}</div>')
        self.code.setPlainText(starter)
        self.out.setPlainText("Starting Python..." if not self.kc else "")
        self.code.setFocus()
        QTimer.singleShot(40, self._boot)

    def _boot(self):
        if self.ensure_kernel() and self.out.toPlainText() == "Starting Python...":
            self.out.clear()

    def ensure_kernel(self):
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
        self.timer.start(40)
        return True

    def shutdown(self):
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
        if self.running or not self.ensure_kernel():
            return
        self.out.clear()
        self.msg_id = self.kc.execute(self.code.toPlainText())
        self._set_running(True)

    def stop(self):
        if self.km and self.running:
            try:
                self.km.interrupt_kernel()
            except Exception:
                pass

    def reset(self):
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
        self.out.setPlainText("Python restarted. All variables are cleared.")

    def _set_running(self, on):
        self.running = on
        self.b_run.setEnabled(not on)
        self.b_stop.setEnabled(on)
        if not on:
            self.inp.hide()

    # ---------- poruke iz kernela ----------
    def _poll(self):
        if not self.kc:
            return
        try:
            while True:
                self._handle(self.kc.get_iopub_msg(timeout=0))
        except queue.Empty:
            pass
        except Exception:
            # kernel je verovatno umro — zaustavi polling i resetuj stanje
            self.shutdown()
            self.out.appendPlainText("\n[kernel se ugasio]")
            return
        try:
            msg = self.kc.get_stdin_msg(timeout=0)
            if msg["msg_type"] == "input_request":
                self._write(msg["content"]["prompt"])
                self.inp.show()
                self.inp.setFocus()
        except queue.Empty:
            pass
        except Exception:
            pass

    def _handle(self, msg):
        if msg["parent_header"].get("msg_id") != self.msg_id:
            return
        t, c = msg["msg_type"], msg["content"]
        if t == "stream":
            self._write(c["text"])
        elif t in ("execute_result", "display_data"):
            txt = c["data"].get("text/plain")
            if txt:
                self._write(txt + "\n")
        elif t == "error":
            self._write(ANSI.sub("", "\n".join(c["traceback"])) + "\n")
        elif t == "status" and c.get("execution_state") == "idle":
            self._set_running(False)

    def _send_input(self):
        text = self.inp.text()
        self.inp.clear()
        self.inp.hide()
        self._write(text + "\n")
        self.kc.input(text)

    def _write(self, text):
        self.out.moveCursor(QTextCursor.End)
        self.out.insertPlainText(text)
        self.out.moveCursor(QTextCursor.End)