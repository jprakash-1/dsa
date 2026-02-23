"""
Problem: Cheapest Flights Within K Stops
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [from_i, to_i, price_i] indicates that there is a flight from city from_i to city to_i with cost price_i.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
"""

def findCheapestPrice(n, flights, src, dst, k):
    # Bellman-Ford Algorithm Approach
    # 'prices' keeps track of the cheapest price to reach each city from 'src'.
    # Initially, all cities cost "infinity" to reach, except the start city ('src') which costs 0.
    prices = [float("inf")] * n
    prices[src] = 0

    # We are allowed AT MOST 'k' stops. This means a flight path can have at most 'k + 1' EDGES.
    # Therefore, we run our price-updating loop exactly 'k + 1' times.
    for i in range(k + 1):
        # We need a temporary copy of prices for the CURRENT number of stops.
        # This prevents a single flight jumping through multiple cities in the *same* iteration.
        tmpPrices = prices.copy()
        
        # Look at every single flight available
        for s, d, p in flights:
            # If we haven't even found a way to reach the source city 's' yet, we can't take this flight!
            if prices[s] == float("inf"):
                continue
                
            # If taking this flight from 's' to 'd' is CHEAPER than any previously known route to 'd'...
            if prices[s] + p < tmpPrices[d]:
                # Update the cost to reach 'd' in our temporary array!
                tmpPrices[d] = prices[s] + p
                
        # After evaluating all flights for this 'stop' iteration, update our main prices array
        prices = tmpPrices
        
    # After 'k+1' iterations, the 'dst' index holds the cheapest price to reach the destination
    # within the allowed stops. If it's still infinity, the destination is unreachable!
    return prices[dst] if prices[dst] != float("inf") else -1

if __name__ == "__main__":
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    print(f"Input: n = {n}, flights = {flights}, src = {src}, dst = {dst}, k = {k}")
    print(f"Output: {findCheapestPrice(n, flights, src, dst, k)}")
