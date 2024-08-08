@echo off
REM Change to the project root directory
cd /d "%~dp0\.."

REM Run Python scripts using relative paths
".venv\Scripts\python.exe" -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 10 --direction nl_en
".venv\Scripts\python.exe" -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 10 --direction en_nl

pause
