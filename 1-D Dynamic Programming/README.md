# 1-D Dynamic Programming - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
Dynamic Programming (DP) is inherently an optimization over standard Recursion. 

When a recursive algorithm branches to solve a problem (e.g., computing `Fibonacci(5)` inherently computes `Fibonacci(4)` and `Fibonacci(3)`), it often accidentally re-solves the exact same subproblems multiple times (because computing `Fibonacci(4)` *also* computes `Fibonacci(3)`). This redundancy leads to catastrophic `O(2^N)` exponential time complexities.

DP fixes this via **Memoization** (Top-Down caching) or **Tabulation** (Bottom-Up array building). 
- **Memoization**: Run normal recursion, but before returning an answer, save it to a Hash Map `cache[n] = answer`. The very first line of the recursive function checks: `if n in cache: return cache[n]`.
- **Tabulation**: Start at the absolute base cases (e.g., `dp[0]` and `dp[1]`) and iteratively loop upwards to `N`. Because `dp[i]` strictly relies on the already-computed answers of `dp[i-1]` and `dp[i-2]`, you simply look back at your array instead of calling a function.

This transforms `O(2^N)` nightmare branches into clean `O(N)` linear loops.

### 🤔 When to use 1-D DP:
- **Optimization Queries**: The problem asks for the "Maximum", "Minimum", or "Most Optimal" way to do something linearly (e.g., maximum profit, minimum coins, longest sequence).
- **Combinatorics (Number of Ways)**: The problem asks "How many ways can you reach step N?". If order doesn't matter or is fixed, it strongly implies DP. 
- **Overlapping Subproblems**: The "Choice" at step `i` entirely dictates its outcome based on the state of step `i-1` or `i-2`. If deciding to rob House 3 physically prevents you from robbing House 2, you have a mathematically overlapping constraint.

### Generic Tabulation Pattern (Bottom-Up)
```python
def solve1DDP(n, costs):
    # 1. Initialize a sequence mapping boundaries holding default limits
    dp = [0] * (n + 1)
    
    # 2. Determine base cases explicitly mapping bounds mathematically
    dp[0] = base_case_0
    dp[1] = base_case_1 # If required structurally
    
    # 3. Iterate sequentially building completely upon previous bounds inherently
    for i in range(2, n + 1):
        # The recurrence relation mapping mathematically explicit dependencies
        dp[i] = max(dp[i-1], costs[i] + dp[i-2]) 
        
    return dp[n]
```

---

## 📚 Problem Breakdowns

### 1. House Robber
- **Intuition**: At any given house `i`, you have exactly two choices: **Rob it** or **Skip it**. If you Rob it, you get `nums[i]` cash, but you are structurally blocked from robbing house `i-1`. Thus, the max cash you can logically have is `nums[i] + dp[i-2]`. If you Skip it, the max cash you logically have is simply whatever you had at `dp[i-1]`. The transaction logically evaluates `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`. Because we only ever look exactly 2 steps backwards, we don't even need a full array—just two integer variables.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)` memory tracking variables identically
- **Pseudocode**:
  ```python
  rob1, rob2 = 0, 0
  for n in nums:
      temp = max(n + rob1, rob2) # temp conceptually maps dynamically new rob2
      rob1 = rob2                # shift window variables explicitly overlapping
      rob2 = temp
  return rob2
  ```

### 2. House Robber II
- **Intuition**: The exact same dynamic strictly bounding `House Robber I`, but the list wraps circularly. Because it's a circle, robbing House[0] explicitly permanently prevents robbing House[-1] mapping limits logically. Therefore, we run the completely standard 1-D DP function **twice** linearly: Once on the array skipping specifically the last house `nums[:-1]`, and once on the array skipping explicitly the first house `nums[1:]`. We return the maximum of the two independent simulations.
- **Time Complexity**: `O(N)` evaluating tracking explicitly twice functionally bounds
- **Space Complexity**: `O(1)` bounds checking limits arrays dynamically
- **Pseudocode**:
  ```python
  def helper(nums): # Exactly House Robber I structurally natively bounds variables
      rob1, rob2 = 0, 0
      for n in nums: temp = max(n + rob1, rob2); rob1 = rob2; rob2 = temp
      return rob2
      
  return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
  ```

### 3. Longest Palindromic Substring
- **Intuition**: A palindrome inherently perfectly mirrors itself explicitly evaluating middle outwards limits checking structurally. Natively we evaluate completely iterating string limits `i`. Assuming conceptually `i` is the explicit middle mapping inherently odd palindromes, we use Two Pointers `l, r` expanding identically outwards testing explicitly checking `s[l] == s[r]`. We repeat completely identical expanding functionally evaluating even palindromes passing inherently logically `i, i+1`. 
- **Time Complexity**: `O(N^2)` checking explicitly boundaries overlapping
- **Space Complexity**: `O(1)` mapping limits natively identifying
- **Pseudocode**:
  ```python
  res = ""; resLen = 0
  for i in range(len(s)):
      # Odd Length Check bounds mapping implicitly evaluating matching
      l, r = i, i
      while l >= 0 and r < len(s) and s[l] == s[r]:
          if (r - l + 1) > resLen: res = s[l : r + 1]; resLen = r - l + 1
          l -= 1; r += 1
          
      # Even Length Check natively tracking parameters dynamically lengths identically mapping
      l, r = i, i + 1
      while l >= 0 and r < len(s) and s[l] == s[r]:
          if (r - l + 1) > resLen: res = s[l : r + 1]; resLen = r - l + 1
          l -= 1; r += 1
  return res
  ```

### 4. Coin Change
- **Intuition**: A classic conceptual Knapsack pattern evaluating perfectly tracking bound combinations identically wrapping limits. We want to functionally mathematically reach `amount`. We establish an array sized `amount + 1` filled entirely with explicitly impossible infinities `amount + 1`. We base map naturally `dp[0] = 0` (0 coins to make 0 amount). We dynamically iterate strictly `1 to amount`. For every value conceptually checking `a`, we loop our given `coins`. If `a - coin >= 0`, we mathematically conceptually check limits `dp[a] = min(dp[a], 1 + dp[a - coin])`.
- **Time Complexity**: `O(Amount * len(coins))` bounds
- **Space Complexity**: `O(Amount)`
- **Pseudocode**:
  ```python
  dp = [amount + 1] * (amount + 1)
  dp[0] = 0
  
  for a in range(1, amount + 1):
      for c in coins:
          if a - c >= 0:
              dp[a] = min(dp[a], 1 + dp[a - c])
              
  return dp[amount] if dp[amount] != amount + 1 else -1
  ```

### 5. Maximum Product Subarray
- **Intuition**: Unlike addition bounds mappings limits exactly tracking max sums, multiplying sequences perfectly inherently completely breaks mapping variables directly limits. A massive negative sequence mathematically limit bounds unexpectedly dynamically flips completely positive natively wrapping explicitly multiplying by another negative. Therefore, dynamically simultaneously logically limit strictly track *both* `cur_max` identically checking explicitly mapping limits `cur_min`. 
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)` boundaries limits evaluating dynamically wrapping limits
- **Pseudocode**:
  ```python
  res = nums[0]
  curMin, curMax = 1, 1
  for n in nums:
      if n == 0: curMin, curMax = 1, 1; res = max(res, 0); continue
      tmp = curMax * n
      curMax = max(n * curMax, n * curMin, n)
      curMin = min(tmp, n * curMin, n)
      res = max(res, curMax)
  return res
  ```
