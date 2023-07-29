"""Matching brackets"""

BRACKETS_OPEN = ("(", "[", "{")
BRACKETS_CLOSE = (")", "]", "}")


def is_paired(input_string: str) -> bool:
    """Is paired"""

    history = []

    for char in input_string:
        if char in BRACKETS_OPEN:
            history.append(char)

        if char in BRACKETS_CLOSE:
            index = BRACKETS_CLOSE.index(char)
            if len(history) == 0 or BRACKETS_OPEN[index] != history.pop():
                return False

    return len(history) == 0
