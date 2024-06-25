from argparse import ArgumentParser, Namespace
from vocab_quiz.quiz import read_csv, quiz


def main() -> None:
    """
    Main function that parses the command line arguments and starts the quiz.
    """
    parser: ArgumentParser = ArgumentParser(description="Vocabulary Quiz")
    parser.add_argument("csv_file", help="Path to the CSV file containing vocabulary")
    parser.add_argument("--num_words", type=int, default=10, help="Number of words in the quiz")
    parser.add_argument("--direction", choices=['nl_en', 'en_nl'], default='nl_en', help="Direction of the quiz")

    args: Namespace = parser.parse_args()

    vocab_list = read_csv(args.csv_file)
    quiz(vocab_list, args.num_words, args.direction)


if __name__ == "__main__":
    main()
