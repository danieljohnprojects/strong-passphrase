"""Randomly generate strong passphrases from the command line."""

import argparse
import secrets
import string
from math import log2
from .eng_words import eng_words
from .flavour_text import flavour_text

vowels = set("aeiou")
consonants = set(string.ascii_lowercase) - vowels
syllables = {c + v for c in consonants for v in vowels}


def random_word(words: set[str]) -> str:
    """Randomly sample a word from a set of strings.

    Args:
        words (set[str]): A sequence of words.

    Returns:
        str: A random choice
    """
    assert isinstance(words, set)  # Don't allow duplicates
    return secrets.choice(list(words))


def random_syllables(n: int) -> str:
    """Randomly sample syllables to make a made-up word.

    Args:
        l (int): The number of syllables to use

    Returns:
        str: A made-up word consisting of a bunch of randomly sampled syllables.
    """
    return "".join(secrets.choice(list(syllables)) for _ in range(n))


def gen_passphrase(
    word_set: set[str] = eng_words,
    num_words: int = 2,
    num_syllables: int = 3,
) -> tuple[str, float]:
    """Generate a strong passphrase.

    Generates a passphrase that alternates between words from the supplied word list and made up words. The words in the passphrase are separated by a randomly chosen delimiter.

    Args:
        word_set (set[str], optional): A set of words to sample from. Defaults to default_words.
        num_words (int, optional): The number of words and made-up words to sample. Determines the length of the passphrase. Must be at least 2. Defaults to 2.
        num_syllables (int, optional): The number of syllables to use in the made up words. Defaults to 3.

    Raises:
        ValueError: _description_

    Returns:
        tuple[str, float]: _description_
    """
    if num_words < 2:
        raise ValueError("Number of words must be at least 2.")
    delimiter = secrets.choice(string.punctuation)
    passphrase = [
        random_word(word_set) + delimiter + random_syllables(num_syllables)
        for _ in range(num_words)
    ]
    entropy = (
        log2(len(string.punctuation))
        + num_words * log2(len(word_set))
        + num_words * num_syllables * log2(len(syllables))
    )

    return delimiter.join(passphrase), entropy


def parse_args():
    parser = argparse.ArgumentParser(
        description="Randomly generate strong passphrases from the command line."
    )
    parser.add_argument(
        "-n",
        "--num_words",
        default=2,
        help="The number of words to use in the passphrase. More words makes for stronger passphrases.",
        type=int,
    )
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        passphrase, entropy = gen_passphrase(num_words=args.num_words)
    except ValueError:
        print(
            "Number of words must be at least 2 to get a sufficiently strong passphrase."
        )
        exit(1)
    print()
    print("=={:=<30s}".format(" Your passphrase "))
    print(passphrase)
    print("=" * 32)
    print()

    print(flavour_text(entropy))
