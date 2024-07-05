"""Series"""


def slices(series, length):
    """Output contiguous substrings of given length"""

    series_length = len(series)
    if series_length == 0:
        raise ValueError("series cannot be empty")
    if length > series_length:
        raise ValueError("slice length cannot be greater than series length")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")

    return [
        series[start : start + length] for start in range(series_length + 1 - length)
    ]
