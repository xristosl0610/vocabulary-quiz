import csv
import random
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


def format_direction_title(direction: str) -> str:
    """
    Formats the direction code into a human-readable title.

    Args:
        direction (str): The direction code (e.g., 'nl_en' or 'en_nl').

    Returns:
        str: The formatted direction title.
    """
    if direction == 'nl_en':
        return 'Dutch to English'
    elif direction == 'en_nl':
        return 'English to Dutch'
    else:
        raise ValueError(f"Unknown quiz direction: {direction}")


def quiz(vocab_list: List[Dict[str, str]], num_words: int = 10, direction: str = 'nl_en') -> None:
    """
    Runs a quiz by selecting a specified number of random words from the vocabulary list.

    Args:
        vocab_list (List[Dict[str, str]]): The list of vocabulary dictionaries.
        num_words (int, optional): The number of words to include in the quiz. Defaults to 10.
        direction (str, optional): The direction of the quiz, 'nl_en' or 'en_nl'. Defaults to 'nl_en'.
    """
    selected_words: List[Dict[str, str]] = random.sample(vocab_list, num_words)

    for word in selected_words:
        if direction == 'nl_en':
            prompt_word: str = word['Dutch']
            correct_translation: str = word['English']
        elif direction == 'en_nl':
            prompt_word: str = word['English']
            correct_translation: str = word['Dutch']
        else:
            raise ValueError(f"Unknown quiz direction: {direction}")

        additional_info: str = word['Additional Info']
        direction_title: str = format_direction_title(direction)

        print(f"\n{direction_title} word: {prompt_word}")
        input("Your translation: ")

        print(f"\nCorrect translation: {correct_translation}")
        print(f"Additional info: {additional_info}\n")

        response: str = input("Press Enter for the next word or 'q' to exit...")

        if response.lower() == "q":
            print("Exiting the quiz...")
            return
