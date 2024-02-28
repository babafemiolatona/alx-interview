#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Return the fewest number of coins
    needed to make up a given amount
    """
    dp = [0] + [float('inf')] * total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
