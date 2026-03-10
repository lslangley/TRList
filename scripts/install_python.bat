@echo off
REM Python Installation Script for Transit Royal Scraper
REM This script installs Python with all necessary configurations

echo.
echo ============================================================
echo   Python Installation for Transit Royal Scraper
echo ============================================================
echo.

REM Download Python installer
set PYTHON_INSTALLER=python-3.11.9-amd64.exe
set PYTHON_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe

echo Downloading Python 3.11.9...
echo.

REM Try to download with curl
if exist %PYTHON_INSTALLER% (
    echo Python installer already downloaded.
) else (
    curl -o %PYTHON_INSTALLER% %PYTHON_URL%
    if errorlevel 1 (
        echo.
        echo ERROR: Could not download Python
        echo.
        echo Please download manually from:
        echo   https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
        echo.
        pause
        exit /b 1
    )
)

echo.
echo ============================================================
echo   Installing Python 3.11.9
echo ============================================================
echo.
echo Installation options:
echo   - Add Python to PATH (automatically checked)
echo   - Install for all users
echo   - Include pip
echo.

REM Run installer with silent options
%PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1 Include_tcltk=1

if errorlevel 1 (
    echo.
    echo WARNING: Installation may have encountered issues
    echo Please verify Python was installed correctly
    echo.
) else (
    echo.
    echo Python installation completed!
    echo.
)

echo Verifying Python installation...
python --version

if errorlevel 1 (
    echo.
    echo ERROR: Python not found after installation
    echo Please restart your computer and try again
    echo.
) else (
    echo.
    echo SUCCESS! Python is now installed
    echo.
    echo Next steps:
    echo   1. Close and reopen Command Prompt or PowerShell
    echo   2. Navigate to the Transit_Royal project directory
    echo   3. Run: python -m pip install -r requirements.txt
    echo   4. Run: quickstart.bat
    echo.
)

pause
