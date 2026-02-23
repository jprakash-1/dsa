"""
Problem: Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
"""

def combinationSum2(candidates, target):
    # Sorting is essential! It places identical numbers adjacent to each other.
    # This makes it very easy to skip duplicates and avoid generating duplicate combinations.
    candidates.sort()
    res = []
    
    # We use Depth-First Search (DFS) / Backtracking.
    def dfs(pos, cur, target):
        # Base Case 1: We hit the target sum exactly!
        if target == 0:
            res.append(cur.copy())
            return
            
        # Base Case 2: We overshot the target sum (since all numbers are positive).
        if target < 0:
            return
            
        # 'prev' keeps track of the last number we tried at this specific depth.
        prev = -1
        for i in range(pos, len(candidates)):
            # If this candidate is the EXACT same as the previous one we just tried, skip it!
            # This prevents duplicate combinations like [1, 2, 5] and another [1, 2, 5].
            if candidates[i] == prev:
                continue
                
            # Decision 1: INCLUDE the current candidate.
            cur.append(candidates[i])
            
            # Since we can only use each number ONCE, the next step starts at index 'i + 1'.
            dfs(i + 1, cur, target - candidates[i])
            
            # Backtrack: Undo our last choice to explore a different combination.
            cur.pop()
            
            # Update 'prev' to the number we just finished exploring.
            prev = candidates[i]
            
    # Start DFS at index 0, with an empty list, and the initial target sum.
    dfs(0, [], target)
    return res

if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(f"Input: candidates = {candidates}, target = {target}")
    print(f"Output: {combinationSum2(candidates, target)}")
