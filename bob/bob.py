"""Bob's responses"""


def response(hey_bob: str) -> str:
    """Respond to someone"""

    prompt = hey_bob.strip()
    is_upper = prompt.isupper()
    is_empty = len(prompt) == 0
    is_question = prompt.endswith("?")

    if is_question and is_upper:
        return "Calm down, I know what I'm doing!"

    if is_question:
        return "Sure."

    if is_upper:
        return "Whoa, chill out!"

    if is_empty:
        return "Fine. Be that way!"

    return "Whatever."
