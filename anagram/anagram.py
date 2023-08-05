"""Anagram"""

from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Find anagrams"""

    target = word.lower()
    char_counts = Counter(target)

    return [
        candidate
        for candidate in candidates
        if (normalized := candidate.lower()) != target
        and Counter(normalized) == char_counts
    ]
