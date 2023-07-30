"""Resistor - trio"""

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


def label(colors: list[str]) -> str:
    """Label"""

    indices = [COLORS.index(color) for color in colors[:3]]
    power = indices[-1]

    amount = indices[0] * 10 + indices[1]
    amount *= pow(10, power)

    magnitude = ""

    if amount >= 10e8:
        magnitude = "giga"
        amount /= 10e8
    elif amount >= 10e5:
        magnitude = "mega"
        amount /= 10e5
    elif amount >= 10e2:
        magnitude = "kilo"
        amount /= 10e2

    return f"{int(amount)} {magnitude}ohms"
