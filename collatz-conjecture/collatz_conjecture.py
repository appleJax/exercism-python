"""Collatz conjecture"""


def steps(number: int) -> int:
    """Calculate the number of steps to terminate the collatz series"""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    num_steps = 0

    while number != 1:
        num_steps += 1
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1

    return num_steps
