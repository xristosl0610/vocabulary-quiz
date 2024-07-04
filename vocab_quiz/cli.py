from argparse import ArgumentParser, Namespace
from vocab_quiz.quiz import read_csv, write_csv, quiz
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

    args: Namespace = parser.parse_args()

    vocab_df: pd.DataFrame = read_csv(args.csv_file)
    quiz(vocab_df, args.num_words, args.direction)
    write_csv(args.csv_file, vocab_df)

    print("Vocabulary file updated successfully!")


if __name__ == "__main__":
    main()
