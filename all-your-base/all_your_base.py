"""Convert number bases"""

import math


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Rebase"""

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(map(lambda x: x < 0 or x >= input_base, digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    base_10 = sum(
        x * pow(input_base, power) for (power, x) in enumerate(reversed(digits))
    )

    if base_10 == 0:
        return [0]

    output_power = math.floor(math.log(base_10, output_base))

    output = []
    target = base_10

    for power in range(output_power, -1, -1):
        val = pow(output_base, power)
        multiplier = target // val
        output.append(multiplier)
        target -= multiplier * val

    return output
