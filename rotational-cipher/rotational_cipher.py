"""Rotational cypher """

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def rotate(text: str, key: int) -> str:
    """Rotate"""

    key %= 26
    rotated = ALPHABET[key:] + ALPHABET[:key]

    result = ""

    for char in text:
        if not char.isalpha():
            result += char
        else:
            new_char = rotated[ALPHABET.index(char.lower())]
            result += new_char if char.islower() else new_char.upper()

    return result
