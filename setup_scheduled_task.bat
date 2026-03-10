@echo off
REM This script creates a Windows Task Scheduler job to run the Transit Royale Scraper
REM Must be run as Administrator

echo Setting up Transit App Royale Scheduler...
echo.

REM Check if running as Administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Error: This script must be run as Administrator
    echo Please right-click and select "Run as Administrator"
    pause
    exit /b 1
)

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0

REM Find Python executable
for /f "delims=" %%i in ('where python') do (
    set PYTHON_EXE=%%i
    goto :found_python
)

:found_python
echo Python found at: %PYTHON_EXE%

REM Create the scheduled task
echo Creating Task Scheduler job...
echo.

taskkill /F /IM scheduler.py >nul 2>&1

REM Delete existing task if it exists
schtasks /delete "Transit Royale Scraper" /f 2>nul

REM Create new task to run scheduler.py every Monday at 10:00 AM
schtasks /create /tn "Transit Royale Scraper" ^
    /tr "\"%PYTHON_EXE%\" \"%SCRIPT_DIR%scheduler.py\"" ^
    /sc weekly /d MON /st 10:00:00 ^
    /sd 01/01/2024 ^
    /f ^
    /ru SYSTEM

if %errorLevel% equ 0 (
    echo.
    echo SUCCESS! Task created successfully.
    echo.
    echo Task Details:
    echo - Name: Transit Royale Scraper
    echo - Schedule: Every Monday at 10:00 AM
    echo - Script: %SCRIPT_DIR%scheduler.py
    echo - Python: %PYTHON_EXE%
    echo.
    echo The scheduler will now run automatically every Monday at 10:00 AM PST.
    echo.
    echo You can view the task in Task Scheduler under:
    echo Library \ Microsoft \ Windows \ Tasks
    echo.
) else (
    echo.
    echo ERROR! Failed to create scheduled task.
    echo Please check that:
    echo 1. You are running as Administrator
    echo 2. Python is properly installed
    echo 3. The script path is correct
    echo.
)

pause
