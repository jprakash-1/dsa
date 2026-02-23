"""
Problem: Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
"""

def lengthOfLIS(nums):
    # LIS array will store the length of the Longest Increasing Subsequence
    # starting at each specific index.
    # We initialize it with 1s because every individual number is technically
    # an increasing subsequence of length 1.
    LIS = [1] * len(nums)
    
    # We build our solution BACKWARDS, starting from the end of the array.
    for i in range(len(nums) - 1, -1, -1):
        
        # For the current number at index 'i', we look at every number that comes AFTER it (index 'j')
        for j in range(i + 1, len(nums)):
            
            # If the current number is strictly smaller than the later number,
            # we can append our current number to the sequence starting at 'j'.
            if nums[i] < nums[j]:
                # Update the LIS at 'i' to be the max between:
                # 1. Its current known best
                # 2. 1 (for the current number) + the LIS starting at 'j'
                LIS[i] = max(LIS[i], 1 + LIS[j])
                
    # The absolute longest sequence could start at ANY index, so we return the max value found.
    return max(LIS)

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Input: nums = {nums}")
    print(f"Output: {lengthOfLIS(nums)}")
