@echo off
call C:\Users\lathourakisc\Projects\Dutch\vocabulary_quiz\.venv\Scripts\activate.bat

python -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 20 --direction nl_en
python -m vocab_quiz.cli data\Dutch_Vocabulary.csv --num_words 20 --direction en_nl
