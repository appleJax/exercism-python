"""Reverse a string"""


def reverse(text: str) -> str:
    """Reverse"""

    return "".join(char for char in reversed(list(text)))
