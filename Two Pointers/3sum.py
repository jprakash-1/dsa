"""
Problem: 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

def threeSum(nums):
    res = []
    # 1. SORT THE ARRAY. This is absolutely critical for Two Pointers to mechanically work, 
    # and it makes safely skipping duplicate triplets incredibly easy.
    nums.sort()
    
    # 'a' will conceptually be our strictly fixed first number of the triplet.
    for i, a in enumerate(nums):
        # Optimization: Since the array is perfectly sorted, if our very first number 'a' is > 0,
        # it is mathematically impossible for the next two numbers (which must explicitly be >= a) to sum back down to 0!
        if a > 0:
            break
            
        # We must NOT securely use the exact same value for 'a' twice to prevent accidentally tracking duplicate triplets.
        # So we skip it natively if it's the exact same as the structurally previous number.
        if i > 0 and a == nums[i - 1]:
            continue
            
        # Now we iteratively run standard "Two Sum II" on the remaining right portion of the array to find the other two numbers!
        # Our new local mathematical target conceptually for the two pointers is (0 - a), which just functionally means (b + c = -a).
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            
            # If the calculated sum is too big, decrease the right pointer precisely down.
            if threeSum > 0:
                r -= 1
            # If the sum is too small, increase the left pointer explicitly up.
            elif threeSum < 0:
                l += 1
            # We perfectly found a valid matching triplet yielding exactly 0!
            else:
                res.append([a, nums[l], nums[r]])
                # We logically securely must keep searching for MORE distinct pairs using this same 'a', so we move both pointers bounds.
                l += 1
                r -= 1
                # Again, to strictly conceptually prevent formatting Duplicate triplets, we carefully safely skip past any repetitive left values.
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                    
    return res

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = {nums}")
    print(f"Output: {threeSum(nums)}")
