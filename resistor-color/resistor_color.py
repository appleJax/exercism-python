"""Resistors - easy"""

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


def color_code(color: str) -> int:
    """Color code"""

    return COLORS.index(color)


def colors() -> list[str]:
    """Colors"""

    return COLORS
