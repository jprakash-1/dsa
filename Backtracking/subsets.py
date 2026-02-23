"""
Problem: Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

def subsets(nums):
    res = []
    subset = []
    
    # Depth-First Search (DFS) / Backtracking helper
    # 'i' represents the current index in the 'nums' array we are looking at.
    def dfs(i):
        # Base Case: If 'i' has reached the end of the array, we have made a decision
        # for every single number (either include or exclude). 
        # So, we add a COPY of our current subset to the complete result list.
        if i >= len(nums):
            res.append(subset.copy())
            return
            
        # Decision Branch 1: INCLUDE the number at index 'i'.
        subset.append(nums[i])
        dfs(i + 1) # Move on to make a decision about the NEXT number.
        
        # Decision Branch 2: DO NOT INCLUDE the number at index 'i'.
        # We must 'pop' the last added number to reverse our previous decision (Backtracking).
        subset.pop()
        dfs(i + 1) # Move on to make a decision about the NEXT number without 'nums[i]'.
        
    # Start the DFS process from index 0.
    dfs(0)
    return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"Input: nums = {nums}")
    print(f"Output: {subsets(nums)}")
