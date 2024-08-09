@echo off
REM Change to the base directory
cd /d "%~dp0.."

REM Check if ".venv" exists
if exist ".venv\Scripts\python.exe" (
    set VENV_PATH=".venv\Scripts\python.exe"
) else (
    REM Check if "venv" exists
    if exist "venv\Scripts\python.exe" (
        set VENV_PATH="venv\Scripts\python.exe"
    ) else (
        echo No virtual environment found. Make sure either ".venv" or "venv" is set up.
        pause
        exit /b
    )
)

REM Run Python scripts using relative paths
%VENV_PATH% -m vocab_quiz.cli data\Dutch_Vocabulary.csv --interactive

pause