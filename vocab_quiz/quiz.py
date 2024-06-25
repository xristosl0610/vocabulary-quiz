import csv
import random
from typing import List, Dict
import shutil

TERMINAL_WIDTH: int = shutil.get_terminal_size().columns


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


def calculate_padding(text: str) -> str:
    """
    Calculate padding to center text based on terminal width.

    Args:
        text (str): The text to center.

    Returns:
        str: Padding spaces to center the text.
    """
    text_length: int = len(text)
    padding_length: int = max(0, (TERMINAL_WIDTH - text_length) // 2)
    return " " * padding_length


def quiz(vocab_list: List[Dict[str, str]], num_words: int = 10, direction: str = 'nl_en') -> None:
    """
    Runs a quiz by selecting a specified number of random words from the vocabulary list.

    Args:
        vocab_list (List[Dict[str, str]]): The list of vocabulary dictionaries.
        num_words (int, optional): The number of words to include in the quiz. Defaults to 10.
        direction (str, optional): The direction of the quiz, 'nl_en' or 'en_nl'. Defaults to 'nl_en'.
    """
    selected_words: List[Dict[str, str]] = random.sample(vocab_list, num_words)
    direction_title: str = format_direction_title(direction)

    centered_title: str = f"*** {direction_title} Quiz ***"
    padding: str = calculate_padding(centered_title)
    print(f"\n{padding}{centered_title}\n")

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

        temp_padding: str = calculate_padding(f"{direction_title.split(' ')[0]} word: {prompt_word}")
        print(f"\n{temp_padding}{direction_title.split(' ')[0]} word: {prompt_word}")
        input(f"{temp_padding}Your translation: ")

        temp_padding: str = calculate_padding(f"Correct translation: {correct_translation}")
        print(f"\n{temp_padding}Correct translation: {correct_translation}")
        print(f"{temp_padding}Additional info: {additional_info}\n")

        temp_padding: str = calculate_padding("Press Enter for the next word or 'q' to exit...")
        response: str = input(f"{temp_padding}Press Enter for the next word or 'q' to exit...")

        if response.lower() == "q":
            print(f"{padding}Exiting the quiz...")
            return
