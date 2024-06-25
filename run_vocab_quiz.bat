@echo off
cmd /c ".\.venv\Scripts\python.exe -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 20 --direction nl_en && .\.venv\Scripts\python.exe -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 20 --direction en_nl"
