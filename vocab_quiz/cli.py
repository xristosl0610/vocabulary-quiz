from argparse import ArgumentParser, Namespace
from vocab_quiz.quiz import read_csv, write_csv, add_word, quiz
import pandas as pd


def main() -> None:
    """
    Main function that parses the command line arguments and starts the quiz or adds a new word.
    """
    parser: ArgumentParser = ArgumentParser(description="Vocabulary Quiz")
    parser.add_argument("csv_file", help="Path to the CSV file containing vocabulary")
    parser.add_argument("--num_words", type=int, default=10, help="Number of words in the quiz")
    parser.add_argument("--direction", type=str, choices=['nl_en', 'en_nl'],
                        default='nl_en', help="Direction of the quiz")

    parser.add_argument("--interactive", action="store_true", help="Interactive mode for adding new words")

    args: Namespace = parser.parse_args()

    vocab_df: pd.DataFrame = read_csv(args.csv_file)

    if args.interactive:
        print("Welcome to the Vocabulary Quiz CLI")
        print("Let's add some new words for future practice")

        while True:
            dutch_word: str = input("Dutch word: ").strip()
            english_word: str = input("English translation: ").strip()
            additional_info: str = input("Additional Info: ").strip()

            if ((vocab_df['Dutch'] == dutch_word) | (vocab_df['English'] == english_word)).any():
                print(f"The word '{dutch_word}' or its translation '{english_word}' already exists.")
            else:
                vocab_df: pd.DataFrame = add_word(vocab_df, dutch_word, english_word, additional_info)
                print(f"{dutch_word} - {english_word} - {additional_info} -- has been added successfully")

            more_words: str = input("More words to add? (y/n): ").strip().lower()
            if more_words not in ['y', 'yes']:
                break
    else:
        quiz(vocab_df, args.num_words, args.direction)

    write_csv(args.csv_file, vocab_df)

    print("Vocabulary file updated successfully!")


if __name__ == "__main__":
    main()
