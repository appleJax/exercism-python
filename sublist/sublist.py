"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from typing import Literal

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_a: list, list_b: list) -> Literal[0, 1, 2, 3]:
    """Compare two lists"""

    if len(list_a) == len(list_b):
        return EQUAL if list_a == list_b else UNEQUAL

    if len(list_a) == 0:
        return SUBLIST

    if len(list_b) == 0:
        return SUPERLIST

    matched = SUBLIST
    left = list_a
    right = list_b

    if len(list_a) > len(list_b):
        matched = SUPERLIST
        left = list_b
        right = list_a

    while left[0] in right:
        index = right.index(left[0])
        if left == right[index : index + len(left)]:
            return matched
        right = right[index + 1 :]

    return UNEQUAL
