@echo off
REM Change to the base directory
cd /d "%~dp0.."

REM Run Python scripts using relative paths
cmd /c ".\venv\Scripts\python.exe -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 50 --direction nl_en && .\venv\Scripts\python.exe -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 50 --direction en_nl"
pause