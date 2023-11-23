#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Update the dp array based on the available coins
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinite, the total cannot be met by any combination of coins
    return dp[total] if dp[total] != float('inf') else -1

# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
