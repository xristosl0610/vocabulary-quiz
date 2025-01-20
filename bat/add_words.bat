@echo off
REM Locate the virtual environment path
call get_venv_path.bat
if errorlevel 1 (
    pause
    exit /b 1
)

REM Run the Python script using the determined virtual environment
%VENV_PATH% -m vocab_quiz.cli data\Dutch_Vocabulary.csv --interactive

pause