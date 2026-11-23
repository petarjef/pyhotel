"""Tab Help AI: cet sa AI tutorom Monty Python preko Google Gemini.

Mrezni poziv radi u zasebnoj niti (Worker) da prozor ne bi zamrzao, a odgovor stize
u delovima (streaming). Kljuc i model su u settings.json, istorija u chat_history.json
(oba su lokalna i nisu u repozitorijumu).
"""

import html
import json
import os
import re
from pathlib import Path

from PySide6.QtCore import QThread, QTimer, QUrl, Qt, Signal
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QStackedWidget, QTextBrowser, QVBoxLayout, QWidget,
)

BASE = Path(__file__).parent
SETTINGS_FILE = BASE / "settings.json"
HISTORY_FILE = BASE / "chat_history.json"
DEFAULT_MODEL = "gemini-3.1-flash-lite"

SYSTEM = (
    "You are Monty Python, the friendly tutor inside a Python learning game for "
    "university students. Only answer questions about Python programming and the "
    "topics of the course (variables, strings, lists, modules, conditions, loops, "
    "functions, files, classes, NumPy, Pandas, basic machine learning). If asked "
    "about anything else, politely decline in one sentence and steer back to Python. "
    "Reply in the language the student writes in (Serbian by default, Latin script). "
    "Keep answers short and beginner-friendly. Put code in triple-backtick blocks. "
    "When a student is stuck on an exercise, prefer a hint or explanation first and "
    "show the full solution only if they ask again."
)

WELCOME = "Hi! I'm Monty Python. Ask me anything about Python."

STYLE = """
QWidget#chat { background: #4672a8; }
QTextBrowser { background: transparent; border: none; }
QLabel#who { color: #ffffff; font-size: 8px; }
QLabel#atitle { color: #ffffff; font-size: 16px; }
QLabel#anote { color: #ffffff; font-size: 10px; }
QLabel#flabel { color: #ffd43b; font-size: 11px; }
QLabel#status { color: #ffffff; font-size: 10px; }
QLineEdit#cin {
    background: #f4e9c8; color: #101826; border: 4px solid #0d1828; padding: 10px;
    font-size: 9px;
}
QPushButton#cbtn {
    background: #ffd43b; color: #101826; border: none; padding: 12px 10px; font-size: 9px;
}
QPushButton#cbtn:hover { background: #ffe066; }
QPushButton#cbtn:disabled { background: #7d7a5c; color: #3b3b3b; }
"""

PAGE_CSS = "body, td { font-size: 10px; line-height: 160%; }"
PRE = ('style="background-color:#101826; color:#9be28f; font-family:Consolas;'
       ' font-size:12px;"')


# ---------------- podesavanja ----------------
def load_settings():
    """Cita kljuc i model: prvo promenljiva okruzenja GEMINI_API_KEY, pa settings.json."""
    s = {"key": os.environ.get("GEMINI_API_KEY", ""), "model": DEFAULT_MODEL}
    try:
        saved = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
        s["key"] = saved.get("key", s["key"])
        s["model"] = saved.get("model", s["model"]) or DEFAULT_MODEL
    except (OSError, ValueError, AttributeError):
        pass  # nema fajla ili je ostecen: koriste se podrazumevane vrednosti
    return s


def save_settings(s):
    """Vraca True ako je upis uspeo."""
    try:
        SETTINGS_FILE.write_text(json.dumps(s, indent=2), encoding="utf-8")
        return True
    except OSError:
        return False


# ---------------- prikaz poruka ----------------
def load_history():
    """Cita sacuvan razgovor; vraca samo ispravne poruke (user/assistant sa tekstom)."""
    try:
        data = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        return [m for m in data if m.get("role") in ("user", "assistant") and m.get("content")]
    except (OSError, ValueError, AttributeError):
        return []


def save_history(history):
    """Cuva razgovor; ako upis ne uspe, ignorise (istorija je samo pogodnost)."""
    try:
        HISTORY_FILE.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        pass  # istorija je samo pogodnost; igra radi i bez nje


def shown_from(history):
    """Lista (ko, tekst) za prikaz: pozdrav pa sve poruke iz istorije."""
    return [("bot", WELCOME)] + [
        ("me" if m["role"] == "user" else "bot", m["content"]) for m in history
    ]

def _plain_html(lines):
    """Obican tekst u HTML: escape, **podebljano** i `kod` u liniji."""
    part = html.escape("\n".join(lines))
    part = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", part)
    part = re.sub(
        r"`([^`]+)`",
        r'<span style="background-color:#e3d6aa; font-family:Consolas;">\1</span>',
        part,
    )
    return part.replace("\n", "<br>")


def fmt(text):
    """Pretvara tekst sa ``` blokovima u HTML koji Qt razume.

    Blok koda se otvara i zatvara samo linijom koja POCINJE sa ```, pa neparan
    broj ``` usred teksta ne pretvara ostatak poruke u kod. Blok koji se jos
    strimuje (nije zatvoren) se prikazuje kao kod do kraja teksta.
    """
    out, buf, in_code = [], [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            if in_code:
                out.append(f"<pre {PRE}>{html.escape(chr(10).join(buf))}</pre>")
            elif buf:
                out.append(_plain_html(buf))
            buf, in_code = [], not in_code
        else:
            buf.append(line)
    if in_code:
        out.append(f"<pre {PRE}>{html.escape(chr(10).join(buf))}</pre>")
    elif buf:
        out.append(_plain_html(buf))
    return "".join(out)


def bubble(role, body):
    """Jedan balon poruke kao HTML tabela (QTextBrowser razume samo osnovni HTML)."""
    body = body or "..."
    if role == "me":
        return (
            '<table width="100%" cellspacing="6"><tr><td width="15%"></td>'
            f'<td bgcolor="#ffd43b" style="padding:8px; color:#101826;">{body}</td>'
            "</tr></table>"
        )
    return (
        '<table width="100%" cellspacing="6"><tr>'
        f'<td bgcolor="#f4e9c8" style="padding:8px; color:#101826;">{body}</td>'
        '<td width="15%"></td></tr></table>'
    )


# ---------------- Gemini ----------------
class Worker(QThread):
    """Nit koja poziva Gemini. Signali: chunk (deo odgovora) i failed (poruka o gresci)."""
    chunk = Signal(str)
    failed = Signal(str)

    def __init__(self, key, model, messages):
        """Pamti kljuc, model i poruke koje se salju."""
        super().__init__()
        self.key = key
        self.model = model
        self.messages = messages

    def run(self):
        """Salje razgovor modelu i emituje odgovor deo po deo. Greske prevodi u poruke
        razumljive ucenicima (neispravan kljuc, nepostojeci model, ogranicenje).
        """
        if not self.key:
            self.failed.emit("Nema API kljuca. Pritisni ACCOUNT i nalepi kljuc.")
            return
        try:
            # biblioteka se uvozi tek ovde, da igra radi i kad google-genai nije instaliran
            from google import genai
            from google.genai import types
        except ImportError:
            self.failed.emit("Nedostaje biblioteka. U terminalu ukucaj: pip install google-genai")
            return
        try:
            client = genai.Client(api_key=self.key)
            contents = [
                types.Content(
                    # Gemini zove odgovore asistenta ulogom 'model'
                    role="model" if m["role"] == "assistant" else "user",
                    parts=[types.Part(text=m["content"])],
                )
                for m in self.messages
            ]
            config = types.GenerateContentConfig(system_instruction=SYSTEM)
            for part in client.models.generate_content_stream(
                model=self.model, contents=contents, config=config
            ):
                if part.text:
                    self.chunk.emit(part.text)
        except Exception as ex:
            code = getattr(ex, "code", None)
            if code in (400, 401, 403):
                msg = ("Kljuc nije ispravan ili nema pristup (moguce je i da besplatan "
                       "nivo nije dostupan u tvom regionu).")
            elif code == 404:
                msg = f"Model '{self.model}' ne postoji. Promeni ime modela u ACCOUNT."
            elif code == 429:
                msg = "Dostigao si besplatni limit. Probaj kasnije."
            else:
                msg = f"{type(ex).__name__}: {ex}"
            self.failed.emit(msg)


# ---------------- ekrani ----------------
def make_button(text):
    """Zuto dugme istog izgleda kao ostala."""
    b = QPushButton(text)
    b.setObjectName("cbtn")
    b.setCursor(Qt.PointingHandCursor)
    return b


class ChatWidget(QWidget):
    """Ekran sa cetom. history je ono sto se salje modelu, shown ono sto ucenik vidi."""
    open_account = Signal()

    def __init__(self):
        """Ucitava istoriju i gradi izgled; render_timer ogranicava iscrtavanje tokom strimovanja."""
        super().__init__()
        self.setObjectName("chat")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.history = load_history()    # ono sto saljemo modelu
        self.shown = shown_from(self.history)  # ono sto vidi ucenik
        self.worker = None
        self.reply = ""
        # tokom strimovanja ne iscrtavamo ceo razgovor na svaki delic odgovora (sporo),
        # nego najvise jednom na 80 ms
        self.render_timer = QTimer(self)
        self.render_timer.setSingleShot(True)
        self.render_timer.setInterval(80)
        self.render_timer.timeout.connect(self.render)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(10, 10, 10, 10)
        lay.setSpacing(8)

        top = QHBoxLayout()
        self.who = QLabel("")
        self.who.setObjectName("who")
        self.new_btn = make_button("NEW")
        self.acc_btn = make_button("ACCOUNT")
        top.addWidget(self.who, 1)
        top.addWidget(self.new_btn)
        top.addWidget(self.acc_btn)
        lay.addLayout(top)

        self.view = QTextBrowser()
        self.view.document().setDefaultStyleSheet(PAGE_CSS)
        lay.addWidget(self.view, 1)

        row = QHBoxLayout()
        row.setSpacing(6)
        self.input = QLineEdit()
        self.input.setObjectName("cin")
        self.input.setPlaceholderText("Ask about Python...")
        self.send_btn = make_button("SEND")
        row.addWidget(self.input, 1)
        row.addWidget(self.send_btn)
        lay.addLayout(row)

        self.input.returnPressed.connect(self.send)
        self.send_btn.clicked.connect(self.send)
        self.new_btn.clicked.connect(self.reset)
        self.acc_btn.clicked.connect(self.open_account)
        self.refresh_who()
        self.render()

    def refresh_who(self):
        """Prikazuje ime modela ili poruku da nije povezano."""
        s = load_settings()
        self.who.setText(f"Gemini - {s['model']}" if s["key"] else "Nije povezano (ACCOUNT)")

    def render(self):
        """Iscrtava ceo razgovor i skroluje do dna."""
        page = "".join(bubble(role, fmt(text) if text else "") for role, text in self.shown)
        self.view.setHtml(page)
        bar = self.view.verticalScrollBar()
        bar.setValue(bar.maximum())

    def send(self):
        """Dodaje pitanje, pokrece Worker. Modelu se salje poslednjih 20 poruka, a razgovor
        mora da pocne porukom korisnika.
        """
        text = self.input.text().strip()
        if not text or (self.worker and self.worker.isRunning()):
            return
        self.input.clear()
        self.history.append({"role": "user", "content": text})
        # prazan 'bot' balon se puni dok stizu delovi odgovora
        self.shown += [("me", text), ("bot", "")]
        self.render()

        msgs = self.history[-20:]
        # Gemini trazi da razgovor pocne porukom korisnika
        while msgs and msgs[0]["role"] != "user":
            msgs.pop(0)
        self.reply = ""
        s = load_settings()
        self.worker = Worker(s["key"], s["model"], msgs)
        self.worker.chunk.connect(self._on_chunk)
        self.worker.failed.connect(self._on_fail)
        self.worker.finished.connect(self._on_done)
        self.send_btn.setEnabled(False)
        self.worker.start()

    def _on_chunk(self, text):
        """Stigao je deo odgovora: nadovezuje se, a iscrtavanje je najvise jednom u 80 ms."""
        self.reply += text
        self.shown[-1] = ("bot", self.reply)
        if not self.render_timer.isActive():
            self.render_timer.start()

    def _on_fail(self, msg):
        """Greska: prikazi poruku i izbaci pitanje iz istorije (nije dobilo odgovor)."""
        self.reply = ""
        self.shown[-1] = ("bot", msg)
        self.history.pop()  # izbaci pitanje na koje nije stigao odgovor
        self.render()

    def _on_done(self):
        """Nit je zavrsila: konacno iscrtavanje, cuvanje odgovora i ponovo omoguci SEND."""
        self.render_timer.stop()
        self.render()  # poslednje stanje odgovora
        if self.reply:
            self.history.append({"role": "assistant", "content": self.reply})
            save_history(self.history)
        self.send_btn.setEnabled(True)
        self.input.setFocus()

    def reset(self):
        """NEW: brise razgovor (ne dok traje odgovor)."""
        if self.worker and self.worker.isRunning():
            return
        self.history = []
        self.shown = [("bot", WELCOME)]
        save_history([])
        self.render()


KEY_URL = "https://aistudio.google.com/apikey"


def spaced(text):
    """Tekst sa razmakom izmedju redova."""
    return f'<div style="line-height: 170%;">{text}</div>'


class AccountPage(QWidget):
    """Ekran za unos API kljuca i naziva modela; GET KEY otvara Google AI Studio."""
    saved = Signal()
    cancelled = Signal()

    def __init__(self):
        """Gradi polja (kljuc je maskiran) i dugmad."""
        super().__init__()
        self.setObjectName("chat")
        self.setAttribute(Qt.WA_StyledBackground, True)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(18, 18, 18, 18)
        lay.setSpacing(16)

        back = make_button("< CHAT")
        back.clicked.connect(self.cancelled)
        lay.addWidget(back, 0, Qt.AlignLeft)

        title = QLabel("ACCOUNT")
        title.setObjectName("atitle")
        lay.addWidget(title)

        note = QLabel(spaced(
            "Monty Python koristi Google Gemini. Pritisni GET KEY, prijavi se "
            "Google nalogom, napravi besplatan API kljuc i nalepi ga ovde. "
            "Besplatan nivo ima ogranicenja i ne mora biti dostupan u svim regionima."
        ))
        note.setObjectName("anote")
        note.setWordWrap(True)
        lay.addWidget(note)

        get_key = make_button("GET KEY")
        get_key.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(KEY_URL)))
        lay.addWidget(get_key, 0, Qt.AlignLeft)

        k = QLabel("API kljuc")
        k.setObjectName("flabel")
        self.key = QLineEdit()
        self.key.setObjectName("cin")
        self.key.setEchoMode(QLineEdit.Password)
        m = QLabel("Model")
        m.setObjectName("flabel")
        self.model = QLineEdit()
        self.model.setObjectName("cin")
        for w in (k, self.key, m, self.model):
            lay.addWidget(w)

        hint = QLabel(spaced(
            "Ako dobijes poruku da model ne postoji, u AI Studiju pogledaj "
            "aktuelno ime modela i upisi ga ovde."
        ))
        hint.setObjectName("anote")
        hint.setWordWrap(True)
        lay.addWidget(hint)

        save = make_button("SAVE")
        save.clicked.connect(self._save)
        lay.addWidget(save, 0, Qt.AlignLeft)

        self.status = QLabel("")
        self.status.setObjectName("status")
        lay.addWidget(self.status)
        lay.addStretch(1)

    def reload(self):
        """Puni polja trenutno sacuvanim vrednostima."""
        s = load_settings()
        self.key.setText(s["key"])
        self.model.setText(s["model"])
        self.status.setText("")

    def _save(self):
        """Cuva podesavanja; ako upis ne uspe, javlja gresku umesto da se vrati na cet."""
        ok = save_settings({"key": self.key.text().strip(),
                            "model": self.model.text().strip() or DEFAULT_MODEL})
        if ok:
            self.saved.emit()
        else:
            self.status.setText("Podesavanja nije moguce sacuvati (nema prava pisanja).")


class ChatPage(QStackedWidget):
    """Stack: 0 cet, 1 ACCOUNT."""
    def __init__(self):
        """Pravi oba ekrana i povezuje njihove signale."""
        super().__init__()
        self.setStyleSheet(STYLE)
        self.chat = ChatWidget()
        self.account = AccountPage()
        self.addWidget(self.chat)
        self.addWidget(self.account)
        self.chat.open_account.connect(self._open_account)
        self.account.saved.connect(self._back)
        self.account.cancelled.connect(self._back)

    def _open_account(self):
        """Otvara ACCOUNT sa svezim vrednostima."""
        self.account.reload()
        self.setCurrentIndex(1)

    def _back(self):
        """Povratak na cet; osvezava prikaz modela."""
        self.chat.refresh_who()
        self.setCurrentIndex(0)