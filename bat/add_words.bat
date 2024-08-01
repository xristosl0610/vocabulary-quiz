@echo off
REM Get the directory of the batch file
setlocal
set "BASE_DIR=%~dp0"

REM Change to the base directory
cd /d "%BASE_DIR%" && cd /d ..

REM Run Python scripts using relative paths
cmd /c ".\venv\Scripts\python.exe -m vocab_quiz.cli data\Dutch_Vocabulary.csv --interactive"
pause