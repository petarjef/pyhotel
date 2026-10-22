from pathlib import Path
import random
from PySide6.QtCore import QPoint, QPropertyAnimation, QRect, Qt, QTimer, Signal
from PySide6.QtGui import (
    QColor, QFont, QFontMetrics, QLinearGradient, QPainter,
    QPixmap, QPolygon,
)
from PySide6.QtWidgets import (
    QApplication, QPushButton, QScrollArea, QVBoxLayout, QWidget,
)

from lectures import SECTIONS
import progress
import tasks

BASE = Path(__file__).parent

# ---- Podaci ----
SKIP = {"ML_25_01_Uvod_1.html"}  # lekcije koje nemaju sprat
LESSONS = [
    title
    for _, items in SECTIONS[1:]
    for file, title in items
    if file not in SKIP
]
LEVELS = 12        # nivoa po spratu
DONE_FLOORS = 0    # koliko spratova je zavrseno (kasnije iz sacuvanog progresa)
PROGRESS = {}      # sprat (0, 1, 2...) -> koliko nivoa je zavrseno

# ---- Boje ----
DARK = "#0d1828"
BRICK, BRICK_D = "#b5523b", "#8a3b2a"
ROOF_BG, LEDGE = "#8a3b2a", "#5c2a1e"
SIGN_BG = "#7d9cc4"   # BILBORD: boja pozadine (menjaj ovde)
SIGN_HI = "#101826"   # svetlija ivica unutar bilborda
PAPER, INK = "#f4e9c8", "#101826"

# ---- Mere ----
W = 320
BX, BW = 32, 256      # pozicija i sirina zgrade
FLOOR_H = 96
TOP, ANT_H, SIGN_H, SIGN_W, ROOF_H, LOBBY_H = 100, 22, 62, 190, 20, 112

STARS = [(20, 30, 2), (90, 80, 2), (160, 20, 3), (60, 140, 2), (210, 110, 2)]
CLOUDS = [(70, 1.0, 0), (230, 0.7, 380)]  # (y, velicina, pocetni pomak)


def fr(p, x, y, w, h, color):
    p.fillRect(int(x), int(y), int(w), int(h), QColor(color))


def floor_done(i):
    return progress.done_count(i + 1) >= LEVELS


UNLOCK_ALL = True  # namerno: svi spratovi otkljucani; konfete tek kad se zavrse svi


def floor_state(i):
    if floor_done(i):
        return "done"
    if UNLOCK_ALL:
        return "cur"
    return "cur" if all(floor_done(k) for k in range(i)) else "locked"

def all_done():
    floors = [i for i in range(len(LESSONS)) if (i + 1) in tasks.QUIZ]
    return bool(floors) and all(floor_done(i) for i in floors)


class Hotel(QWidget):
    floor_clicked = Signal(int)
    door_clicked = Signal()

    def __init__(self):
        super().__init__()
        self.n = len(LESSONS)
        self.y_ant = TOP
        self.y_sign = TOP + ANT_H - 2
        self.y_roof = self.y_sign + SIGN_H - 4
        self.y_floors = self.y_roof + ROOF_H
        self.y_lobby = self.y_floors + self.n * FLOOR_H
        self.setFixedSize(W, self.y_lobby + LOBBY_H)
        self.setMouseTracking(True)
        self.blink = False
        self.door_hover = False
        self.confetti = []

        base = QFont(QApplication.font())
        self.f8 = QFont(base)
        self.f8.setPixelSize(8)
        self.f16 = QFont(base)
        self.f16.setPixelSize(16)
        logo = QPixmap(str(BASE / "assets" / "python_logo.png"))
        self.logo = logo.scaled(36, 36, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def step_confetti(self, tick):
        if tick % 85 == 0 and all_done():  # novi talas na svakih ~5 sekundi
            cx = W // 2
            for sx, direction in ((cx - SIGN_W // 2, -1), (cx + SIGN_W // 2, 1)):
                for _ in range(24):
                    self.confetti.append([
                        sx, self.y_sign,
                        direction * random.uniform(0.5, 4),
                        random.uniform(-9, -4),
                        random.choice(["#ffd43b", "#d6336c", "#4b8bbe", "#6bd16b", "#ffffff", "#ff7a1a"]),
                        random.choice((4, 6)),
                    ])
        if not self.confetti:
            return
        for c in self.confetti:
            c[0] += c[2]
            c[1] += c[3]
            c[3] += 0.35  # gravitacija
        self.confetti = [c for c in self.confetti if c[1] < self.y_sign + 260]

    # ---------- crtanje ----------
    def paintEvent(self, ev):
        p = QPainter(self)
        cx = W // 2
        top, bot = ev.rect().top(), ev.rect().bottom()

        if top < self.y_floors + 4:
            self._paint_top(p, cx)

        for r in range(self.n):
            y = self.y_floors + r * FLOOR_H
            if y > bot + 12 or y + FLOOR_H < top - 12:
                continue
            self._paint_floor(p, y, self.n - 1 - r)

        for r in range(self.n):
            y = self.y_floors + r * FLOOR_H
            if y > bot + 12 or y + FLOOR_H < top - 12:
                continue
            self._paint_plate(p, y, self.n - 1 - r)

        if bot > self.y_lobby - 20:
            self._paint_lobby(p, cx)
        for x, y, _vx, _vy, color, size in self.confetti:
            p.fillRect(int(x), int(y), size, size, QColor(color))
        p.end()

    def _paint_top(self, p, cx):
        fr(p, cx - 3, self.y_ant, 6, ANT_H, DARK)  # antena

        # krov + ispust
        rx, ry = cx - 136, self.y_roof
        fr(p, rx, ry, 272, ROOF_H, DARK)
        fr(p, rx + 4, ry + 4, 264, ROOF_H - 8, ROOF_BG)
        lx = cx - 144
        fr(p, lx, ry + 10, 288, 10, DARK)
        fr(p, lx + 4, ry + 10, 280, 6, LEDGE)

        # bilbord
        x, y = cx - SIGN_W // 2, self.y_sign
        fr(p, x + 6, y + 6, SIGN_W, SIGN_H, DARK)
        fr(p, x, y, SIGN_W, SIGN_H, DARK)
        fr(p, x + 4, y + 4, SIGN_W - 8, SIGN_H - 8, SIGN_HI)
        fr(p, x + 7, y + 7, SIGN_W - 14, SIGN_H - 14, SIGN_BG)
        if not self.logo.isNull():
            p.drawPixmap(x + 18, y + (SIGN_H - 36) // 2, self.logo)
        p.setFont(self.f16)
        tx, ty = x + 18 + 36 + 12, y + SIGN_H // 2 + 8
        p.setPen(QColor(DARK))
        p.drawText(tx + 3, ty + 3, "PYTHON")
        p.setPen(QColor("#ffffff"))
        p.drawText(tx, ty, "PYTHON")

    def _paint_floor(self, p, y, i):
        state = floor_state(i)
        x = BX
        fr(p, x, y, BW, FLOOR_H, BRICK)
        for by in range(0, FLOOR_H, 16):
            fr(p, x, y + by, BW, 4, BRICK_D)
        for k, by in enumerate(range(0, FLOOR_H, 32)):
            for bx in range((k % 2) * 32, BW, 64):
                fr(p, x + bx, y + by, 4, 32, BRICK_D)
        if state == "locked":
            p.fillRect(x, y, BW, FLOOR_H, QColor(0, 0, 0, 70))
        fr(p, x, y, 4, FLOOR_H, DARK)
        fr(p, x + BW - 4, y, 4, FLOOR_H, DARK)
        fr(p, x, y + FLOOR_H - 4, BW, 4, DARK)

        for wx in (28, 106, 184):
            X, Y = x + wx, y + 23
            if state == "locked":
                fill, shade, hi = "#243246", "#1a2433", None
            else:
                fill = "#ffd43b"
                shade, hi = "#e0a800", "#fff3a8"
            fr(p, X, Y, 44, 50, DARK)
            fr(p, X + 4, Y + 4, 36, 42, fill)
            if hi:
                fr(p, X + 4, Y + 4, 36, 4, hi)
                fr(p, X + 4, Y + 4, 4, 42, hi)
            fr(p, X + 4, Y + 38, 36, 8, shade)
            fr(p, X + 20, Y, 4, 50, DARK)

    def _paint_plate(self, p, y, i):
        state = floor_state(i)
        p.setFont(self.f8)
        fm = QFontMetrics(self.f8)
        txt = fm.elidedText(f"{i + 1}. {LESSONS[i]}", Qt.ElideRight, BW - 60)
        extra = 0
        bw, bh = fm.horizontalAdvance(txt) + 24 + extra, 30
        bx, by = W // 2 - bw // 2, y - 4
        color = {"cur": "#ffd43b", "done": "#6bd16b", "locked": "#8b8f98"}[state]
        fr(p, bx + 3, by + 3, bw, bh, DARK)
        fr(p, bx, by, bw, bh, DARK)
        fr(p, bx + 4, by + 4, bw - 8, bh - 8, color)
        p.setPen(QColor(INK))
        p.drawText(QRect(bx + 4, by + 4, bw - 8 - extra, bh - 8), Qt.AlignCenter, txt)
        

        # brojac nivoa
        n_done = progress.done_count(i + 1)
        badge = f"{n_done}/{LEVELS}"
        bw2 = fm.horizontalAdvance(badge) + 12
        bx2, by2 = BX + BW - 4 - 8 - bw2, y + FLOOR_H - 4 - 6 - 18
        fr(p, bx2, by2, bw2, 18, DARK)
        p.setPen(QColor("#ffffff"))
        p.drawText(QRect(bx2, by2, bw2, 18), Qt.AlignCenter, badge)

    def _paint_lobby(self, p, cx):
        lx, ly = cx - 152, self.y_lobby
        fr(p, lx, ly, 304, LOBBY_H, DARK)
        fr(p, lx + 4, ly + 4, 296, LOBBY_H - 8, "#7a3322")
        fr(p, lx - 4, ly, 312, 12, DARK)
        fr(p, lx, ly + 4, 304, 4, LEDGE)

        p.setFont(self.f8)
        tw = QFontMetrics(self.f8).horizontalAdvance("CODE LAB")
        p.setPen(QColor("#000000"))
        p.drawText(cx - tw // 2 + 2, ly + 34 + 2, "CODE LAB")
        p.setPen(QColor("#ffd43b"))
        p.drawText(cx - tw // 2, ly + 34, "CODE LAB")

        d = self._door_rect()
        fr(p, d.x(), d.y(), 64, 72, DARK)
        fr(p, d.x() + 4, d.y() + 4, 56, 64, "#34506f" if self.door_hover else "#243246")
        for rx, ry, rw, rh in ((4, 4, 56, 4), (4, 64, 56, 4), (4, 4, 4, 64), (56, 4, 4, 64)):
            fr(p, d.x() + rx, d.y() + ry, rw, rh, "#ffd43b")
        fr(p, d.x() + 46, d.y() + 40, 6, 6, "#ffd43b")

    # ---------- mis ----------
    def _door_rect(self):
        return QRect(W // 2 - 32, self.y_lobby + 36, 64, 72)

    def _floor_at(self, pos):
        if not (BX <= pos.x() < BX + BW) or pos.y() < self.y_floors:
            return None
        r = (pos.y() - self.y_floors) // FLOOR_H
        return self.n - 1 - r if r < self.n else None

    def mouseMoveEvent(self, ev):
        pos = ev.position().toPoint()
        over_door = self._door_rect().contains(pos)
        i = self._floor_at(pos)
        if over_door or (i is not None and floor_state(i) != "locked"):
            self.setCursor(Qt.PointingHandCursor)
        elif i is not None:
            self.setCursor(Qt.ForbiddenCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        if over_door != self.door_hover:
            self.door_hover = over_door
            self.update(self._door_rect())

    def leaveEvent(self, ev):
        if self.door_hover:
            self.door_hover = False
            self.update(self._door_rect())

    def mousePressEvent(self, ev):
        if ev.button() != Qt.LeftButton:
            return
        pos = ev.position().toPoint()
        if self._door_rect().contains(pos):
            self.door_clicked.emit()
            return
        i = self._floor_at(pos)
        if i is not None and floor_state(i) != "locked":
            self.floor_clicked.emit(i + 1)


class Ground(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(64)

    def paintEvent(self, ev):
        p = QPainter(self)
        w, h = self.width(), self.height()
        fr(p, 0, 0, w, h, "#3d8f3d")
        fr(p, 0, 4, w, 8, "#56b356")
        fr(p, 0, 0, w, 4, DARK)
        p.end()


class CloudButton(QPushButton):
    RECTS = [(4, 20, 52, 16), (12, 10, 36, 10), (22, 2, 18, 8)]

    def __init__(self, up):
        super().__init__()
        self.up = up
        self.setFixedSize(64, 42)
        self.setCursor(Qt.PointingHandCursor)

    def enterEvent(self, e):
        self.update()

    def leaveEvent(self, e):
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        fill = "#ffffff" if self.underMouse() else "#e7f0ff"
        for off, color in ((3, DARK), (0, fill)):
            for x, y, w, h in self.RECTS:
                p.fillRect(x + off, y + off, w, h, QColor(color))
        pts = [(30, 12), (21, 26), (39, 26)] if self.up else [(30, 30), (21, 16), (39, 16)]
        p.setPen(Qt.NoPen)
        p.setBrush(QColor("#3776ab"))
        p.drawPolygon(QPolygon([QPoint(x, y) for x, y in pts]))
        p.end()


class HotelPage(QWidget):
    open_lab = Signal()          # vrata -> Code Lab (povezujemo kasnije)
    floor_clicked = Signal(int)  # broj sprata (1, 2, 3...)

    def __init__(self):
        super().__init__()
        self.tick = 0
        self._placed = False

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setStyleSheet(
            "QScrollArea, QScrollArea > QWidget > QWidget"
            " { background: transparent; border: none; }"
        )
        self.scroll.viewport().setAutoFillBackground(False)

        scene = QWidget()
        scene.setAutoFillBackground(False)
        sl = QVBoxLayout(scene)
        sl.setContentsMargins(0, 0, 0, 0)
        sl.setSpacing(0)
        self.hotel = Hotel()
        self.hotel.floor_clicked.connect(self.floor_clicked)
        self.hotel.door_clicked.connect(self.open_lab)
        sl.addWidget(self.hotel, 0, Qt.AlignHCenter)
        sl.addWidget(Ground(), 1)
        self.scroll.setWidget(scene)
        outer.addWidget(self.scroll)

        # Oblaci sa strelicama
        self.clouds = QWidget(self)
        self.clouds.setStyleSheet("background: transparent;")
        from PySide6.QtWidgets import QVBoxLayout as VBox
        cl = VBox(self.clouds)
        cl.setContentsMargins(0, 0, 0, 0)
        cl.setSpacing(10)
        up, down = CloudButton(True), CloudButton(False)
        up.clicked.connect(lambda: self._scroll_by(-208))
        down.clicked.connect(lambda: self._scroll_by(208))
        cl.addWidget(up)
        cl.addWidget(down)
        self.clouds.adjustSize()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._frame)
        self.timer.start(60)

    def _frame(self):
        self.tick += 1
        self.hotel.step_confetti(self.tick)
        if self.tick % 13 == 0:
            self.hotel.blink = not self.hotel.blink
        self.update()

    def paintEvent(self, ev):
        p = QPainter(self)
        w, h = self.width(), self.height()
        g = QLinearGradient(0, 0, 0, h)
        g.setColorAt(0, QColor("#2d4f80"))
        g.setColorAt(0.55, QColor("#4672a8"))
        g.setColorAt(1, QColor("#7fa6d4"))
        p.fillRect(self.rect(), g)

        star = QColor(255, 255, 255, 140)
        for ty in range(0, h + 170, 170):
            for tx in range(0, w + 240, 240):
                for sx, sy, s in STARS:
                    p.fillRect(tx + sx, ty + sy, s, s, star)

        cloud = QColor("#d4e4f7")
        for cy, k, phase in CLOUDS:
            x = (self.tick + phase) % (w + 240) - 120
            for ox, oy in ((0, 0), (16, -12), (32, 0), (-8, 8)):
                p.fillRect(int(x + ox * k), int(cy + oy * k), int(64 * k), int(16 * k), cloud)
        p.end()

    def _scroll_by(self, dy):
        bar = self.scroll.verticalScrollBar()
        self.anim = QPropertyAnimation(bar, b"value", self)
        self.anim.setDuration(250)
        self.anim.setStartValue(bar.value())
        self.anim.setEndValue(max(bar.minimum(), min(bar.maximum(), bar.value() + dy)))
        self.anim.start()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.clouds.adjustSize()
        self.clouds.move(self.width() - self.clouds.width() - 6,
                         (self.height() - self.clouds.height()) // 2)
        self.clouds.raise_()

    def showEvent(self, e):
        super().showEvent(e)
        if not self._placed:  # na pocetku pokazi prizemlje
            self._placed = True
            bar = self.scroll.verticalScrollBar()
            QTimer.singleShot(50, lambda: bar.setValue(bar.maximum()))