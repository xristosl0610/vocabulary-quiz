import csv
import random
import argparse
from typing import List, Dict


def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns a list of dictionaries containing the vocabulary data.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        List[Dict[str, str]]: A list of dictionaries where each dictionary represents a row in the CSV file.
    """
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader: csv.DictReader = csv.DictReader(csvfile)
        vocab_list: List[Dict[str, str]] = list(reader)
    return vocab_list


def quiz(vocab_list: List[Dict[str, str]], num_words: int = 10) -> None:
    """
    Runs a quiz by selecting a specified number of random words from the vocabulary list.

    Args:
        vocab_list (List[Dict[str, str]]): The list of vocabulary dictionaries.
        num_words (int, optional): The number of words to include in the quiz. Defaults to 10.
    """
    print("\n*** Dutch to English Quiz ***\n")
    quiz_dutch_to_english(vocab_list, num_words)

    print("\n*** English to Dutch Quiz ***\n")
    quiz_english_to_dutch(vocab_list, num_words)


def quiz_dutch_to_english(vocab_list: List[Dict[str, str]], num_words: int) -> None:
    """
    Quiz where Dutch words are presented for translation into English.

    Args:
        vocab_list (List[Dict[str, str]]): The list of vocabulary dictionaries.
        num_words (int): The number of Dutch words to include in the quiz.
    """
    selected_words: List[Dict[str, str]] = random.sample(vocab_list, num_words)

    for word in selected_words:
        dutch_word: str = word['Dutch']
        correct_english_word: str = word['English']
        additional_info: str = word['Additional Info']

        print(f"\nDutch word: {dutch_word}")
        input("Your translation: ")

        print(f"\nCorrect translation: {correct_english_word}")
        print(f"Additional info: {additional_info}\n")

        response: str = input(
            "Press Enter for the next word or 'q' to exit...")

        if response.lower() == "q":
            print("Exiting the quiz...")
            return


def quiz_english_to_dutch(vocab_list: List[Dict[str, str]], num_words: int) -> None:
    """
    Quiz where English words are presented for translation into Dutch.

    Args:
        vocab_list (List[Dict[str, str]]): The list of vocabulary dictionaries.
        num_words (int): The number of English words to include in the quiz.
    """
    selected_words: List[Dict[str, str]] = random.sample(vocab_list, num_words)

    for word in selected_words:
        english_word: str = word['English']
        correct_dutch_word: str = word['Dutch']
        additional_info: str = word['Additional Info']

        print(f"\nEnglish word: {english_word}")
        input("Your translation: ")

        print(f"\nCorrect translation: {correct_dutch_word}")
        print(f"Additional info: {additional_info}\n")

        response: str = input(
            "Press Enter for the next word or 'q' to exit...")

        if response.lower() == "q":
            print("Exiting the quiz...")
            return


def main() -> None:
    """
    Main function that parses the command line arguments and starts the quiz.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Vocabulary Quiz")
    parser.add_argument(
        "csv_file", help="Path to the CSV file containing vocabulary")
    args: argparse.Namespace = parser.parse_args()

    vocab_list: List[Dict[str, str]] = read_csv(args.csv_file)
    num_words: int = 20  # Number of words for each quiz (change as needed)
    quiz(vocab_list, num_words)


if __name__ == "__main__":
    main()
