"""Square root"""


def square_root(number: int) -> int:
    """Square root"""

    if number == 1:
        return 1

    for num in range(1, number // 2 + 1):
        if num * num == number:
            return num

    raise ValueError("Integer square root not found.")
