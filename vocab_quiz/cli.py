from argparse import ArgumentParser, Namespace
from vocab_quiz.quiz import read_csv, write_csv, add_word, quiz
import pandas as pd


def main() -> None:
    """
    Main function that parses the command line arguments and starts the quiz.
    """
    parser: ArgumentParser = ArgumentParser(description="Vocabulary Quiz")
    parser.add_argument("csv_file", help="Path to the CSV file containing vocabulary")
    parser.add_argument("--num_words", type=int, default=10, help="Number of words in the quiz")
    parser.add_argument("--direction", type=str, choices=['nl_en', 'en_nl'],
                        default='nl_en', help="Direction of the quiz")

    parser.add_argument("--add_word", action="store_true", help="Add a new word to the vocabulary")
    parser.add_argument("--dutch_word", type=str, help="Dutch word to add")
    parser.add_argument("--english_word", type=str, help="English word to add")
    parser.add_argument("--additional_info", type=str, help="Additional info for the new word")

    args: Namespace = parser.parse_args()

    vocab_df: pd.DataFrame = read_csv(args.csv_file)

    if args.add_word:
        if not args.dutch_word or not args.english_word or not args.additional_info:
            print("To add a word, you must provide the Dutch word, English word, and additional info.")
            return
        vocab_df = add_word(vocab_df, args.dutch_word, args.english_word, args.additional_info)
    else:
        quiz(vocab_df, args.num_words, args.direction)

    write_csv(args.csv_file, vocab_df)

    print("Vocabulary file updated successfully!")


if __name__ == "__main__":
    main()
