@echo off
REM Insightify - GUI Application Launcher
REM This script launches the Insightify GUI application

echo.
echo ========================================
echo   INSIGHTIFY - Report Generator
echo   Professional Data Analysis System
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Check if required modules are installed
python -c "import PyQt6" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Installing required dependencies...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Launch the GUI application
echo.
echo Launching Insightify GUI Application...
echo.
python ui_application.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to launch application
    pause
    exit /b 1
)

pause
