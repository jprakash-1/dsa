"""
Problem: Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product, and return the product.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
"""

def maxProduct(nums):
    # Initialize the result with the first element
    res = nums[0]
    
    # We MUST track both the current max AND the current min.
    # Why track the min? Because a massive NEGATIVE number (currMin) 
    # multiplied by another NEGATIVE number becomes a massive POSITIVE number!
    curMin, curMax = 1, 1
    
    for n in nums:
        # We need a temporary variable for curMax because we are about to update it,
        # but we still need its old value to calculate the new curMin in the next step.
        tmp = curMax * n
        
        # The new curMax is the maximum of:
        # 1. n * old_curMax (if n is positive, this gets bigger)
        # 2. n * curMin (if both are negative, this becomes a large positive!)
        # 3. just 'n' itself (if we want to start a fresh subarray from here)
        curMax = max(n * curMax, n * curMin, n)
        
        # Similarly, the new curMin is the minimum of those three scenarios.
        curMin = min(tmp, n * curMin, n)
        
        # Update our absolute maximum result found so far
        res = max(res, curMax)
        
    return res

if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(f"Input: nums = {nums}")
    print(f"Output: {maxProduct(nums)}")
