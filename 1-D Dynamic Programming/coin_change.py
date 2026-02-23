"""
Problem: Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
"""

def coinChange(coins, amount):
    # dp[i] represents the Minimum num of coins needed to make amount `i`
    # We initialize the array with (amount + 1) because the max possible coins 
    # we could ever need is `amount` (if we only had 1-cent coins). 
    # So, `amount + 1` acts as our "infinity" value.
    dp = [amount + 1] * (amount + 1)
    
    # Base case: It takes 0 coins to make an amount of 0.
    dp[0] = 0
    
    # We will calculate the minimum coins needed for EVERY amount from 1 up to our target `amount`.
    for a in range(1, amount + 1):
        # For the current amount `a`, we try every available coin denomination
        for c in coins:
            # If the coin's value is less than or equal to the amount we are trying to make...
            if a - c >= 0:
                # We update dp[a] to be the minimum of:
                # 1. The current best known way to make amount `a`
                # 2. 1 (the current coin we are using) + dp[a - c] (the best way to make the REMAINDER)
                dp[a] = min(dp[a], 1 + dp[a - c])
                
    # If dp[amount] is still `amount + 1`, it means we never found a valid combination. Returns -1.
    return dp[amount] if dp[amount] != amount + 1 else -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(f"Input: coins = {coins}, amount = {amount}")
    print(f"Output: {coinChange(coins, amount)}")
