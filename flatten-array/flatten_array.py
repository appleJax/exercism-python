"""Flatten iterables"""


def flatten(iterable: list) -> list:
    """Flatten"""

    if not isinstance(iterable, list):
        return [iterable]

    result = []

    for element in iterable:
        if element is not None:
            result += flatten(element)

    return result
