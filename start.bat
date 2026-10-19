@echo off
cd /d "%~dp0"

if not exist .venv\ready (
    echo Prvo pokretanje: podesavanje traje nekoliko minuta...
    if exist .venv rmdir /s /q .venv
    py -m venv .venv || goto :error
    .venv\Scripts\python -m pip install --upgrade pip || goto :error
    .venv\Scripts\python -m pip install -r requirements.txt || goto :error
    echo ok> .venv\ready
)

.venv\Scripts\python main.py
goto :eof

:error
echo.
echo Podesavanje nije uspelo. Proveri da je Python 3.12 ili noviji instaliran (python.org)
echo i da je pri instalaciji cekirano "Add python.exe to PATH".
pause