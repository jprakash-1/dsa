"""
Problem: Search in Rotated Sorted Array
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        # Target found!
        if target == nums[mid]:
            return mid
            
        # Left sorted portion
        # We know we're in the left sorted portion if the left element is <= mid element.
        if nums[l] <= nums[mid]:
            # If the target is strictly GREATER than the middle, 
            # OR strictly LESS than the leftmost element, it MUST be in the right half!
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            # Otherwise, it must be realistically nestled in this left sorted half.
            else:
                r = mid - 1
        # Right sorted portion
        else:
            # If the target is strictly LESS than the middle,
            # OR strictly GREATER than the rightmost element, it MUST be in the left half!
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            # Otherwise, it must be realistically nestled in this right sorted half.
            else:
                l = mid + 1
                
    # Target was not found in the array.
    return -1

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {search(nums, target)}")
