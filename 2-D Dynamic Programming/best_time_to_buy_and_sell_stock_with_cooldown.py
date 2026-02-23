"""
Problem: Best Time to Buy and Sell Stock with Cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
"""

def maxProfit(prices):
    # dp dictionary acts as our cache (memoization).
    # Key: (index in prices array, boolean is_buying_state)
    # Value: Maximum profit achievable from that state onwards.
    dp = {}

    # Depth-First Search (DFS) with Memoization
    # 'i' is the current day. 
    # 'buying' is True if we are looking to BUY, False if we are looking to SELL.
    def dfs(i, buying):
        # Base Case: We ran out of days. We can't make any more profit.
        if i >= len(prices):
            return 0
            
        # If we already calculated the max profit for this exact day and state, 
        # just return the saved answer! This saves us from redundant calculations.
        if (i, buying) in dp:
            return dp[(i, buying)]

        # Scenario 1: We are currently in a "Buying" state
        if buying:
            # Choice A: We BUY today. We pay the price, and move to the next day in a "Selling" state.
            buy = dfs(i + 1, not buying) - prices[i]
            
            # Choice B: We DO NOTHING (Cooldown/Skip). We move to the next day still wanting to buy.
            cooldown = dfs(i + 1, buying)
            
            # Store the BEST choice in our cache.
            dp[(i, buying)] = max(buy, cooldown)
            
        # Scenario 2: We are currently in a "Selling" state
        else:
            # Choice A: We SELL today. We gain the price, but because of the MANDATORY COOLDOWN, 
            # we must jump TWO days ahead (i + 2) in a "Buying" state.
            sell = dfs(i + 2, not buying) + prices[i]
            
            # Choice B: We DO NOTHING (Hold/Skip). We move to the next day still wanting to sell.
            cooldown = dfs(i + 1, buying)
            
            # Store the BEST choice in our cache.
            dp[(i, buying)] = max(sell, cooldown)
            
        return dp[(i, buying)]

    # Start the simulation on day 0, in a "Buying" state.
    return dfs(0, True)

if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    print(f"Input: prices = {prices}")
    print(f"Output: {maxProfit(prices)}")
