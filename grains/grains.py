"""Grains"""


def square(number: int) -> int:
    """Square"""

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return pow(2, number - 1)


def total():
    """Total"""

    return sum(square(x) for x in range(1, 65))
