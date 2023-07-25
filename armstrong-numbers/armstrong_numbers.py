"""Determine if a number is an armstrong number"""


def is_armstrong_number(number: int) -> bool:
    """
    Determine if a number equals the sum of its own digits
    each raised to the power of the number of digits
    """

    num_as_string = str(number)
    num_digits = len(num_as_string)

    return number == sum(int(digit) ** num_digits for digit in num_as_string)
