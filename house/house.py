"""The House that Jack Built"""

VERB_NOUNS = [
    None,
    ("lay in", "house that Jack built"),
    ("ate", "malt"),
    ("killed", "rat"),
    ("worried", "cat"),
    ("tossed", "dog"),
    ("milked", "cow with the crumpled horn"),
    ("kissed", "maiden all forlorn"),
    ("married", "man all tattered and torn"),
    ("woke", "priest all shaven and shorn"),
    ("kept", "rooster that crowed in the morn"),
    ("belonged to", "farmer sowing his corn"),
    ("", "horse and the hound and the horn"),
]


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite"""

    return [recite_verse(verse, "") for verse in range(start_verse, end_verse + 1)]


def recite_verse(verse: int, partial_verse: str) -> str:
    """Recite line"""

    if VERB_NOUNS[verse] is None:
        return partial_verse + "."

    if len(partial_verse) == 0:
        partial_verse = f"This is the {VERB_NOUNS[verse][1]}"
    else:
        partial_verse += f" that {VERB_NOUNS[verse][0]} the {VERB_NOUNS[verse][1]}"

    return recite_verse(verse - 1, partial_verse)
