"""
Problem: Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4
"""
import math

def minEatingSpeed(piles, h):
    # Koko's speed is between 1 and the maximum pile size
    l, r = 1, max(piles)
    res = r
    
    # Binary search to find the minimum eating speed
    while l <= r:
        k = (l + r) // 2
        
        # Calculate total hours needed at speed k
        totalTime = 0
        for p in piles:
            totalTime += math.ceil(float(p) / k)
            
        # If koko can finish within h hours, try a slower speed (left side)
        if totalTime <= h:
            res = k
            r = k - 1
        # If it takes too long, she needs to eat faster (right side)
        else:
            l = k + 1
            
    return res

if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(f"Input: piles = {piles}, h = {h}")
    print(f"Output: {minEatingSpeed(piles, h)}")
