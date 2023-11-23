#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
 number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    This function takes a pile of coins of different values and determine
     the fewest  number of coins needed to meet a given amount total.
    """

    coins.sort()

    changeAddUp = total
    coinCount = 0
    numOfCoins = len(coins)

    if total <= 0:
        return 0

    while numOfCoins > 0:
        if (changeAddUp - coins[numOfCoins - 1]) >= 0:
            changeAddUp = changeAddUp - coins[numOfCoins - 1]
            coinCount = coinCount + 1
        else:
            numOfCoins = numOfCoins - 1

    if changeAddUp == 0:
        return coinCount
    else:
        return -1
