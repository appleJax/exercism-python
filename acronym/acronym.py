"""Acronym creator"""

import re as regex

SPECIAL_CHARS = regex.compile("[^a-z -]", regex.IGNORECASE)
HYPHENS = regex.compile("[ -]+")


def abbreviate(words: str) -> str:
    """Abbreviate"""

    normalized = regex.sub(SPECIAL_CHARS, "", words)
    normalized = regex.sub(HYPHENS, " ", normalized)

    return "".join(word[0].upper() for word in normalized.replace("-", " ").split(" "))
