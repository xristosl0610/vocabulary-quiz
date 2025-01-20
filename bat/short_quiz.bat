@echo off
REM Locate the virtual environment path
call get_venv_path.bat
if errorlevel 1 (
    pause
    exit /b 1
)

REM Run the Python scripts using the determined virtual environment
%VENV_PATH% -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 10 --direction nl_en
%VENV_PATH% -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 10 --direction en_nl

pause