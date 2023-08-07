""""Affine Cipher"""

import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

SYMBOLS = re.compile("[^a-z0-9]+", re.IGNORECASE)

CHUNK_SIZE = 5


def encode(plain_text: str, key_a: int, key_b: int) -> str:
    """Encode"""

    if not is_coprime(key_a, 26):
        raise ValueError("a and m must be coprime.")

    normalized = re.sub(SYMBOLS, "", plain_text).lower()
    result = ""

    for char in normalized:
        if char.isnumeric():
            result += char
        else:
            encoded_index = (key_a * ALPHABET.index(char) + key_b) % 26
            result += ALPHABET[encoded_index]

    return chunk(result)


def decode(ciphered_text: str, key_a: str, key_b: str) -> str:
    """Decode"""

    if not is_coprime(key_a, 26):
        raise ValueError("a and m must be coprime.")

    mmi = modular_multiplicative_inverse(key_a)
    result = ""

    for char in ciphered_text:
        if char.isspace():
            continue

        if char.isnumeric():
            result += char
        else:
            decoded_index = mmi * (ALPHABET.index(char) - key_b) % 26
            result += ALPHABET[decoded_index]

    return result


def is_coprime(num_a: int, num_b) -> bool:
    """Is Coprime

    Euclid's algorithm for finding Greatest Common Divisor
    """

    high = max(num_a, num_b)
    low = min(num_a, num_b)

    while low > 0:
        high, low = low, high % low

    return high == 1


def chunk(text: str) -> str:
    """Chunk text into groups of CHUNK_SIZE chars"""

    return " ".join(text[i : i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE))


def modular_multiplicative_inverse(num: int) -> int:
    """Find modular multiplicative inverse of num mod 26"""

    for i in range(1, 26):
        if num * i % 26 == 1:
            return i

    raise ValueError(f"Modular multiplicative inverse not found for {num}")
