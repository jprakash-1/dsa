"""
Problem: Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
"""

def findMin(nums):
    res = nums[0]
    l, r = 0, len(nums) - 1
    
    # Binary search for the minimum element in O(log n) time
    while l <= r:
        # If the sub-array is strictly increasing, the left element is the minimum
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
            
        m = (l + r) // 2
        res = min(res, nums[m])
        
        # If the middle element is greater than or equal to the left element,
        # we are in the left sorted portion, so the minimum is to the right
        if nums[m] >= nums[l]:
            l = m + 1
        # Otherwise, we are in the right sorted portion, so minimum is to the left
        else:
            r = m - 1
            
    return res

if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(f"Input: nums = {nums}")
    print(f"Output: {findMin(nums)}")
