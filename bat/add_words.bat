@echo off
REM Change to the base directory
cd /d "%~dp0.."

REM Run Python scripts using relative paths
cmd /c ".\venv\Scripts\python.exe -m vocab_quiz.cli data\Dutch_Vocabulary.csv --interactive"
pause