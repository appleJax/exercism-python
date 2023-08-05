"""Atbash Cipher"""

import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"

SYMBOLS = re.compile("[^a-z0-9]+", re.IGNORECASE)


def encode(plain_text: str) -> str:
    """Encode"""

    normalized = re.sub(SYMBOLS, "", plain_text).lower()
    result = ""

    for index, char in enumerate(normalized, 1):
        result += char if char.isnumeric() else CIPHER[ALPHABET.index(char)]

        if index % 5 == 0 and index < len(normalized):
            result += " "

    return result


def decode(ciphered_text: str) -> str:
    """Decode"""

    normalized = re.sub(SYMBOLS, "", ciphered_text).lower()

    return "".join(
        char if char.isnumeric() else ALPHABET[CIPHER.index(char)]
        for char in normalized
    )
