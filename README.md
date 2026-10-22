# Python Hotel

An educational game for learning Python. Climb the floors of a pixel-art hotel,
one floor per lesson, by solving quizzes and writing real code.

## Play

| Platform | How |
| --- | --- |
| Browser (any device) | Coming soon |
| Windows | Download `PythonHotel_Setup.exe` from the [latest release](https://github.com/petarjef/pyhotel/releases) |
| Mac | Use the browser version, or run from source (see below) |

The Windows installer downloads Python and everything else it needs, so the
first installation takes a few minutes and needs an internet connection.
Windows may show a "protected your PC" warning because the installer is not
signed. Click **More info**, then **Run anyway**.

## Features

- **Hotel:** every floor is a lesson, with 12 levels each (quizzes and coding tasks).
- **Code Lab:** a built-in Python editor backed by a Jupyter kernel. Variables
  persist between runs, and `input()` works.
- **Lectures:** course material, with the lecture book and slides inside the game.
- **Monty Python:** an AI tutor that answers Python questions.
  It uses Google Gemini with your own free API key (see below).
- Progress is saved locally on your computer.

## Run from source

Requires Python 3.12 or newer.

```powershell
git clone https://github.com/petarjef/pyhotel
cd pyhotel
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Monty Python (AI tutor)

Open **Help AI**, press **ACCOUNT**, then **GET KEY** to create a free Gemini
API key at Google AI Studio, and paste it in. The free tier has usage limits
and may not be available in every region. The key is stored only on your
computer, in `settings.json`, which is not part of this repository.

## Course material

The lecture book and the lecture notebooks are not included in this repository.
The book is by Professors Azdejković, Radojičić and Stamenković.

## Project files

| File | Purpose |
| --- | --- |
| `main.py` | Window and the three top tabs |
| `hotel.py` | Hotel scene, floors, confetti |
| `play.py` | Level selection, quizzes, tasks |
| `tasks.py` | All quiz and coding tasks |
| `lab.py` | Code Lab (Jupyter kernel) |
| `lectures.py` | Lecture book and slides |
| `ai.py` | AI tutor |
| `progress.py` | Saved progress |