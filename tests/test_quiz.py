import unittest
import os
from vocab_quiz.quiz import read_csv


class TestVocabQuiz(unittest.TestCase):

    def test_read_csv(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(current_dir, '../data/Dutch_Vocabulary.csv')
        vocab_list = read_csv(csv_file_path)
        self.assertIsInstance(vocab_list, list)
        self.assertGreater(len(vocab_list), 0)
        self.assertIn('Dutch', vocab_list[0])
        self.assertIn('English', vocab_list[0])
        self.assertIn('Additional Info', vocab_list[0])


if __name__ == '__main__':
    unittest.main()
