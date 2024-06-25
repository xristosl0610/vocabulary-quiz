import unittest
from vocab_quiz.quiz import read_csv


class TestVocabQuiz(unittest.TestCase):

    def test_read_csv(self):
        vocab_list = read_csv('data/Dutch_Vocabulary.csv')
        self.assertIsInstance(vocab_list, list)
        self.assertGreater(len(vocab_list), 0)
        self.assertIn('Dutch', vocab_list[0])
        self.assertIn('English', vocab_list[0])
        self.assertIn('Additional Info', vocab_list[0])


if __name__ == '__main__':
    unittest.main()
