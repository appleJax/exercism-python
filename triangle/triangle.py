"""Triangles"""


def equilateral(sides: list[int]) -> bool:
    """Equilateral"""

    return is_valid_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    """Isosceles"""

    return is_valid_triangle(sides) and len(set(sides)) < 3


def scalene(sides: list[int]) -> bool:
    """Scalene"""

    return is_valid_triangle(sides) and len(set(sides)) == 3


def is_valid_triangle(sides: list[int]) -> bool:
    """Is Triangle valid"""

    # pylint: disable=invalid-name
    [a, b, c] = sides
    return all(sides) and a + b >= c and b + c >= a and a + c >= b
