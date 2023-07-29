"""Darts"""

from typing import Literal


def score(x_coord: int, y_coord: int) -> Literal[0, 1, 5, 10]:
    """Calculate the darts score"""

    distance = pow(pow(abs(x_coord), 2) + pow(abs(y_coord), 2), 0.5)

    if distance > 10:
        return 0

    if distance > 5:
        return 1

    if distance > 1:
        return 5

    return 10
