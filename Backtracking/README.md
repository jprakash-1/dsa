# Backtracking - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
Backtracking is essentially **Depth First Search (DFS)** applied specifically to finding valid combinations, permutations, or subsets of data. Unlike a standard DFS over a Graph/Tree where you simply "visit" nodes to find a path, Backtracking actively **builds a state** (like appending to a `path` array) as it traverses deeper. 

The core mechanical identifier of Backtracking is the "Undo" step. When you drill down into a decision branch and it either:
1. Reaches a valid baseline solution (so you save a copy of it).
2. Hits a constraint violation (so you know this branch is a dead-end).
You must `pop()` or "undo" the last choice you made to physically back up the Tree of decisions, allowing the algorithm to cleanly try the *next* sibling choice without the old stale data corrupting the `path` array.

### 🤔 When to use Backtracking:
- **Combinatorics**: If the problem explicitly asks you to generate "All Permutations", "All Combinations", or "All Subsets". 
- **Constraint Satisfaction Puzzles**: Problems like Sudoku, N-Queens, or Word Search where you must place elements adhering to strict localized rules. If a rule is broken, you immediately backtrack to try a different configuration.
- **Explicit "Find all ways..." phrasing**: Anytime the prompt requires generating an exhaustive list of possibilities rather than just returning a single maximum/minimum integer value (which would imply Dynamic Programming).

### Generic Pseudocode Pattern
```python
def solve_backtracking(options):
    res = []
    
    # 'start_index' prevents us from reusing old elements if order doesn't matter (Combinations/Subsets)
    # 'current_path' holds the ongoing trajectory of our choices
    def backtrack(start_index, current_path):
        
        # Base Case: Did we successfully build a valid sequence?
        if is_goal(current_path):
            # 🚨 CRITICAL: Append a COPY [:] so future .pop() calls don't erase the saved result
            res.append(current_path.copy()) 
            return
            
        for i in range(start_index, len(options)):
            if not is_valid(options[i]):
                continue
            
            # 1. Make a Choice (Add to state)
            current_path.append(options[i])
            
            # 2. Recursively Explore that Choice
            # Use 'i' if you CAN reuse the same element (e.g., Combination Sum I)
            # Use 'i + 1' if you CANNOT reuse the same element
            backtrack(i + 1, current_path)
            
            # 3. Undo the Choice (Backtrack!)
            current_path.pop()
            
    backtrack(0, [])
    return res
```

---

## 📚 Problem Breakdowns

### 1. Subsets
- **Intuition**: At every single element `nums[i]`, we have precisely two choices forming a binary tree: **Include it** in our current subset, or **Exclude it**. We explicitly code both decisions at every structural level of the recursion.
- **Time Complexity**: `O(N * 2^N)` (2^N subsets, takes N to copy each)
- **Space Complexity**: `O(N)` for the recursion stack
- **Pseudocode**:
  ```python
  def dfs(i):
      if i >= len(nums):
          res.append(subset.copy()); return
      # Decision 1: INCLUDE nums[i]
      subset.append(nums[i])
      dfs(i + 1)
      # Decision 2: EXCLUDE nums[i]
      subset.pop()
      dfs(i + 1)
  ```

### 2. Combination Sum
- **Intuition**: We want to reach a `target` sum. The catch: we can reuse elements unlimited times. The binary decision branch is slightly different here: Decision 1 is "Include `candidates[i]` BUT stay at index `i`" (allowing us to pick it again). Decision 2 is "Skip `candidates[i]` entirely and move to `target_i + 1`".
- **Time Complexity**: `O(N ^ (target / min_val))`
- **Space Complexity**: `O(target / min_val)`
- **Pseudocode**:
  ```python
  def dfs(i, cur, total):
      if total == target: res.append(cur.copy()); return
      if i >= len(candidates) or total > target: return
      
      cur.append(candidates[i])
      dfs(i, cur, total + candidates[i]) # Note: We pass 'i', not 'i + 1'
      cur.pop()
      dfs(i + 1, cur, total)
  ```

### 3. Permutations
- **Intuition**: We need all arrangements. Because `[1,2] != [2,1]`, order matters. This means we cannot use a `start_index` to restrict looping. Every recursive step must loop from `0` to `N` exploring all unused elements. Since `nums` has distinct elements, we can just check `if element not in path` to know if it's unused.
- **Time Complexity**: `O(N * N!)`
- **Space Complexity**: `O(N)`
- **Pseudocode**:
  ```python
  def dfs(path):
      if len(path) == len(nums):
          res.append(path.copy()); return
      for n in nums:
          if n not in path:
              path.append(n)
              dfs(path)
              path.pop()
  ```

### 4. Word Search
- **Intuition**: Try to start the word from every single cell in the Matrix. For a valid starting cell, run DFS checking its 4 neighbors `(Top, Bottom, Left, Right)`. To prevent looping back on ourselves (e.g., `A -> B -> A`), we must temporarily mark the cell as `visited`. Critically, after the DFS explores that cell's paths, we must *unmark* it (Backtrack) so other valid paths don't treat it as permanently blocked.
- **Time Complexity**: `O(N * M * 4^L)` where L is word length
- **Space Complexity**: `O(L)`
- **Pseudocode**:
  ```python
  def dfs(r, c, i):
      if i == len(word): return True
      if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path:
          return False
      path.add((r, c)) # Make Choice
      res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
      path.remove((r, c)) # Undo Choice
      return res
  ```
