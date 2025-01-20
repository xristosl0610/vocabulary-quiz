@echo off
REM Shared script to find the virtual environment Python executable
REM Change to the project root directory
cd /d "%~dp0\.."

REM Check for ".venv"
if exist ".venv\Scripts\python.exe" (
    set VENV_PATH=".venv\Scripts\python.exe"
    exit /b 0
)

REM Check for "venv"
if exist "venv\Scripts\python.exe" (
    set VENV_PATH="venv\Scripts\python.exe"
    exit /b 0
)

REM If no virtual environment is found
echo No virtual environment found. Make sure either ".venv" or "venv" is set up.
exit /b 1
