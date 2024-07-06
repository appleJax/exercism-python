"""These tests are auto-generated with test data from:
https://github.com/exercism/problem-specifications/tree/main/exercises/diamond/canonical-data.json
File last updated on 2023-07-19
"""

import unittest
import pytest

from diamond import (
    rows,
)


class DiamondTest(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_degenerate_case_with_a_single_a_row(self):
        result = ["A"]
        self.assertEqual(rows("A"), result)

    @pytest.mark.task(taskno=1)
    def test_degenerate_case_with_no_row_containing_3_distinct_groups_of_spaces(self):
        result = [" A ", "B B", " A "]
        self.assertEqual(rows("B"), result)

    @pytest.mark.task(taskno=1)
    def test_smallest_non_degenerate_case_with_odd_diamond_side_length(self):
        result = ["  A  ", " B B ", "C   C", " B B ", "  A  "]
        self.assertEqual(rows("c"), result)

    @pytest.mark.task(taskno=1)
    def test_smallest_non_degenerate_case_with_even_diamond_side_length(self):
        result = [
            "   A   ",
            "  B B  ",
            " C   C ",
            "D     D",
            " C   C ",
            "  B B  ",
            "   A   ",
        ]
        self.assertEqual(rows("D"), result)

    @pytest.mark.task(taskno=1)
    def test_largest_possible_diamond(self):
        result = [
            "                         A                         ",
            "                        B B                        ",
            "                       C   C                       ",
            "                      D     D                      ",
            "                     E       E                     ",
            "                    F         F                    ",
            "                   G           G                   ",
            "                  H             H                  ",
            "                 I               I                 ",
            "                J                 J                ",
            "               K                   K               ",
            "              L                     L              ",
            "             M                       M             ",
            "            N                         N            ",
            "           O                           O           ",
            "          P                             P          ",
            "         Q                               Q         ",
            "        R                                 R        ",
            "       S                                   S       ",
            "      T                                     T      ",
            "     U                                       U     ",
            "    V                                         V    ",
            "   W                                           W   ",
            "  X                                             X  ",
            " Y                                               Y ",
            "Z                                                 Z",
            " Y                                               Y ",
            "  X                                             X  ",
            "   W                                           W   ",
            "    V                                         V    ",
            "     U                                       U     ",
            "      T                                     T      ",
            "       S                                   S       ",
            "        R                                 R        ",
            "         Q                               Q         ",
            "          P                             P          ",
            "           O                           O           ",
            "            N                         N            ",
            "             M                       M             ",
            "              L                     L              ",
            "               K                   K               ",
            "                J                 J                ",
            "                 I               I                 ",
            "                  H             H                  ",
            "                   G           G                   ",
            "                    F         F                    ",
            "                     E       E                     ",
            "                      D     D                      ",
            "                       C   C                       ",
            "                        B B                        ",
            "                         A                         ",
        ]
        self.assertEqual(rows("Z"), result)

    @pytest.mark.task(taskno=2)
    def test_invalid_input_number(self):
        with self.assertRaises(ValueError) as err:
            rows("1")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "input must be a single letter A-Z")

    @pytest.mark.task(taskno=2)
    def test_invalid_input_length(self):
        with self.assertRaises(ValueError) as err:
            rows("AB")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "input must be a single letter A-Z")
