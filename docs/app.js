"use strict";
/* Python Hotel - web verzija. Podaci dolaze iz data.js (generise ga build_web_data.py). */

const { lessons: LESSONS, quiz: QUIZ, code: CODE, topics: TOPICS } = window.HOTEL_DATA;
const LEVELS = 12;
const UNLOCK_ALL = true;        // namerno: svi spratovi otkljucani; konfete tek kad se zavrse svi
const LENIENT_NUMBERS = true;   // 20 i 20.0 se racunaju kao isti output (vidi sameOutput)
const DEFAULT_MODEL = "gemini-3.1-flash-lite";

const $ = (id) => document.getElementById(id);
const store = {
  get(k, d) { try { const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch { return d; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* privatni mod */ } },
};

/* ---------------- progres ---------------- */
const progress = {
  solved: new Set(store.get("pyhotel.solved", [])),
  mark(f, l) { this.solved.add(`${f}-${l}`); store.set("pyhotel.solved", [...this.solved].sort()); },
  is(f, l) { return this.solved.has(`${f}-${l}`); },
  doneCount(f) { let n = 0; while (n < LEVELS && this.is(f, n + 1)) n++; return n; },
};

/* ---------------- tabovi ---------------- */
function showTab(name) {
  document.querySelectorAll("#tabs button").forEach((b) => b.classList.toggle("on", b.dataset.tab === name));
  document.querySelectorAll(".page").forEach((p) => p.classList.toggle("on", p.id === "page-" + name));
  if (name === "play") hotel.draw();
}
document.querySelectorAll("#tabs button").forEach((b) => b.addEventListener("click", () => showTab(b.dataset.tab)));

function showView(page, id) {
  document.querySelectorAll(`#page-${page} .view`).forEach((v) => (v.hidden = v.id !== id));
}

/* ---------------- lectures ---------------- */
const BOOK_BASE = "https://dazdejkovic.github.io/OI_25_jb1/";
$("topics").innerHTML = TOPICS.slice(1).map((s) =>
  `<div class="topic-h">${esc(s.title)}</div>` + s.items.map((t) =>
    `<a class="topic" href="${BOOK_BASE}${esc(t.file)}" target="_blank" rel="noopener">${esc(t.title)}</a>`
  ).join("")
).join("");

function esc(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

/* ---------------- pozadina (nebo, zvezde, oblaci) ---------------- */
const sky = (() => {
  const c = $("sky"), x = c.getContext("2d");
  let tick = 0;
  const STARS = [[20, 30, 2], [90, 80, 2], [160, 20, 3], [60, 140, 2], [210, 110, 2]];
  const CLOUDS = [[70, 1.0, 0], [230, 0.7, 380]];
  function draw() {
    const dpr = window.devicePixelRatio || 1, w = innerWidth, h = innerHeight;
    if (c.width !== Math.round(w * dpr) || c.height !== Math.round(h * dpr)) { c.width = Math.round(w * dpr); c.height = Math.round(h * dpr); }
    x.setTransform(dpr, 0, 0, dpr, 0, 0);
    const g = x.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, "#2d4f80"); g.addColorStop(0.55, "#4672a8"); g.addColorStop(1, "#7fa6d4");
    x.fillStyle = g; x.fillRect(0, 0, w, h);
    x.fillStyle = "rgba(255,255,255,0.55)";
    for (let ty = 0; ty < h + 170; ty += 170) for (let tx = 0; tx < w + 240; tx += 240)
      for (const [sx, sy, s] of STARS) x.fillRect(tx + sx, ty + sy, s, s);
    x.fillStyle = "#d4e4f7";
    for (const [cy, k, phase] of CLOUDS) {
      const cx = ((tick + phase) % (w + 240)) - 120;
      for (const [ox, oy] of [[0, 0], [16, -12], [32, 0], [-8, 8]])
        x.fillRect(Math.floor(cx + ox * k), Math.floor(cy + oy * k), Math.floor(64 * k), Math.floor(16 * k));
    }
  }
  draw();
  addEventListener("resize", draw);
  if (!matchMedia("(prefers-reduced-motion: reduce)").matches)
    setInterval(() => { if (!document.hidden) { tick++; draw(); } }, 60);
})();

/* ---------------- hotel ---------------- */
const hotel = (() => {
  const canvas = $("hotel"), ctx = canvas.getContext("2d");
  const DARK = "#0d1828", BRICK = "#b5523b", BRICK_D = "#8a3b2a", ROOF_BG = "#8a3b2a", LEDGE = "#5c2a1e";
  const SIGN_BG = "#7d9cc4", SIGN_HI = "#101826", INK = "#101826";
  const W = 320, BX = 32, BW = 256, FLOOR_H = 96;
  const TOP = 100, ANT_H = 22, SIGN_H = 62, SIGN_W = 190, ROOF_H = 20, LOBBY_H = 112;
  const n = LESSONS.length;
  const yAnt = TOP, ySign = TOP + ANT_H - 2, yRoof = ySign + SIGN_H - 4, yFloors = yRoof + ROOF_H;
  const yLobby = yFloors + n * FLOOR_H, H = yLobby + LOBBY_H;
  const logo = new Image(); logo.src = "assets/python_logo.png"; logo.onload = () => draw();
  let confetti = [], tick = 0, doorHover = false;

  const fr = (x, y, w, h, c) => { ctx.fillStyle = c; ctx.fillRect(Math.floor(x), Math.floor(y), Math.floor(w), Math.floor(h)); };
  const floorDone = (i) => progress.doneCount(i + 1) >= LEVELS;
  const allDone = () => { const f = Object.keys(QUIZ).map((k) => +k - 1); return f.length > 0 && f.every(floorDone); };
  const floorState = (i) => floorDone(i) ? "done" : (UNLOCK_ALL || [...Array(i).keys()].every(floorDone) ? "cur" : "locked");

  function setup() {
    const dpr = window.devicePixelRatio || 1;
    canvas.width = W * dpr; canvas.height = H * dpr;
    canvas.style.width = W + "px"; canvas.style.height = H + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.imageSmoothingEnabled = true;
  }

  function elide(text, maxW) {
    if (ctx.measureText(text).width <= maxW) return text;
    while (text.length > 1 && ctx.measureText(text + "…").width > maxW) text = text.slice(0, -1);
    return text + "…";
  }

  function doorRect() { return { x: W / 2 - 32, y: yLobby + 36, w: 64, h: 72 }; }

  function paintTop(cx) {
    fr(cx - 3, yAnt, 6, ANT_H, DARK);
    const rx = cx - 136, ry = yRoof;
    fr(rx, ry, 272, ROOF_H, DARK); fr(rx + 4, ry + 4, 264, ROOF_H - 8, ROOF_BG);
    const lx = cx - 144;
    fr(lx, ry + 10, 288, 10, DARK); fr(lx + 4, ry + 10, 280, 6, LEDGE);
    const x = cx - SIGN_W / 2, y = ySign;
    fr(x + 6, y + 6, SIGN_W, SIGN_H, DARK); fr(x, y, SIGN_W, SIGN_H, DARK);
    fr(x + 4, y + 4, SIGN_W - 8, SIGN_H - 8, SIGN_HI); fr(x + 7, y + 7, SIGN_W - 14, SIGN_H - 14, SIGN_BG);
    if (logo.complete && logo.naturalWidth) ctx.drawImage(logo, x + 18, y + (SIGN_H - 36) / 2, 36, 36);
    ctx.font = '16px "Press Start 2P"'; ctx.textAlign = "left"; ctx.textBaseline = "alphabetic";
    const tx = x + 18 + 36 + 12, ty = y + SIGN_H / 2 + 8;
    ctx.fillStyle = DARK; ctx.fillText("PYTHON", tx + 3, ty + 3);
    ctx.fillStyle = "#fff"; ctx.fillText("PYTHON", tx, ty);
  }

  function paintFloor(y, i) {
    const st = floorState(i), x = BX;
    fr(x, y, BW, FLOOR_H, BRICK);
    for (let by = 0; by < FLOOR_H; by += 16) fr(x, y + by, BW, 4, BRICK_D);
    for (let k = 0, by = 0; by < FLOOR_H; by += 32, k++)
      for (let bx = (k % 2) * 32; bx < BW; bx += 64) fr(x + bx, y + by, 4, 32, BRICK_D);
    if (st === "locked") { ctx.fillStyle = "rgba(0,0,0,0.27)"; ctx.fillRect(x, y, BW, FLOOR_H); }
    fr(x, y, 4, FLOOR_H, DARK); fr(x + BW - 4, y, 4, FLOOR_H, DARK); fr(x, y + FLOOR_H - 4, BW, 4, DARK);
    for (const wx of [28, 106, 184]) {
      const X = x + wx, Y = y + 23;
      let fill = "#ffd43b", shade = "#e0a800", hi = "#fff3a8";
      if (st === "locked") { fill = "#243246"; shade = "#1a2433"; hi = null; }
      fr(X, Y, 44, 50, DARK); fr(X + 4, Y + 4, 36, 42, fill);
      if (hi) { fr(X + 4, Y + 4, 36, 4, hi); fr(X + 4, Y + 4, 4, 42, hi); }
      fr(X + 4, Y + 38, 36, 8, shade); fr(X + 20, Y, 4, 50, DARK);
    }
  }

  function paintPlate(y, i) {
    const st = floorState(i);
    ctx.font = '8px "Press Start 2P"'; ctx.textAlign = "center"; ctx.textBaseline = "middle";
    const txt = elide(`${i + 1}. ${LESSONS[i]}`, BW - 60);
    const bw = Math.ceil(ctx.measureText(txt).width) + 24, bh = 30;
    const bx = Math.floor(W / 2 - bw / 2), by = y - 4;
    const color = { cur: "#ffd43b", done: "#6bd16b", locked: "#8b8f98" }[st];
    fr(bx + 3, by + 3, bw, bh, DARK); fr(bx, by, bw, bh, DARK); fr(bx + 4, by + 4, bw - 8, bh - 8, color);
    ctx.fillStyle = INK; ctx.fillText(txt, bx + bw / 2, by + bh / 2 + 1);
    const badge = `${progress.doneCount(i + 1)}/${LEVELS}`;
    const bw2 = Math.ceil(ctx.measureText(badge).width) + 12;
    const bx2 = BX + BW - 4 - 8 - bw2, by2 = y + FLOOR_H - 4 - 6 - 18;
    fr(bx2, by2, bw2, 18, DARK);
    ctx.fillStyle = "#fff"; ctx.fillText(badge, bx2 + bw2 / 2, by2 + 10);
  }

  function paintLobby(cx) {
    const lx = cx - 152, ly = yLobby;
    fr(lx, ly, 304, LOBBY_H, DARK); fr(lx + 4, ly + 4, 296, LOBBY_H - 8, "#7a3322");
    fr(lx - 4, ly, 312, 12, DARK); fr(lx, ly + 4, 304, 4, LEDGE);
    ctx.font = '8px "Press Start 2P"'; ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
    ctx.fillStyle = "#000"; ctx.fillText("CODE LAB", cx + 2, ly + 34 + 2);
    ctx.fillStyle = "#ffd43b"; ctx.fillText("CODE LAB", cx, ly + 34);
    const d = doorRect();
    fr(d.x, d.y, 64, 72, DARK); fr(d.x + 4, d.y + 4, 56, 64, doorHover ? "#34506f" : "#243246");
    for (const [rx, ry, rw, rh] of [[4, 4, 56, 4], [4, 64, 56, 4], [4, 4, 4, 64], [56, 4, 4, 64]])
      fr(d.x + rx, d.y + ry, rw, rh, "#ffd43b");
    fr(d.x + 46, d.y + 40, 6, 6, "#ffd43b");
  }

  function draw() {
    if (!document.getElementById("page-play").classList.contains("on") || $("v-hotel").hidden) return;
    if (!canvas.width) setup();
    ctx.clearRect(0, 0, W, H);
    const cx = W / 2;
    paintTop(cx);
    for (let r = 0; r < n; r++) paintFloor(yFloors + r * FLOOR_H, n - 1 - r);
    for (let r = 0; r < n; r++) paintPlate(yFloors + r * FLOOR_H, n - 1 - r);
    paintLobby(cx);
    for (const [x, y, , , color, size] of confetti) fr(x, y, size, size, color);
  }

  function stepConfetti() {
    tick++;
    if (tick % 85 === 0 && allDone()) {
      const cx = W / 2, cols = ["#ffd43b", "#d6336c", "#4b8bbe", "#6bd16b", "#ffffff", "#ff7a1a"];
      for (const [sx, dir] of [[cx - SIGN_W / 2, -1], [cx + SIGN_W / 2, 1]])
        for (let i = 0; i < 24; i++)
          confetti.push([sx, ySign, dir * (0.5 + Math.random() * 3.5), -4 - Math.random() * 5,
            cols[Math.floor(Math.random() * cols.length)], Math.random() < 0.5 ? 4 : 6]);
    }
    if (!confetti.length) return false;
    for (const c of confetti) { c[0] += c[2]; c[1] += c[3]; c[3] += 0.35; }
    confetti = confetti.filter((c) => c[1] < ySign + 260);
    return true;
  }
  setInterval(() => { if (!document.hidden && stepConfetti()) draw(); }, 60);

  function pos(ev) {
    const r = canvas.getBoundingClientRect();
    return { x: (ev.clientX - r.left) * (W / r.width), y: (ev.clientY - r.top) * (H / r.height) };
  }
  function floorAt(p) {
    if (p.x < BX || p.x >= BX + BW || p.y < yFloors) return null;
    const r = Math.floor((p.y - yFloors) / FLOOR_H);
    return r < n ? n - 1 - r : null;
  }
  const inDoor = (p) => { const d = doorRect(); return p.x >= d.x && p.x < d.x + d.w && p.y >= d.y && p.y < d.y + d.h; };

  canvas.addEventListener("mousemove", (ev) => {
    const p = pos(ev), over = inDoor(p), i = floorAt(p);
    canvas.style.cursor = over || (i !== null && floorState(i) !== "locked") ? "pointer" : (i !== null ? "not-allowed" : "default");
    if (over !== doorHover) { doorHover = over; draw(); }
  });
  canvas.addEventListener("mouseleave", () => { if (doorHover) { doorHover = false; draw(); } });
  canvas.addEventListener("click", (ev) => {
    const p = pos(ev);
    if (inDoor(p)) return openFreeLab();
    const i = floorAt(p);
    if (i !== null && floorState(i) !== "locked") openFloor(i + 1);
  });

  // oblaci sa strelicama
  function cloud(id, up) {
    const c = $(id), x = c.getContext("2d");
    const R = [[4, 20, 52, 16], [12, 10, 36, 10], [22, 2, 18, 8]];
    function paint(hover) {
      x.clearRect(0, 0, 64, 42);
      for (const [off, col] of [[3, DARK], [0, hover ? "#ffffff" : "#e7f0ff"]])
        for (const [rx, ry, rw, rh] of R) { x.fillStyle = col; x.fillRect(rx + off, ry + off, rw, rh); }
      const pts = up ? [[30, 12], [21, 26], [39, 26]] : [[30, 30], [21, 16], [39, 16]];
      x.fillStyle = "#3776ab"; x.beginPath(); x.moveTo(...pts[0]); x.lineTo(...pts[1]); x.lineTo(...pts[2]); x.fill();
    }
    paint(false);
    c.addEventListener("mouseenter", () => paint(true));
    c.addEventListener("mouseleave", () => paint(false));
    c.addEventListener("click", () => $("hotelScroll").scrollBy({ top: up ? -208 : 208, behavior: "smooth" }));
  }
  cloud("cloudUp", true); cloud("cloudDown", false);

  function start() {
    setup(); draw();
    $("hotelScroll").scrollTop = $("hotelScroll").scrollHeight;   // na pocetku prizemlje
  }
  document.fonts.load('8px "Press Start 2P"').then(() => document.fonts.load('16px "Press Start 2P"')).then(() => {
    showTab("play"); start();
  });
  addEventListener("resize", () => { setup(); draw(); });
  return { draw, allDone };
})();

/* ---------------- nivoi, kviz ---------------- */
let cur = { floor: 1, level: 1, from: "levels" };

function getTask(f, l) {
  if (!QUIZ[f] || l < 1 || l > LEVELS) return null;
  if (l % 2 === 1) { const q = QUIZ[f][(l - 1) / 2]; return q && { type: "quiz", ...q }; }
  const c = CODE[f] && CODE[f][l / 2 - 1];
  return c && { type: "code", ...c };
}

function openFloor(n) {
  cur.floor = n;
  showLevels();
}

function showLevels() {
  const n = cur.floor, done = progress.doneCount(n);
  $("levelsTitle").textContent = `Floor ${n}: ${LESSONS[n - 1]}`;
  const grid = $("levelsGrid");
  grid.innerHTML = "";
  if (!QUIZ[n]) { grid.innerHTML = '<p class="note">Zadaci za ovaj sprat stizu uskoro.</p>'; }
  else for (let l = 1; l <= LEVELS; l++) {
    const st = progress.is(n, l) ? "done" : (l === done + 1 ? "cur" : "locked");
    const b = document.createElement("button");
    b.className = "lv " + st; b.textContent = l; b.disabled = st === "locked";
    b.addEventListener("click", () => openLevel(n, l));
    grid.appendChild(b);
  }
  showView("play", "v-levels");
}
$("levelsBack").onclick = () => { showView("play", "v-hotel"); hotel.draw(); };

function openLevel(f, l) {
  cur = { floor: f, level: l, from: "levels" };
  const t = getTask(f, l);
  if (!t) return showLevels();
  const title = `Floor ${f} - Level ${l}`;
  if (t.type === "quiz") loadQuiz(title, t); else loadTask(`${title}  (${LESSONS[f - 1]})\n${t.text}`, t);
}

let quizDone = false;
function loadQuiz(title, t) {
  quizDone = false;
  $("quizTitle").textContent = title;
  $("quizCode").textContent = t.code;
  $("quizMsg").textContent = ""; $("quizNext").hidden = true;
  const box = $("quizOpts"); box.innerHTML = "";
  t.options.forEach((o, k) => {
    const b = document.createElement("button");
    b.textContent = o;
    b.onclick = () => {
      if (quizDone) return;
      if (k === t.answer) {
        quizDone = true; b.classList.add("ok"); $("quizMsg").textContent = "TACNO!"; $("quizNext").hidden = false;
        progress.mark(cur.floor, cur.level);
      } else { b.classList.add("bad"); b.disabled = true; $("quizMsg").textContent = "Netacno, probaj ponovo."; }
    };
    box.appendChild(b);
  });
  showView("play", "v-quiz");
}
$("quizBack").onclick = showLevels;
$("quizNext").onclick = next;

function next() {
  for (let l = cur.level + 1; l <= LEVELS; l++) if (getTask(cur.floor, l)) return openLevel(cur.floor, l);
  showLevels();
}

/* ---------------- Code Lab ---------------- */
// Poredjenje outputa: kao desktop verzija (razmaci na kraju reda se ignorisu),
// plus 20 i 20.0 su isto ako je LENIENT_NUMBERS ukljucen.
function norm(s) { return s.trim().split(/\r?\n/).map((l) => l.replace(/\s+$/, "")).join("\n"); }
function canonNums(s) {
  return s.replace(/(?<![\w.])-?\d+(?:\.\d+)?(?![\w.])/g, (m) => {
    const v = parseFloat(m);
    return Number.isSafeInteger(v) || !Number.isInteger(v) ? String(v) : m;
  });
}
function sameOutput(got, expected) {
  const a = norm(got), b = norm(expected);
  if (a === b) return true;
  return LENIENT_NUMBERS && canonNums(a) === canonNums(b);
}

const lab = (() => {
  let worker = null, running = false, checking = false, captured = "", expected = null, workerReady = false;
  const code = $("labCode"), out = $("labOut"), status = $("labStatus"), stdin = $("labStdinBox");

  function newWorker() {
    if (worker) worker.terminate();
    workerReady = false;
    worker = new Worker("pyworker.js");
    worker.onmessage = (e) => {
      const m = e.data;
      if (m.t === "out") write(m.s);
      else if (m.t === "status") status.textContent = m.s;
      else if (m.t === "ready") { workerReady = true; status.textContent = "Python je spreman."; }
      else if (m.t === "figs") m.figs.forEach((b64) => { const im = new Image(); im.src = "data:image/png;base64," + b64; $("labImgs").appendChild(im); });
      else if (m.t === "fatal") { write("Python nije mogao da se ucita: " + m.s + "\n"); workerReady = false; setRunning(false); }
      else if (m.t === "done") finish();
    };
    worker.onerror = (e) => { write("[greska u radniku: " + (e.message || "nepoznata") + "]\n"); setRunning(false); };
  }
  function write(s) { out.textContent += s; if (checking) captured += s; out.scrollTop = out.scrollHeight; }

  function setRunning(on) {
    running = on;
    $("labRun").disabled = on; $("labStop").disabled = !on; $("labCheck").disabled = on;
    if (!on) status.textContent = workerReady ? "Python je spreman." : "";
  }

  function run(isCheck) {
    if (running) return;
    if (!worker) newWorker();
    out.textContent = ""; $("labImgs").innerHTML = "";
    checking = isCheck; captured = "";
    setRunning(true);
    status.textContent = "Pokrecem...";
    worker.postMessage({ t: "run", code: code.value, stdin: stdin.value ? stdin.value.split("\n") : [] });
  }

  function finish() {
    const wasChecking = checking;
    checking = false; setRunning(false);
    if (!wasChecking || expected === null) return;
    if (sameOutput(captured, expected)) {
      out.textContent += "\n>>> TACNO!";
      $("labNext").hidden = false;
      progress.mark(cur.floor, cur.level);
    } else {
      out.textContent += "\n>>> JOS NE. Trazeni output:\n" + expected;
    }
  }

  function stop() { if (!running) return; newWorker(); setRunning(false); checking = false; out.textContent += "\n[zaustavljeno]"; }
  function reset() { newWorker(); setRunning(false); checking = false; out.textContent = "Python restarted. All variables are cleared."; $("labImgs").innerHTML = ""; }

  function start(taskText, starter, exp, free) {
    expected = exp; checking = false;
    $("labTask").textContent = taskText;
    code.value = starter; out.textContent = ""; $("labImgs").innerHTML = "";
    $("labCheck").hidden = free; $("labNext").hidden = true;
    stdin.value = ""; syncStdin();
    showView("play", "v-lab");
    if (!worker) newWorker();   // zagrej Python dok korisnik cita zadatak
    setRunning(false);
  }

  function syncStdin() { stdin.hidden = !/\binput\s*\(/.test(code.value); }

  $("labRun").onclick = () => run(false);
  $("labCheck").onclick = () => run(true);
  $("labStop").onclick = stop;
  $("labReset").onclick = reset;
  $("labNext").onclick = next;
  $("labBack").onclick = () => { if (cur.from === "levels") showLevels(); else { showView("play", "v-hotel"); hotel.draw(); } };
  code.addEventListener("input", syncStdin);
  code.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) { e.preventDefault(); run(false); return; }
    if (e.key === "Tab") { e.preventDefault(); document.execCommand("insertText", false, "    "); return; }
    if (e.key === "Enter") {
      e.preventDefault();
      const pos = code.selectionStart, before = code.value.slice(0, pos);
      const line = before.slice(before.lastIndexOf("\n") + 1);
      let indent = line.match(/^\s*/)[0];
      if (line.trimEnd().endsWith(":")) indent += "    ";
      document.execCommand("insertText", false, "\n" + indent);
    }
  });
  return { start };
})();

function loadTask(text, t) { cur.from = "levels"; lab.start(text, t.starter, t.expected, false); }
function openFreeLab() {
  cur.from = "hotel";
  lab.start("CODE LAB: pisi Python i pritisni RUN (ili Ctrl+Enter).", "", null, true);
}

/* ---------------- AI tutor (Gemini) ---------------- */
const SYSTEM =
  "You are Monty Python, the friendly tutor inside a Python learning game for university students. " +
  "Only answer questions about Python programming and the topics of the course (variables, strings, lists, " +
  "modules, conditions, loops, functions, files, classes, NumPy, Pandas, basic machine learning). If asked " +
  "about anything else, politely decline in one sentence and steer back to Python. Reply in the language the " +
  "student writes in (Serbian by default, Latin script). Keep answers short and beginner-friendly. Put code in " +
  "triple-backtick blocks. When a student is stuck on an exercise, prefer a hint or explanation first and show " +
  "the full solution only if they ask again.";
const WELCOME = "Hi! I'm Monty Python. Ask me anything about Python.";

// Markdown-lite: blok koda se otvara/zatvara samo linijom koja POCINJE sa ```,
// pa neparan broj ``` usred teksta ne pokvari ostatak poruke.
function fmt(text) {
  const out = []; let inCode = false, buf = [];
  const flushText = () => {
    if (!buf.length) return;
    out.push(esc(buf.join("\n")).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/`([^`\n]+)`/g, "<code>$1</code>").replace(/\n/g, "<br>"));
    buf = [];
  };
  const flushCode = () => { out.push(`<pre>${esc(buf.join("\n"))}</pre>`); buf = []; };
  for (const line of text.split("\n")) {
    if (/^\s*```/.test(line)) {
      if (inCode) { flushCode(); inCode = false; } else { flushText(); inCode = true; }
    } else buf.push(line);
  }
  inCode ? flushCode() : flushText();
  return out.join("");
}

const chat = (() => {
  const log = $("chatLog"), input = $("chatInput");
  let history = store.get("pyhotel.chat", []);     // [{role:"me"|"assistant", content}]
  let busy = false;
  const settings = () => ({ key: "", model: DEFAULT_MODEL, ...store.get("pyhotel.ai", {}) });

  function bubble(role, html) {
    const d = document.createElement("div"); d.className = "msg " + role;
    d.innerHTML = `<div>${html}</div>`; log.appendChild(d); log.scrollTop = log.scrollHeight;
    return d.firstChild;
  }
  function render() {
    log.innerHTML = "";
    bubble("bot", esc(WELCOME));
    for (const m of history) bubble(m.role === "me" ? "me" : "bot", fmt(m.content));
    $("aiWho").textContent = "Monty Python · " + settings().model;
  }

  async function send(text) {
    const s = settings();
    if (!s.key) return bubble("err", "Nema API kljuca. Pritisni ACCOUNT i nalepi kljuc.");
    busy = true; $("chatSend").disabled = true;
    history.push({ role: "me", content: text });
    bubble("me", fmt(text));
    const target = bubble("bot", "...");
    let acc = "";
    try {
      const contents = history.slice(-30).map((m) => ({ role: m.role === "me" ? "user" : "model", parts: [{ text: m.content }] }));
      const res = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(s.model)}:streamGenerateContent?alt=sse`,
        { method: "POST", headers: { "Content-Type": "application/json", "x-goog-api-key": s.key },
          body: JSON.stringify({ systemInstruction: { parts: [{ text: SYSTEM }] }, contents }) });
      if (!res.ok) throw { status: res.status };
      const reader = res.body.getReader(), dec = new TextDecoder();
      let buf = "";
      for (;;) {
        const { done, value } = await reader.read();
        if (done) break;
        buf += dec.decode(value, { stream: true });
        let nl;
        while ((nl = buf.indexOf("\n")) >= 0) {
          const line = buf.slice(0, nl).trim(); buf = buf.slice(nl + 1);
          if (!line.startsWith("data:")) continue;
          try {
            const j = JSON.parse(line.slice(5));
            const parts = (j.candidates && j.candidates[0] && j.candidates[0].content && j.candidates[0].content.parts) || [];
            for (const p of parts) if (p.text) { acc += p.text; target.innerHTML = fmt(acc); log.scrollTop = log.scrollHeight; }
          } catch { /* nepotpun chunk */ }
        }
      }
      history.push({ role: "assistant", content: acc || "(prazan odgovor)" });
      if (!acc) target.textContent = "(prazan odgovor)";
    } catch (ex) {
      history.pop();   // izbaci pitanje koje nije dobilo odgovor
      const c = ex && ex.status;
      let msg = "Greska: " + ((ex && ex.message) || "mreza ili CORS");
      if (c === 400 || c === 401 || c === 403) msg = "Kljuc nije ispravan ili nema pristup (moguce je i da besplatan nivo nije dostupan u tvom regionu).";
      else if (c === 404) msg = `Model '${s.model}' ne postoji. Promeni ime modela u ACCOUNT.`;
      else if (c === 429) msg = "Dostigao si besplatni limit. Probaj kasnije.";
      target.parentElement.className = "msg err"; target.textContent = msg;
    }
    store.set("pyhotel.chat", history.slice(-60));
    busy = false; $("chatSend").disabled = false;
  }

  $("chatForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const t = input.value.trim();
    if (!t || busy) return;
    input.value = ""; send(t);
  });
  $("aiClear").onclick = () => { if (busy) return; history = []; store.set("pyhotel.chat", []); render(); };
  $("aiAccount").onclick = () => {
    const s = settings(); $("accKey").value = s.key; $("accModel").value = s.model; $("accStatus").textContent = "";
    showView("ai", "v-account");
  };
  $("accBack").onclick = () => { showView("ai", "v-chat"); render(); };
  $("accSave").onclick = () => {
    store.set("pyhotel.ai", { key: $("accKey").value.trim(), model: $("accModel").value.trim() || DEFAULT_MODEL });
    $("accStatus").textContent = "Sacuvano.";
  };
  render();
})();

showTab("play");
