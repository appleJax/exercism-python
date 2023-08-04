"""Hamming distance"""


def distance(strand_a: str, strand_b: str) -> int:
    """Hamming distance"""

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum(1 for a_char, b_char in zip(strand_a, strand_b) if a_char != b_char)
