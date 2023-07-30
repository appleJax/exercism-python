"""Perfect numbers"""

from typing import Literal


def classify(number: int) -> Literal["perfect", "abundant", "deficient"]:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    ceil = number / 2

    factors = [
        num for num in range(1, min(number, round(ceil + 1))) if number % num == 0
    ]
    sum_of_factors = sum(factors)

    if len(factors) == 1 or sum_of_factors < number:
        return "deficient"

    if sum_of_factors == number:
        return "perfect"

    return "abundant"
