import unittest
import os
from vocab_quiz.quiz import read_csv, format_direction_title, calculate_padding
import shutil

TERMINAL_WIDTH: int = shutil.get_terminal_size().columns


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

    def test_format_direction_title(self):
        self.assertEqual(format_direction_title('nl_en'), 'Dutch to English')
        self.assertEqual(format_direction_title('en_nl'), 'English to Dutch')
        with self.assertRaises(ValueError):
            format_direction_title('invalid_direction')

    def test_calculate_padding(self):
        self.assertEqual(calculate_padding('Test'), ' ' * 38)
        self.assertEqual(calculate_padding(''), '')
        self.assertEqual(calculate_padding('A'), ' ' * 39)
        self.assertEqual(calculate_padding('Test' * (TERMINAL_WIDTH // 4)), ' ')
        max_length_text = 'X' * (TERMINAL_WIDTH - 1)
        self.assertEqual(calculate_padding(max_length_text), ' ')
        long_text = 'X' * (TERMINAL_WIDTH + 10)
        self.assertEqual(calculate_padding(long_text), '')
        unicode_text = '🌟 Centered Text 🌟'
        self.assertEqual(calculate_padding(unicode_text), ' ' * 15)
        mixed_text = 'Test - 123! - Padding'
        self.assertEqual(calculate_padding(mixed_text), ' ' * 25)


if __name__ == '__main__':
    unittest.main()
