import numpy as np
import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a DataFrame containing the vocabulary data.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the vocabulary data.
    """
    return pd.read_csv(file_path)


def write_csv(file_path: str, vocab_df: pd.DataFrame) -> None:
    """
    Writes the updated vocabulary data back to the CSV file.

    Args:
        file_path (str): The path to the CSV file.
        vocab_df (pd.DataFrame): The DataFrame containing the updated vocabulary data.
    """
    vocab_df.to_csv(file_path, index=False)


def format_direction_title(direction: str) -> str:
    """
    Formats the direction code into a human-readable title.

    Args:
        direction (str): The direction code (e.g., 'nl_en' or 'en_nl').

    Returns:
        str: The formatted direction title.
    """
    match direction:
        case 'nl_en':
            return 'Dutch to English'
        case 'en_nl':
            return 'English to Dutch'
        case _:
            raise ValueError(f"Unknown quiz direction: {direction}")


def select_words(vocab_df: pd.DataFrame, num_words: int, direction: str) -> pd.DataFrame:
    """
    Selects words for the quiz based on inverse weighted probabilities, prioritizing words with
    fewer appearances and fewer correct guesses.

    Args:
        vocab_df (pd.DataFrame): The DataFrame containing the vocabulary data.
        num_words (int): The number of words to include in the quiz.
        direction (str): The direction code (e.g., 'nl_en' or 'en_nl').

    Returns:
        pd.DataFrame: The selected words for the quiz.
    """
    probabilities: pd.DataFrame = 1 / (vocab_df[f'Showed_{direction}'] + 1)
    probabilities /= probabilities.sum()  # Normalize to sum to 1
    selected_indices: np.ndarray = np.random.choice(
        vocab_df.index, size=num_words, replace=False, p=probabilities)

    return vocab_df.loc[selected_indices]


def add_word(vocab_df: pd.DataFrame, dutch_word: str, english_word: str, additional_info: str) -> pd.DataFrame:
    """
    Adds a new word to the vocabulary DataFrame.

    Args:
        vocab_df (pd.DataFrame): The DataFrame containing the vocabulary data.
        dutch_word (str): The Dutch word to add.
        english_word (str): The English translation to add.
        additional_info (str): Additional information about the word.

    Returns:
        pd.DataFrame: The updated DataFrame containing the new word.
    """
    if ((vocab_df['Dutch'] == dutch_word) | (vocab_df['English'] == english_word)).any():
        print("Word already exists in the vocabulary.")
        return vocab_df

    new_row: pd.DataFrame = pd.DataFrame([{
        'Dutch': dutch_word,
        'English': english_word,
        'Additional Info': additional_info,
        'Showed_nl_en': 0,
        'Showed_en_nl': 0
    }])

    updated_vocab_df: pd.DataFrame = pd.concat(
        [vocab_df, new_row], ignore_index=True)
    return updated_vocab_df


def quiz(vocab_df: pd.DataFrame, num_words: int = 50, direction: str = 'nl_en') -> None:
    """
    Runs a quiz by selecting a specified number of random words from the vocabulary list.

    Args:
        vocab_df (pd.DataFrame): The DataFrame containing the vocabulary data.
        num_words (int, optional): The number of words to include in the quiz. Defaults to 50.
        direction (str, optional): The direction of the quiz, 'nl_en' or 'en_nl'. Defaults to 'nl_en'.
    """
    selected_words: pd.DataFrame = select_words(vocab_df, num_words, direction)

    direction_title: str = format_direction_title(direction)
    print(f"\n*** {direction_title} Quiz ***\n")

    match direction:
        case 'nl_en':
            prompt_col: str = 'Dutch'
            translation_col: str = 'English'
        case 'en_nl':
            prompt_col: str = 'English'
            translation_col: str = 'Dutch'
        case _:
            raise ValueError(f"Unknown quiz direction: {direction}")

    for word_idx, (index, word) in enumerate(selected_words.iterrows(), start=1):
        print(
            f"\n{word_idx}. {direction_title.split(' ', maxsplit=1)[0]} word: {word[prompt_col]}")
        input("Your translation: ")

        print(f"\nCorrect translation: {word[translation_col]}")
        print(f"Additional info: {word['Additional Info']}\n")

        while True:
            correct = input("Was your answer correct? (y/n): ").strip().lower()
            if correct in ('yes', 'y'):
                vocab_df.at[index, f'Showed_{direction}'] += 1
                break
            if correct in ('no', 'n'):
                vocab_df.at[index, f'Showed_{direction}'] = max(
                    0, vocab_df.at[index, f'Showed_{direction}'] - 1)
                break

            print("Invalid response. Please type 'y' for yes or 'n' for no.")

        response: str = input(
            "\nPress Enter for the next word or 'q' to exit...")

        if response.lower() == "q":
            print("Exiting the quiz...")
            return
