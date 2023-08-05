"""Binary search"""


def find(search_list: list[int], value: int) -> int:
    """Find element"""

    low = 0
    high = len(search_list)

    while low <= high:
        mid = (low + high) // 2

        try:
            element = search_list[mid]
        except IndexError:
            break

        if element == value:
            return mid
        if element > value:
            high = mid - 1
        else:
            low = mid + 1

    raise ValueError("value not in array")
