from argparse import ArgumentParser, Namespace
from colorama import init, Fore, Style
from vocab_quiz.quiz import read_csv, quiz, calculate_padding


def main() -> None:
    """
    Main function that parses the command line arguments and starts the quiz.
    """
    init(autoreset=True)

    parser: ArgumentParser = ArgumentParser(description="Vocabulary Quiz")
    parser.add_argument("csv_file", help="Path to the CSV file containing vocabulary")
    parser.add_argument("--num_words", type=int, default=10, help="Number of words in the quiz")
    parser.add_argument("--direction", choices=['nl_en', 'en_nl'], default='nl_en', help="Direction of the quiz")

    args: Namespace = parser.parse_args()

    try:
        vocab_list = read_csv(args.csv_file)
    except FileNotFoundError:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} File '{args.csv_file}' not found. Please check the file path.")
        return
    except Exception as e:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} An error occurred while reading the CSV file: {str(e)}")
        return

    title: str = " Welcome to Vocabulary Quiz CLI "
    padding: str = calculate_padding(title)
    print(f"\n{padding}{len(title)*'='}"
          f"\n{padding} Welcome to Vocabulary Quiz CLI "
          f"\n{padding}{len(title)*'='}")

    # print(f"\n{Fore.YELLOW}======================================="
    #       f"\nWelcome to Vocabulary Quiz CLI"
    #       f"\n=======================================\n{Style.RESET_ALL}")

    try:
        quiz(vocab_list, args.num_words, args.direction)
    except ValueError as ve:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} {str(ve)}")
        return
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting...")
        return
    except Exception as e:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} An unexpected error occurred: {str(e)}")
        return


if __name__ == "__main__":
    main()
