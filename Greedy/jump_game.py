"""
Problem: Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
"""

def canJump(nums):
    # Start by setting the goal to the very last index of the array
    goal = len(nums) - 1
    
    # We are going to work backwards! We start from the second-to-last index and move left.
    for i in range(len(nums) - 1, -1, -1):
        # Can we leap from our current position (i) and reach or pass the 'goal'?
        # nums[i] is the max jump length from index i.
        if i + nums[i] >= goal:
            # Yes, we can! So if we can just reach 'i', we know we can reach the end.
            # We Shift our goalpost backward to 'i'.
            goal = i
            
    # After iterating all the way back to the start (index 0),
    # If our goalpost successfully shifted all the way to index 0, it means the end is reachable!
    return True if goal == 0 else False

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(f"Input: nums = {nums}")
    print(f"Output: {canJump(nums)}")
