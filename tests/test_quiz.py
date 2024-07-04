import unittest
from unittest.mock import patch, mock_open, call
import pandas as pd
from io import StringIO
import numpy as np

from vocab_quiz.quiz import read_csv, write_csv, format_direction_title, select_words, quiz


class TestVocabQuiz(unittest.TestCase):

    def setUp(self):
        self.csv_content = """Dutch,English,Additional Info,Showed_nl_en,Showed_en_nl
huis,house,building,2,1
boek,book,reading material,0,0
kat,cat,animal,1,1
fiets,bike,vehicle,3,0
"""
        self.vocab_df = pd.read_csv(StringIO(self.csv_content))
        self.file_path = "test_vocab.csv"

    @patch("builtins.open", new_callable=mock_open, read_data="Dutch,English,Additional Info,Showed_nl_en,Showed_en_nl\nhuis,house,building,2,1\nboek,book,reading material,0,0\nkat,cat,animal,1,1\nfiets,bike,vehicle,3,0\n")
    def test_read_csv(self, mock_file):
        expected_df = pd.read_csv(StringIO(self.csv_content))
        result_df = read_csv(self.file_path)
        pd.testing.assert_frame_equal(result_df, expected_df)
        mock_file.assert_called_once_with(self.file_path, 'r', encoding='utf-8', errors='strict', newline='')

    @patch("builtins.open", new_callable=mock_open)
    def test_write_csv(self, mock_file):
        with patch('pandas.DataFrame.to_csv') as mock_to_csv:
            write_csv(self.file_path, self.vocab_df)
            mock_to_csv.assert_called_once_with(self.file_path, index=False)

    def test_format_direction_title(self):
        self.assertEqual(format_direction_title('nl_en'), 'Dutch to English')
        self.assertEqual(format_direction_title('en_nl'), 'English to Dutch')
        with self.assertRaises(ValueError):
            format_direction_title('unknown')

    def test_select_words(self):
        np.random.seed(0)  # Set seed for reproducibility
        selected_words = select_words(self.vocab_df, 2, 'nl_en')
        self.assertEqual(len(selected_words), 2)
        self.assertTrue('Dutch' in selected_words.columns)
        self.assertTrue('English' in selected_words.columns)

    @patch('builtins.input', side_effect=['house', 'y', 'q'])
    @patch('builtins.print')
    def test_quiz(self, mock_print, *args):
        with patch('vocab_quiz.quiz.select_words', return_value=self.vocab_df.iloc[:1]):
            quiz(self.vocab_df, 1, 'nl_en')

            self.assertEqual(self.vocab_df.at[0, 'Showed_nl_en'], 3)
            self.assertEqual(self.vocab_df.at[1, 'Showed_nl_en'], 0)
            mock_print.assert_has_calls([call('\n*** Dutch to English Quiz ***\n'),
                                         call('\nDutch word: huis'),
                                         call('\nCorrect translation: house'),
                                         call('Additional info: building\n'),
                                         call('Exiting the quiz...')])


if __name__ == '__main__':
    unittest.main()
