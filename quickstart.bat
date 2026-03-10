@echo off
REM Quick Start Script - Sets up and runs the scraper for the first time

setlocal enabledelayedexpansion
cd /d "%~dp0"

echo.
echo ============================================================
echo   Transit App Royale Scraper - Quick Start
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Step 1: Installing dependencies...
echo.
pip install -r requirements.txt
if %errorLevel% neq 0 (
    echo.
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Step 2: Running scraper for the first time...
echo.
python scraper.py
if %errorLevel% neq 0 (
    echo.
    echo ERROR: Scraper failed
    pause
    exit /b 1
)

echo.
echo Step 3: Generating dashboard...
echo.
python dashboard.py
if %errorLevel% neq 0 (
    echo.
    echo ERROR: Dashboard generation failed
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   Setup Complete!
echo ============================================================
echo.
echo Files created:
echo   - transit_agencies.csv (Transit agency data)
echo   - transit_agencies.json (Raw data format)
echo   - index.html (Interactive dashboard)
echo.
echo Next Steps:
echo.
echo 1. View the dashboard:
echo    Open: index.html in your web browser
echo.
echo 2. Set up automatic scheduling (Optional):
echo    
echo    Option A - Using Task Scheduler (Recommended):
echo    - Run as Administrator: setup_scheduled_task.bat
echo    
echo    Option B - Using PowerShell:
echo    - Run PowerShell as Administrator
echo    - Run: .\setup_scheduled_task.ps1
echo    
echo    Option C - Manual Python Scheduler:
echo    - Run: python scheduler.py
echo    - Keep this window open to run scheduler continuously
echo.
echo 3. For future manual runs:
echo    - Scraper only: python scraper.py
echo    - Dashboard only: python dashboard.py
echo    - Both: python run.py both
echo.
echo ============================================================
echo.
pause
