"""
Problem: House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
"""

def rob(nums):
    # Edge case: If there's only one house, just rob it! No circle logic needed.
    if len(nums) == 1:
        return nums[0]
        
    # Since the houses are in a circle, we CANNOT rob both the first AND the last house.
    # We break this circular problem into two linear "House Robber I" problems:
    # 1. Try robbing from house 1 to the second-to-last house (skip the last).
    # 2. Try robbing from house 2 to the last house (skip the first).
    # Return the maximum of these two scenarios.
    return max(helper(nums[1:]), helper(nums[:-1]))
    
def helper(nums):
    # This is the exact same logic from "House Robber I" (Linear street)
    rob1, rob2 = 0, 0
    for n in nums:
        newRob = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2

if __name__ == "__main__":
    nums = [2, 3, 2]
    print(f"Input: nums = {nums}")
    print(f"Output: {rob(nums)}")
