"""These tests are auto-generated with test data from:
https://github.com/exercism/problem-specifications/tree/main/exercises/atbash-cipher/canonical-data.json
File last updated on 2023-07-20
"""

import unittest
import pytest

from atbash_cipher import (
    decode,
    encode,
)


class AtbashCipherTest(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_encode_yes(self):
        self.assertEqual(encode("yes"), "bvh")

    @pytest.mark.task(taskno=1)
    def test_encode_no(self):
        self.assertEqual(encode("no"), "ml")

    @pytest.mark.task(taskno=1)
    def test_encode_omg(self):
        self.assertEqual(encode("OMG"), "lnt")

    @pytest.mark.task(taskno=1)
    def test_encode_spaces(self):
        self.assertEqual(encode("O M G"), "lnt")

    @pytest.mark.task(taskno=1)
    def test_encode_mindblowingly(self):
        self.assertEqual(encode("mindblowingly"), "nrmwy oldrm tob")

    @pytest.mark.task(taskno=1)
    def test_encode_numbers(self):
        self.assertEqual(encode("Testing,1 2 3, testing."), "gvhgr mt123 gvhgr mt")

    @pytest.mark.task(taskno=1)
    def test_encode_deep_thought(self):
        self.assertEqual(encode("Truth is fiction."), "gifgs rhurx grlm")

    @pytest.mark.task(taskno=1)
    def test_encode_all_the_letters(self):
        self.assertEqual(
            encode("The quick brown fox jumps over the lazy dog."),
            "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt",
        )

    @pytest.mark.task(taskno=2)
    def test_decode_exercism(self):
        self.assertEqual(decode("vcvix rhn"), "exercism")

    @pytest.mark.task(taskno=2)
    def test_decode_a_sentence(self):
        self.assertEqual(
            decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v"),
            "anobstacleisoftenasteppingstone",
        )

    @pytest.mark.task(taskno=2)
    def test_decode_numbers(self):
        self.assertEqual(decode("gvhgr mt123 gvhgr mt"), "testing123testing")

    @pytest.mark.task(taskno=2)
    def test_decode_all_the_letters(self):
        self.assertEqual(
            decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"),
            "thequickbrownfoxjumpsoverthelazydog",
        )

    @pytest.mark.task(taskno=2)
    def test_decode_with_too_many_spaces(self):
        self.assertEqual(decode("vc vix    r hn"), "exercism")

    @pytest.mark.task(taskno=2)
    def test_decode_with_no_spaces(self):
        self.assertEqual(
            decode("zmlyhgzxovrhlugvmzhgvkkrmthglmv"), "anobstacleisoftenasteppingstone"
        )
