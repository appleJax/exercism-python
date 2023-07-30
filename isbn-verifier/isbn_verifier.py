"""ISBN Verifier"""


def is_valid(isbn: str) -> bool:
    """Is valid ISBN-10 number"""

    normalized = isbn.replace("-", "")[:-1]
    if len(normalized) != 9 or not normalized.isdigit():
        return False

    check_char = isbn[-1]
    check_val = 10

    if check_char.isdecimal():
        check_val = int(check_char)
    elif check_char.lower() != "x":
        return False

    digit_list = map(int, reversed(list(normalized)))

    sum_digits = sum(
        multiplier * digit for (multiplier, digit) in enumerate(digit_list, 2)
    )

    return (sum_digits + check_val) % 11 == 0
