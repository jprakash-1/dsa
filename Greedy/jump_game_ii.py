"""
Problem: Jump Game II
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where: 0 <= j <= nums[i] and i + j < n.
Return the minimum number of jumps to reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
"""

def jump(nums):
    # res tracks the total number of jumps made.
    res = 0
    
    # We essentially use a Breadth-First Search (BFS) approach.
    # l and r represent the "window" of indices we can currently reach with 'res' jumps.
    l = r = 0
    
    # Continue jumping until our window's right edge covers or passes the final index!
    while r < len(nums) - 1:
        farthest = 0
        
        # Look at every single index within our current reachablity window [l, r]
        for i in range(l, r + 1):
            # Calculate the absolutely furthest index we can reach from ANY point in this window.
            farthest = max(farthest, i + nums[i])
            
        # Our next window of reachable indices shifts forward!
        # The new left edge starts exactly one step past our old right edge.
        l = r + 1
        # The new right edge is the furthest point we found.
        r = farthest
        
        # We successfully expanded our reach by taking 1 jump!
        res += 1
        
    return res

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(f"Input: nums = {nums}")
    print(f"Output: {jump(nums)}")
