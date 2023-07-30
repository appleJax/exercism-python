"""Change"""


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Find fewest coins"""

    if target < 0:
        raise ValueError("target can't be negative")

    if target == 0:
        return []

    if len(coins) == 0:
        raise ValueError("can't make target with given coins")

    branches = [([], coins, target)]

    while branches:
        (change, coin_list, target_left) = branches.pop(0)
        biggest_coin = coin_list[-1]

        if len(coin_list) > 1:
            branches.append((change, coin_list[:-1], target_left))

        if biggest_coin <= target_left:
            new_change = change[:]
            new_change.insert(0, biggest_coin)
            if target_left == biggest_coin:
                return new_change

            branches.append((new_change, coin_list, target_left - biggest_coin))

    raise ValueError("can't make target with given coins")
