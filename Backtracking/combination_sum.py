"""
Problem: Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
"""

def combinationSum(candidates, target):
    res = []
    
    # We use Depth-First Search (DFS) / Backtracking to explore all unique combinations.
    # 'i' is the index in candidates we are currently considering.
    # 'cur' is the list of numbers we've chosen so far in this path.
    # 'total' is the mathematical sum of the numbers we currently hold.
    def dfs(i, cur, total):
        # Base Case 1: We successfully found a valid combination!
        if total == target:
            res.append(cur.copy())  # Must append a COPY, not the original reference!
            return
            
        # Base Case 2: We went out of bounds, OR our sum exceeded the target (no point in continuing).
        if i >= len(candidates) or total > target:
            return
            
        # Decision 1: INCLUDE the current candidate at index 'i'.
        # Since we can reuse the same number an unlimited number of times, we pass 'i' again!
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        
        # Backtrack: Undo our last choice to explore an alternative path.
        cur.pop()
        
        # Decision 2: EXCLUDE the current candidate entirely and conceptually move on to the next one.
        dfs(i + 1, cur, total)
        
    # Start DFS at index 0, with an empty starting combination and a running sum of 0.
    dfs(0, [], 0)
    return res

if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(f"Input: candidates = {candidates}, target = {target}")
    print(f"Output: {combinationSum(candidates, target)}")
