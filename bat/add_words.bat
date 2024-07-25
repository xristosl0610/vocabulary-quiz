@echo off
REM Change directory to the directory of the batch file
cd /d "C:\Users\lathourakisc\Projects\Dutch\vocabulary_quiz"

REM Run Python scripts using relative paths
cmd /c ".\venv\Scripts\python.exe -m vocab_quiz.cli data\Dutch_Vocabulary.csv --interactive"
pause