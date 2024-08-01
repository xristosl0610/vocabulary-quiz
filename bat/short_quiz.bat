@echo off
REM Get the directory of the batch file
setlocal
set "BASE_DIR=%~dp0"

REM Change to the base directory
cd /d "%~dp0.."

REM Run Python scripts using relative paths
cmd /c ".\venv\Scripts\python.exe -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 10 --direction nl_en && .\venv\Scripts\python.exe -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 10 --direction en_nl"
pause