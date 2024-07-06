"""Diamond Challenge"""

from typing import List
import math

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rows(letter: str) -> List[str]:
    """Return an array with letters starting from A to letter in the shape of a diamond"""

    end_letter = letter.upper()
    if len(end_letter) != 1 or not end_letter in ALPHABET:
        raise ValueError("input must be a single letter A-Z")

    iterations = ALPHABET.index(end_letter) * 2
    diamond = []
    middle_index = math.floor(iterations / 2)

    for index in range(iterations + 1):
        adjusted_index = index if index <= middle_index else iterations - index
        current_letter = ALPHABET[adjusted_index]
        line = list(" " * (iterations + 1))
        line[middle_index - adjusted_index] = current_letter
        line[middle_index + adjusted_index] = current_letter
        diamond.append("".join(line))

    return diamond
