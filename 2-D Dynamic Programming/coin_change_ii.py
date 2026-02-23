"""
Problem: Coin Change II
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
"""

def change(amount, coins):
    # dp[i] represents the NUMBER OF WAYS to make the amount 'i'
    # We create an array of size (amount + 1) to cover 0 through 'amount'
    dp = [0] * (amount + 1)
    
    # Base case: There is exactly 1 way to make the amount 0 (use no coins).
    dp[0] = 1

    # We iterate through EACH coin denomination one by one.
    # Why this order? It prevents counting permutations (like 1+2 and 2+1) as separate ways.
    # It ensures we count *combinations*.
    for c in coins:
        # We only need to start updating amounts that are at least as large as the coin itself.
        for a in range(1, amount + 1):
            # If the current amount 'a' minus the coin 'c' isn't negative,
            # it means we COULD potentially use this coin!
            if a - c >= 0:
                # We add the number of ways to make the *remainder* (a - c).
                # This essentially says: "If I use coin 'c', how many ways could I have
                # arrived at the remaining sum needed?"
                dp[a] += dp[a - c]
                
    # Finally, dp[amount] holds the total combinations found for our target amount.
    return dp[amount]

if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    print(f"Input: amount = {amount}, coins = {coins}")
    print(f"Output: {change(amount, coins)}")
