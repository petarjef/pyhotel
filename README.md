# Python Hotel

An educational game for learning Python. Climb the floors of a pixel-art hotel,
one floor per lesson, by solving quizzes and writing real code.

## How the code editor works

Your variables stay between runs. If you write `x = 5` and run it, then write
`print(x)` and run again, it prints 5. This is the same in the Code Lab and in
the coding levels, and it carries over from one level to the next. Press **RESET**
to clear everything and start with a clean Python. In the browser version,
**STOP** also clears your variables.

## Play

| Platform | How |
| --- | --- |
| Browser (any device) | [petarjef.github.io/pyhotel](https://petarjef.github.io/pyhotel/) |
| Windows | Download `PythonHotel_Setup.exe` from the [latest release](https://github.com/petarjef/pyhotel/releases) |

The Windows installer downloads Python and everything else it needs, so the
first installation takes a few minutes and needs an internet connection.
Windows may show a "protected your PC" warning because the installer is not
signed. Click **More info**, then **Run anyway**.

## Features

- **Hotel:** every floor is a lesson, with 12 levels each (quizzes and coding tasks).
- **Code Lab:** a built-in Python editor backed by a Jupyter kernel.
- **Lectures:** the course book, opened from its website ([dazdejkovic.github.io/OI_25_jb1](https://dazdejkovic.github.io/OI_25_jb1/OI_25_00_uvod.html)). It needs an internet connection.
- **Monty Python:** an AI tutor that answers Python questions.
  It uses Google Gemini with your own free API key (see below).
- Progress is saved locally on your computer.

## Browser version

Nothing to install, it runs in your browser. The first time you run code, the page loads Python, which takes a few seconds. The first time you use NumPy, Pandas, SciPy or scikit-learn, those libraries are loaded as well, which can take longer on a slow connection. After that it is quick. If your code uses `input()`, type the answers in the box under the editor, one per line. Your progress is saved in your browser, and the Gemini key for the AI tutor stays in your browser too.

## Monty Python (AI tutor)

Open **Help AI**, press **ACCOUNT**, then **GET KEY** to create a free Gemini
API key at Google AI Studio, and paste it in. The free tier has usage limits
and may not be available in every region. The key is stored only on your
computer, in `settings.json`, which is not part of this repository.

## Course material

The course book is not included in this repository or in the Windows installer.
It is read online at
[dazdejkovic.github.io/OI_25_jb1](https://dazdejkovic.github.io/OI_25_jb1/OI_25_00_uvod.html).
In the game, the Lectures tab opens its chapters from there, so it needs an
internet connection. The book is by Professors Azdejković, Radojičić and
Stamenković.