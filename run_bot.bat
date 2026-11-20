@echo off
setlocal
cd /d "%~dp0"

if not defined BOT_TOKEN (
    set /p BOT_TOKEN="BOT_TOKEN ni kiriting: "
)

if not defined BOT_TOKEN (
    echo BOT_TOKEN topilmadi.
    pause
    exit /b 1
)

".\venv\Scripts\python.exe" ".\main.py"
