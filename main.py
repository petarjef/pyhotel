import sys
import ctypes
from pathlib import Path
from PySide6.QtGui import QIcon
from lectures import LecturesPage
from ai import ChatPage
from play import PlayPage
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QPushButton, QStackedWidget, QVBoxLayout, QWidget,
)

BASE = Path(__file__).parent
FONT_PATH = BASE / "assets" / "PressStart2P-Regular.ttf"

STYLE = """
QWidget#root { background: #4672a8; }
QPushButton#tab, QPushButton#play {
    background: #1d2f4a; color: #9fb6d6; border: none;
    border-right: 2px solid #5d7ea8; padding: 0px; font-size: 10px;
}
QPushButton#play { font-size: 14px; color: #ffd43b; }
QPushButton#tab:hover, QPushButton#play:hover { background: #26405f; }
QPushButton#tab:pressed, QPushButton#play:pressed,
QPushButton#tab:checked, QPushButton#play:checked {
    background: #ffd43b; color: #101826;
}
QLabel#page { color: #ffffff; font-size: 12px; }
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("root")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("Python Hotel")
        self.resize(460, 816)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        #Header sa tri taba
        header = QHBoxLayout()
        header.setSpacing(0)
        self.stack = QStackedWidget()
        group = QButtonGroup(self)
        group.setExclusive(True)

        tabs = [("Lectures", 20), ("PLAY", 23), ("Help AI", 20)]
        for i, (title, stretch) in enumerate(tabs):
            btn = QPushButton(title)
            btn.setObjectName("play" if title == "PLAY" else "tab")
            if title == "PLAY":
                btn.setProperty("class", "tab")
            btn.setCheckable(True)
            btn.setFixedHeight(56)
            btn.setCursor(Qt.PointingHandCursor)
            group.addButton(btn, i)
            header.addWidget(btn, stretch)
            btn.clicked.connect(lambda _=False, idx=i: self.stack.setCurrentIndex(idx))
            if title == "PLAY":
                btn.setChecked(True)

        #Ekrani
        self.stack.addWidget(LecturesPage())
        self.stack.addWidget(PlayPage())
        self.stack.addWidget(ChatPage())
        self.stack.setCurrentIndex(1)

        outer.addLayout(header)
        outer.addWidget(self.stack, 1)


def main():
    try:  # da traka zadataka pokaze nasu ikonicu, a ne Pythonovu
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("pythonhotel.game")
    except Exception:
        pass
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(str(BASE / "assets" / "icon.ico")))

    font_id = QFontDatabase.addApplicationFont(str(FONT_PATH))
    if font_id == -1:
        print("UPOZORENJE: font nije nadjen na putanji:", FONT_PATH)
    else:
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        app.setFont(QFont(family))
        print("Font ucitan:", family)

    app.setStyleSheet(STYLE)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


main()