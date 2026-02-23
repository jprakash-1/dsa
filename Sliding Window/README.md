# Sliding Window - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
The Sliding Window is a dynamic variant of the Two Pointers technique. Instead of `left` and `right` moving towards each other, they move in the same direction, framing a contiguous subarray or substring (the "window"). 

The primary goal of a Sliding Window is to **eliminate redundant work**. In a brute-force approach, to evaluate all subarrays, you would use a nested loop `O(N^2)`, re-calculating the inner elements repeatedly. A Sliding Window transforms this into an `O(N)` solution: as the window slides forward, you simply `add` the effect of the new element entering the window on the right, and `subtract` the effect of the old element leaving the window on the left.

The window expands by moving `right` when it can safely absorb more elements without violating constraints. It shrinks by moving `left` when constraints are broken, continuing to shrink until the window is valid again.

### 🤔 When to use Sliding Window:
- **Contiguous Subarrays/Substrings**: This is the massive giveaway. If the problem asks for the "longest," "shortest," or "maximum" *contiguous* sequence, Sliding Window is almost certainly the optimal approach.
- **Fixed Size Windows**: E.g., "Find the max sum of a subarray of size K". The `len(window)` is always `K`. You move `right` and simultaneously move `left` to maintain the exact size.
- **Dynamic Size Windows (Condition Based)**: E.g., "Find the longest substring distinct characters". The window expands until a duplicate is found, then shrinks from the left until the duplicate is evicted. The window size breathes dynamically.

### Generic Pseudocode Pattern
```python
def sliding_window_dynamic(arr):
    left = 0
    res = 0 # Track max length, min length, max sum, etc.
    state = initialize_state() # Hash map, set, sum variable, etc.
    
    for right in range(len(arr)):
        # 1. Expand the window by adding the new element at 'right'
        state.add(arr[right]) 
        
        # 2. If the window violates the problem's constraints, shrink it
        while condition_is_invalid(state):
            state.remove(arr[left]) # Remove effect of left element
            left += 1               # Shrink window
            
        # 3. Process the valid window and update the result
        res = max(res, right - left + 1)
        
    return res
```

---

## 📚 Problem Breakdowns

### 1. Longest Substring Without Repeating Characters
- **Intuition**: We want a dynamically sizing window ensuring all characters inside are unique. As we expand `right`, we track seen characters in a Set. If `s[right]` exists in our Set, our window is instantly invalid. We must forcibly shrink the window from the `left`, removing characters from the Set, until the duplicate is evicted.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)` (Space bounded by the character set size, e.g., max 26 or 128 characters)
- **Pseudocode**:
  ```python
  charSet = set()
  l = 0; res = 0
  for r in range(len(s)):
      while s[r] in charSet:
          charSet.remove(s[l])
          l += 1
      charSet.add(s[r])
      res = max(res, r - l + 1)
  return res
  ```

### 2. Longest Repeating Character Replacement
- **Intuition**: A window is valid if: `(Length of Window) - (Count of most frequent char) <= K`. The `K` represents our literal allowance of flips. As we expand `right`, we update our frequency HashMap and track `max_freq_count`. If the condition is violated, we increment `left` and decrement `s[left]`'s count. 
  *Note on optimization:* `max_freq_count` doesn't strictly need to be recalculated when shrinking because we only care about finding a *historically longer* valid window.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)` (Array/dict of size 26)
- **Pseudocode**:
  ```python
  count = {}
  l = 0; maxf = 0
  for r in range(len(s)):
      count[s[r]] = 1 + count.get(s[r], 0)
      maxf = max(maxf, count[s[r]])
      while (r - l + 1) - maxf > k:
          count[s[l]] -= 1
          l += 1
      res = max(res, r - l + 1)
  return res
  ```

### 3. Permutation in String
- **Intuition**: A string is a permutation of another if their character frequencies are completely identical. This translates to a **Fixed Size Sliding Window**. We maintain a window exactly the size of `len(s1)` traversing `s2`. We compare an array of 26 character counts for `s1` with the array for our current window in `s2`. To mathematically achieve `O(1)` window sliding, we track an integer `matches` (0 to 26) representing how many characters have identical frequencies.
- **Time Complexity**: `O(N)` where N is length of s2
- **Space Complexity**: `O(1)` (Two maps size 26)
- **Pseudocode**:
  ```python
  if len(s1) > len(s2): return False
  s1Count, s2Count = [0]*26, [0]*26
  # Initialize first window
  for i in range(len(s1)): s1Count[ord(s1[i])-97] += 1; s2Count[ord(s2[i])-97] += 1
  matches = 0 # Calculate initial matches
  for i in range(26): if s1Count[i] == s2Count[i]: matches += 1
  
  l = 0
  for r in range(len(s1), len(s2)):
      if matches == 26: return True
      # Add s2[r] to s2Count, update matches
      # Remove s2[l] from s2Count, update matches
      l += 1
  return matches == 26
  ```
