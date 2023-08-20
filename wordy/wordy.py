"""Wordy"""

# pylint: disable=invalid-name,too-many-branches


def answer(question: str) -> int:
    """Answer wordy"""

    if not question.startswith("What is"):
        raise ValueError("unknown operation")

    parts = (
        question.replace("What is", "")
        .replace("multiplied by", "mult")
        .replace("divided by", "div")
        .replace("?", "")
        .split()
    )

    left = None
    op = None
    right = None
    print(parts)

    for part in parts:
        if left is None:
            try:
                left = int(part)
            except Exception as err:
                raise ValueError("syntax error") from err
        elif op is None:
            if part == "plus":
                op = "__add__"
            elif part == "minus":
                op = "__sub__"
            elif part == "mult":
                op = "__mul__"
            elif part == "div":
                op = "__floordiv__"
            elif part.replace("-", "").isnumeric():
                raise ValueError("syntax error")
            else:
                raise ValueError("unknown operation")

        else:
            try:
                right = int(part)
                left = getattr(left, op)(right)
                op = None
                right = None

            except Exception as err:
                raise ValueError("syntax error") from err

    if left is None or op is not None:
        raise ValueError("syntax error")

    return left
