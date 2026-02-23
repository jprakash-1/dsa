"""
Problem: Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

def productExceptSelf(nums):
    # We initialize our result array with 1s.
    # It will carefully store the final calculated product for each index.
    res = [1] * len(nums)
    
    # PREFIX PASS:
    # 'prefix' keeps a running product of all elements strictly to the LEFT of the current index.
    prefix = 1
    for i in range(len(nums)):
        # Store the current running prefix strictly BEFORE multiplying by the current number.
        res[i] = prefix
        # Update our running prefix product to include this current number for the NEXT loop iteration.
        prefix *= nums[i]
        
    # POSTFIX PASS:
    # 'postfix' keeps a running product of all elements strictly to the RIGHT of the current index.
    postfix = 1
    # We iterate backwards through the array.
    for i in range(len(nums) - 1, -1, -1):
        # We multiply what we already stored (the Left prefix) by the Right postfix.
        # Reasoning: This perfectly gives us: (Left Product) * (Right Product) = Product Except Self!
        res[i] *= postfix
        # Update our running postfix product to include this number for the NEXT loop going left.
        postfix *= nums[i]
        
    return res

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(f"Input: nums = {nums}")
    print(f"Output: {productExceptSelf(nums)}")
