"""
Problem: Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

def permute(nums):
    res = []
    
    # Base Case: A single number only has one permutation (itself).
    # We return a COPY of the list to avoid modifying it later in the recursive calls.
    if len(nums) == 1:
        return [nums.copy()]
        
    # We will pick each number in the list to be the "first" number of a permutation,
    # then recursively find all permutations of the REMAINING numbers.
    for i in range(len(nums)):
        # 1. Remove the current number from the list. It's our "fixed" starting element for now.
        n = nums.pop(0)
        
        # 2. Recursively find all permutations of the REST of the list.
        perms = permute(nums)
        
        # 3. For every permutation returned, append our "fixed" element 'n' to the END of it.
        for p in perms:
            p.append(n)
            
        # 4. Add all these newly formed permutations to our result list.
        res.extend(perms)
        
        # 5. BACKTRACK: Put the "fixed" element 'n' back into the list, but at the END!
        # This acts to naturally rotate the list elements so the next iteration 
        # picks a different "first" number.
        nums.append(n)
        
    return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"Input: nums = {nums}")
    print(f"Output: {permute(nums)}")
