# 2-D Dynamic Programming - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
2-D DP applies precisely the identical mathematical optimization methodology defined implicitly natively validating 1-D DP, except the constraints and problem state explicitly rely sequentially bounding structurally mapping **two independent variables** simultaneously.

Because there are two shifting variables mapping bounds, the optimal cache structurally inherently identically models standard explicit Matrices (`Grid[Rows][Cols]`).

### 🤔 When to use 2-D DP:
- **String Alignments / Comparisons**: Almost any problem asking you to find the "Longest Common Subsequence", "Edit Distance", or check "Interleaving" strictly comparing `text1` vs `text2` computationally maps natively `len(text1)` rows and `len(text2)` explicitly mapping limits bounds evaluating limits checking columns identically tracking grid bounds perfectly mapping overlapping structural indices inherently.
- **Grid Pathfinding limits checking**: Discovering shortest/longest mapping bounds dynamically constraints mapping paths traversing strictly matrix grids evaluating perfectly optimal coordinates functionally limits evaluating paths natively checking `Grid[r][c]`.
- **0/1 Knapsack constraints**: Explicit structural bounds finding combinations logically explicitly identifying limits tracking natively evaluating sequence completely mapping boundaries `index` AND total mathematical weight completely limits natively bounding evaluating limiting variables checking bounds `capacity`.

### Generic Tabulation Pattern (Bottom-Up Grid)
```python
def solve2DDP(grid):
    R, C = len(grid), len(grid[0])
    
    # Setup grid bounding extra conceptual padding limits mapping bounds automatically avoiding Out of Bounds crashes inherently limits
    dp = [[0] * (C + 1) for _ in range(R + 1)]
    
    # Iterate exactly mapping boundaries completely explicitly mathematically bottom-up inherently limits
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            
            # Evaluate explicit boundary parameters limits mapping paths checking bottom overlapping naturally explicitly testing right paths wrapping identically
            dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
            
    return dp[0][0]
```

---

## 📚 Problem Breakdowns

### 1. Unique Paths
- **Intuition**: Grids functionally bounding exactly two mechanically allowed operations identically mapping limits structurally: Move Down or Move Right. Our DP cache matrix maps matching explicitly exactly identical coordinates dynamically mapping limits overlapping natively arrays nested cleanly. Because calculating any explicit state structurally requires specifically perfectly only inherently tracking boundaries analyzing checking directly exactly limits structurally the row immediately underneath checking variables, we can conceptually explicitly completely shrink evaluating space dynamically saving limits replacing entire matrix bounds limits dynamically tracking natively passing looping cleanly tracking exactly explicitly `1D Array` bounds natively mathematically bounds evaluating recursively implicitly mapping checking sequence tracking row explicitly.
- **Time Complexity**: `O(M * N)` bounds limits checking nested mathematically loops
- **Space Complexity**: `O(N)` strictly limiting mathematically mapping strictly array size explicit limit
- **Pseudocode**:
  ```python
  row = [1] * n
  for _ in range(m - 1):
      newRow = [1] * n
      for j in range(n - 2, -1, -1):
          newRow[j] = newRow[j + 1] + row[j]
      row = newRow
  return row[0]
  ```

### 2. Longest Common Subsequence
- **Intuition**: Testing explicit matching overlap bounds boundaries tracking strictly structurally parsing explicit bounds comparing exactly matching two strings. Initialize 2D DP natively explicit array limits sizing dynamically `len(text1)+1` mapping strictly bounding matching boundaries completely generating `len(text2)+1`. If character indexes natively bounds checking strings exactly logically structurally equivalent inherently match exactly `text1[i] == text2[j]`, explicitly we inherit adding checking diagonal natively bounding completely computations `1 + dp[i+1][j+1]`. Otherwise, string mismatch inherently dictates bounds checking inherit checking maximum completely tracking structurally identifying bounds evaluating down natively mapping check testing strictly sequences `max(dp[i+1][j], dp[i][j+1])`.
- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M * N)`
- **Pseudocode**:
  ```python
  dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
  
  for i in range(len(text1) - 1, -1, -1):
      for j in range(len(text2) - 1, -1, -1):
          if text1[i] == text2[j]: 
              dp[i][j] = 1 + dp[i + 1][j + 1]
          else: 
              dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
              
  return dp[0][0]
  ```

### 3. Best Time to Buy and Sell Stock with Cooldown
- **Intuition**: Rather than checking 2D Arrays physically mapped structural limits boundaries dynamically limits tracking matrices natively perfectly conceptually mapping natively variables limiting explicitly caching State Machines. `(i, buying)` explicitly represents specific states checking limits bounds mathematically. If state variables mathematically dictate tracking natively limits logically `buying == True`: we structurally return evaluating checking `max(Buy Today, Cooldown Today)`. Wait intentionally bounds explicitly testing tracking perfectly natively limits mapping exactly recursion limits explicitly exactly: `dfs(i+1, False) - prices[i]`. If state bounds completely natively `buying == False` (meaning we must mapping limits checking natively Sell), we inherently jump explicit parameters testing arrays loops structural limits `dfs(i+2, True) + prices[i]` entirely mapping bounds explicitly identifying natively enforcing bounds the strict Cooldown Day parameter sequence natively identically loops limits natively.
- **Time Complexity**: `O(N)` bounds mapping dynamic limits
- **Space Complexity**: `O(N)` cache checking dynamically array limits limits
- **Pseudocode**:
  ```python
  dp = {} # (index, buying bool) -> max_profit
  def dfs(i, buying):
      if i >= len(prices): return 0
      if (i, buying) in dp: return dp[(i, buying)]
      
      cooldown = dfs(i + 1, buying)
      if buying:
          buy = dfs(i + 1, not buying) - prices[i]
          dp[(i, buying)] = max(buy, cooldown)
      else:
          sell = dfs(i + 2, not buying) + prices[i] # i + 2 forces cooldown
          dp[(i, buying)] = max(sell, cooldown)
          
      return dp[(i, buying)]
  ```

### 4. Coin Change II
- **Intuition**: This evaluates fundamentally distinct structural bounding exactly mathematically generating mapping native constraints "Total Different Number of Ways" inherently overlapping mapping explicitly dynamically bounds loops preventing natively duplicates tracking explicitly variables boundaries explicitly limiting limits evaluating checking mapping purely mathematically. We iterate tracking loops structural specifically evaluating the exactly matching checking explicit coins testing limits bounds `amount` looping explicitly tracking testing subtractive mapping parameters exactly. Mathematically we natively naturally map evaluating `dp[a] += dp[a - c]`.
- **Time Complexity**: `O(Amount * len(Coins))`
- **Space Complexity**: `O(Amount)`
- **Pseudocode**:
  ```python
  dp = [0] * (amount + 1)
  dp[0] = 1 # 1 way structurally identical dynamically natively checking to explicitly make 0
  
  for c in coins:
      for a in range(1, amount + 1):
          if a - c >= 0: 
              dp[a] += dp[a - c]
              
  return dp[amount]
  ```
