"""
Problem: House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
"""

def rob(nums):
    # rob1 keeps track of the max money robbed UP TO the house *before* the previous one.
    # rob2 keeps track of the max money robbed UP TO the *previous* house.
    rob1, rob2 = 0, 0
    
    # Iterate through every house's money [house1, house2, house3...]
    for n in nums:
        # For the current house 'n', we have a choice:
        # 1. Rob it: We get 'n' + whatever we robbed from the house two steps back (rob1)
        # 2. Skip it: We keep whatever maximum money we had up to the previous house (rob2)
        temp = max(n + rob1, rob2)
        
        # Shift our variables forward for the next iteration
        rob1 = rob2 # The old 'previous' becomes the new 'two steps back'
        rob2 = temp # The current max becomes the new 'previous'
        
    # After checking all houses, rob2 holds our absolute maximum loot.
    return rob2

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(f"Input: nums = {nums}")
    print(f"Output: {rob(nums)}")
