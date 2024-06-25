from setuptools import setup, find_packages

setup(
    name="vocab_quiz",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here.
    ],
    entry_points={
        "console_scripts": [
            "vocab_quiz = vocab_quiz.cli:main",
        ],
    },
)
