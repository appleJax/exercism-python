"""Difference of squares calculations"""


def square_of_sum(number: int) -> int:
    """Square of sum"""

    if number < 0:
        raise ValueError("Number must be positive.")

    return pow(sum(range(1, number + 1)), 2)


def sum_of_squares(number: int) -> int:
    """Sum of squares"""

    if number < 0:
        raise ValueError("Number must be positive.")

    return sum(pow(x, 2) for x in range(1, number + 1))


def difference_of_squares(number: int) -> int:
    """Difference of squares"""

    if number < 0:
        raise ValueError("Number must be positive.")

    return square_of_sum(number) - sum_of_squares(number)
