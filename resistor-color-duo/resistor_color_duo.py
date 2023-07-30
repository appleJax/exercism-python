"""Resister - medium"""


COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors: list[str]) -> int:
    """Resistor value"""

    indices = map(COLORS.index, colors[:2])
    digits = "".join(map(str, indices))
    return int(digits)
