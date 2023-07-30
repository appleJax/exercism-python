"""List ops"""

from typing import Any, Callable


# pylint: disable=redefined-builtin,


def append(list1: list[Any], list2: list[Any]) -> list[Any]:
    """Append"""
    for item in list2:
        list1.append(item)

    return list1


def concat(lists: list[list[Any]]) -> list[Any]:
    """Concat"""

    result = []

    for list_item in lists:
        result.extend(list_item)

    return result


def filter(function: Callable, list_arg: list[Any]) -> list[Any]:
    """Filter"""

    return [x for x in list_arg if function(x)]


def length(list_arg: list[Any]) -> int:
    """Length"""

    return sum(1 for x in list_arg)


def map(function: Callable, list_arg: list) -> list:
    """Map"""

    return [function(x) for x in list_arg]


def foldl(function: Callable, list_arg: list, initial: Any) -> Any:
    """FoldL"""

    result = initial

    for item in list_arg:
        result = function(result, item)

    return result


def foldr(function: Callable, list_arg: list, initial: Any) -> Any:
    """FoldR"""

    return foldl(function, reverse(list_arg), initial)


def reverse(list_arg: list) -> list:
    """Reverse"""

    result = []

    for item in list_arg:
        result.insert(0, item)

    return result
