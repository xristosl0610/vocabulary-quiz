# Vocabulary Quiz

<div align="center" markdown="1">

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fxristosl0610%2Fvocabulary-quiz&label=visitors&countColor=%23263759&style=flat&labelStyle=none)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fxristosl0610%2Fvocabulary-quiz)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/xristosl0610/vocabulary-quiz/actions)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![Issues](https://img.shields.io/github/issues/xristosl0610/vocabulary-quiz)](https://github.com/xristosl0610/vocabulary-quiz/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/xristosl0610/vocabulary-quiz)](https://github.com/xristosl0610/vocabulary-quiz/pulls)
[![Downloads](https://img.shields.io/badge/downloads-available-brightgreen)](https://github.com/xristosl0610/vocabulary-quiz/releases)

</div>

Welcome to the Vocabulary Quiz! This project is a command-line interface (CLI) tool designed to help you practice Dutch vocabulary by translating words between Dutch and English.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Features
- Quiz yourself by translating words from Dutch to English or vice versa.
- Random selection of words for each quiz.
- Support for providing additional information about each word.
- Ability to exit the quiz at any time.

## Installation
To set up the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/vocabulary-quiz.git
    cd vocabulary-quiz
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment:**
   On Windows:
    ```bash
    .\.venv\Scripts\activate
    ```

4. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use the Vocabulary Quiz, follow these steps:

1. **Prepare your vocabulary CSV file:**
    - Ensure your CSV file (e.g., `Dutch_Vocabulary.csv`) is in the `data` directory.
    - The CSV file should have the following columns: `Dutch`, `English`, and `Additional Info`.

2. **Run the quiz:**
    ```bash
    python -m vocab_quiz.cli data/Dutch_Vocabulary.csv --num_words 20 --direction nl_en
    ```

    - `--num_words`: Number of words in the quiz (default is 10).
    - `--direction`: Direction of the quiz (`nl_en` for Dutch to English, `en_nl` for English to Dutch).

3. **Batch file for running both directions:**
    You can use the provided batch file to run quizzes in both directions sequentially.
    ```bash
    run_vocab_quiz.bat
    ```
   or using again a batch file you can add new words to the `csv` file
   ```bash
    add_words.bat
    ```

## Project Structure
Here’s an overview of the project structure:

vocab_quiz/<br>
│<br>
├── vocab_quiz/<br>
│ ├── init.py<br>
│ ├── quiz.py<br>
│ ├── cli.py<br>
│<br>
├── bat/<br>
│ ├── add_words.bat<br>
│ ├── run_vocab_quiz.bat<br>
│ └── short_quiz.bat<br>
├── data/<br>
│ └── Dutch_Vocabulary.csv<br>
│<br>
├── .venv/<br>
│ └── (virtual environment files)<br>
│<br>
├── tests/<br>
│ └── test_quiz.py<br>
│<br>
├── run_vocab_quiz.bat<br>
├── requirements.txt<br>
├── setup.py<br>
└── README.md

## Running Tests
To run the tests, use the following command:

```bash
python -m unittest discover tests
```

Make sure you have the correct working directory and the `Dutch_Vocabulary.csv` file is in the expected location.

## Contributing
We welcome contributions! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Author
Christos Lathourakis <br>
Machine Learning Engineer @TNO <br>
You can contact me at `xristosl0610@gmail.com` for any queries or further information.
