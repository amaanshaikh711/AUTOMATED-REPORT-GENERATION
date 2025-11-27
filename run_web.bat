@echo off
REM Insightify Web Server Launcher
REM This script starts the Insightify web interface

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║          INSIGHTIFY - PROFESSIONAL REPORT GENERATOR        ║
echo ║                                                            ║
echo ║  Starting web server...                                   ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

REM Install requirements if needed
echo [*] Checking dependencies...
pip install -q -r requirements.txt

REM Start the web server
echo [*] Starting Insightify web server on http://localhost:8000
echo [*] Opening browser...
timeout /t 2 /nobreak

REM Open browser
start http://localhost:8000

REM Run the server
python web_server.py 8000

pause
