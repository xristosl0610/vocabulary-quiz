import unittest
from unittest.mock import patch, mock_open, call
import pandas as pd
from io import StringIO
import numpy as np

from vocab_quiz.quiz import (
    read_csv,
    write_csv,
    format_direction_title,
    select_words,
    add_word,
    quiz,
)


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

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="Dutch,English,Additional Info,Showed_nl_en,Showed_en_nl\nhuis,house,building,2,1\nboek,book,reading material,0,0\nkat,cat,animal,1,1\nfiets,bike,vehicle,3,0\n",
    )
    def test_read_csv(self, mock_file):
        expected_df = pd.read_csv(StringIO(self.csv_content))
        result_df = read_csv(self.file_path)
        pd.testing.assert_frame_equal(result_df, expected_df)
        mock_file.assert_called_once_with(
            self.file_path, "r", encoding="utf-8", errors="strict", newline=""
        )

    @patch("builtins.open", new_callable=mock_open)
    def test_write_csv(self, mock_file):
        with patch("pandas.DataFrame.to_csv") as mock_to_csv:
            write_csv(self.file_path, self.vocab_df)
            mock_to_csv.assert_called_once_with(self.file_path, index=False)

    def test_format_direction_title(self):
        self.assertEqual(format_direction_title("nl_en"), "Dutch to English")
        self.assertEqual(format_direction_title("en_nl"), "English to Dutch")
        with self.assertRaises(ValueError):
            format_direction_title("unknown")

    def test_select_words(self):
        np.random.seed(0)  # Set seed for reproducibility
        selected_words = select_words(self.vocab_df, 2, "nl_en")
        self.assertEqual(len(selected_words), 2)
        self.assertTrue("Dutch" in selected_words.columns)
        self.assertTrue("English" in selected_words.columns)

    def test_importance_sampling(self):
        extreme_csv_content = """Dutch,English,Additional Info,Showed_nl_en,Showed_en_nl
woord1,word1,info1,100,0
woord2,word2,info2,0,100
woord3,word3,info3,0,0
"""
        vocab_df_extreme = pd.read_csv(StringIO(extreme_csv_content))

        np.random.seed(0)
        selected_words = select_words(vocab_df_extreme, 1, "nl_en")

        selected_dutch_word = selected_words.iloc[0]["Dutch"]
        self.assertIn(selected_dutch_word, ["woord2", "woord3"])

    def test_close_probabilities_sampling(self):
        close_csv_content = """Dutch,English,Additional Info,Showed_nl_en,Showed_en_nl
woord1,word1,info1,1,0
woord2,word2,info2,3,0
woord3,word3,info3,0,0
"""
        vocab_df_close = pd.read_csv(StringIO(close_csv_content))

        np.random.seed(0)
        selection_counts = {"woord1": 0, "woord2": 0, "woord3": 0}
        num_trials = 1000

        for _ in range(num_trials):
            selected_words = select_words(vocab_df_close, 1, "nl_en")
            selected_dutch_word = selected_words.iloc[0]["Dutch"]
            selection_counts[selected_dutch_word] += 1

        self.assertGreater(selection_counts["woord1"], selection_counts["woord2"])
        self.assertGreater(selection_counts["woord3"], selection_counts["woord2"])

        print("CSV info")
        print(
            {row["Dutch"]: row["Showed_nl_en"] for _, row in vocab_df_close.iterrows()}
        )
        print("Sampling count")
        print(selection_counts)

    @patch("builtins.input", side_effect=["house", "y", "q"])
    @patch("builtins.print")
    def test_quiz(self, mock_print, *args):
        with patch("vocab_quiz.quiz.select_words", return_value=self.vocab_df.iloc[:1]):
            quiz(self.vocab_df, 1, "nl_en")

            self.assertEqual(self.vocab_df.at[0, "Showed_nl_en"], 3)
            self.assertEqual(self.vocab_df.at[1, "Showed_nl_en"], 0)
            mock_print.assert_has_calls(
                [
                    call("\n*** Dutch to English Quiz ***\n"),
                    call("\n1. Dutch word: huis"),
                    call("\nCorrect translation: house"),
                    call("Additional info: building\n"),
                    call("Exiting the quiz..."),
                ]
            )

    def test_add_word(self):
        vocab_df = self.vocab_df.copy()
        new_dutch_word = "appel"
        new_english_word = "apple"
        new_additional_info = "fruit"

        updated_vocab_df = add_word(
            vocab_df, new_dutch_word, new_english_word, new_additional_info
        )

        self.assertTrue((updated_vocab_df["Dutch"] == new_dutch_word).any())
        self.assertTrue((updated_vocab_df["English"] == new_english_word).any())
        self.assertTrue(
            (updated_vocab_df["Additional Info"] == new_additional_info).any()
        )
        self.assertTrue((updated_vocab_df["Showed_nl_en"] == 0).any())
        self.assertTrue((updated_vocab_df["Showed_en_nl"] == 0).any())

        pd.testing.assert_frame_equal(
            vocab_df.iloc[:, :-1], updated_vocab_df.iloc[:-1, :-1]
        )

        updated_vocab_df = add_word(vocab_df, "huis", "house", "building")
        self.assertEqual(len(updated_vocab_df), len(vocab_df))


if __name__ == "__main__":
    unittest.main()
