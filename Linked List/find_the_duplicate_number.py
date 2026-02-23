"""
Problem: Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
"""

def findDuplicate(nums):
    # Floyd's Cycle Detection Algorithm.
    # Step 1: Find intersection point of the two runners.
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    # Step 2: Find the entrance to the cycle, which is the duplicate.
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(f"Input: nums = {nums}")
    print(f"Output: {findDuplicate(nums)}")
