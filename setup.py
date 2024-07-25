from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="vocab_quiz",
    version="0.1.0",
    description='A fun way to study vocabulary, among Dutch and English',
    author='Christos Lathourakis',
    author_email='xristosl0610@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "vocab_quiz = vocab_quiz.cli:main",
        ],
    },
    python_requires='>=3.9'
)
