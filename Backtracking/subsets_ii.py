"""
Problem: Subsets II
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""

def subsetsWithDup(nums):
    res = []
    # VERY IMPORTANT: Sort the array first! 
    # Sorting guarantees that duplicate numbers will be right next to each other.
    nums.sort()
    
    # Backtracking helper. 'i' is the current index, 'subset' is the path we are building.
    def backtrack(i, subset):
        # Base Case: We've made a decision for every number in the input list.
        if i == len(nums):
            res.append(subset[::]) # subset[::] is just a quick way to copy a list
            return
            
        # --- Decision Branch 1: INCLUDE the current number ---
        subset.append(nums[i])
        # Recursively make decisions for the rest of the array.
        backtrack(i + 1, subset)
        
        # Backtrack: Remove the number we just added so we can explore the "exclude" path.
        subset.pop()
        
        # --- Decision Branch 2: EXCLUDE the current number ---
        # The Trick: If we decide NOT to include nums[i], we must also NOT include
        # any identical numbers that follow it. Otherwise, we'll generate duplicate subsets.
        # We use a while loop to easily skip over all contiguous duplicate numbers.
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
            
        # Now 'i' is pointing to the LAST instance of that duplicate number.
        # So passing 'i + 1' correctly skips all of them.
        backtrack(i + 1, subset)
        
    # Kick off the backtracking process starting at index 0 with an empty subset.
    backtrack(0, [])
    return res

if __name__ == "__main__":
    nums = [1, 2, 2]
    print(f"Input: nums = {nums}")
    print(f"Output: {subsetsWithDup(nums)}")
