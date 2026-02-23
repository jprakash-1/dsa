"""
Problem: Target Sum
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
"""

def findTargetSumWays(nums, target):
    # dp acts as a cache (memoization) to store results of subproblems we've already solved.
    # Key: (current_index_in_nums, current_running_total)
    # Value: Total number of valid ways to reach the final target from this state.
    dp = {}  

    # Recursive Backtracking function
    def backtrack(i, total):
        # Base Case: We've made a +/- decision for EVERY number in the array.
        if i == len(nums):
            # If our running 'total' matches the required 'target', we found 1 valid way!
            return 1 if total == target else 0
            
        # Optimization: If we've seen this exact state (index, total) before, 
        # just return the saved answer. Don't recalculate!
        if (i, total) in dp:
            return dp[(i, total)]

        # We have two choices for the current number: ADD it or SUBTRACT it.
        # We branch out into two recursive calls and sum up the valid ways from both.
        dp[(i, total)] = backtrack(i + 1, total + nums[i]) + \
                         backtrack(i + 1, total - nums[i])
                         
        return dp[(i, total)]

    # Kick off the backtracking starting at index 0 with a running total of 0.
    return backtrack(0, 0)

if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {findTargetSumWays(nums, target)}")
