"""Two fer"""

from typing import Optional


def two_fer(name: Optional[str]) -> str:
    """Two fer"""

    subject = name if name else "you"
    return f"One for {subject}, one for me."
