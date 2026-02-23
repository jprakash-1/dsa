# Two Pointers - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
The Two Pointers technique involves iterating over an array from two different positions simultaneously. Standard iterations use one pointer starting from index `0`. Two pointers usually initialize one pointer at the start (`left = 0`) and one at the end (`right = len(arr) - 1`), moving them towards each other until they meet.

The power of Two Pointers shines in **sorted arrays**. When an array is sorted, the relative magnitudes of the endpoints are known (left is smallest, right is largest). By evaluating a condition involving both pointers (like their sum), you gain logical certainty on which pointer to move:
- If the evaluated sum is **too large**, moving the `left` pointer forward will only make it larger. Therefore, you *must* move the `right` pointer backward to decrease the sum.
- If the evaluated sum is **too small**, moving the `right` pointer backward makes it smaller. Therefore, you *must* move the `left` pointer forward to increase the sum.

This intelligent narrowing completely eliminates the need to check every pair (which takes `O(N^2)`), shrinking the search space directly to the answer in linear `O(N)` time.

### 🤔 When to use Two Pointers:
- **Sorted Arrays Searching for Pairs**: Anytime you need to find two numbers in a sorted array that sum to a target, or meet a specific proportional constraint.
- **Palindrome Verification**: Checking if a string reads the same forwards and backwards fundamentally requires comparing the outermost characters and moving inward.
- **Partitioning / Swapping**: Problems like "Move Zeros to the end" or "Sort Colors (Dutch National Flag)" use two pointers moving from the same side (fast and slow) or opposite sides to swap elements in-place.
- **Maximizing/Minimizing Area**: When width `(right - left)` is a factor in a calculation (like Container With Most Water), and you want to evaluate constraints dynamically while the width shrinks.

### Generic Pseudocode Pattern
```python
def solve_two_pointers(arr, target):
    # Sort the array if not already sorted (costs O(N log N))
    # Note: Only sort if the original indices are no longer needed!
    arr.sort() 
    
    left, right = 0, len(arr) - 1
    
    while left < right: # Use <= if the two pointers can point to the same element
        curr_val = check(arr[left], arr[right])
        
        if curr_val == target:
            return True # or return [left, right]
        elif curr_val > target:
            right -= 1 # The value is too big, shrink from the top end
        else:
            left += 1  # The value is too small, grow from the bottom end
            
    return False
```

---

## 📚 Problem Breakdowns

### 1. Two Sum II (Input Array Is Sorted)
- **Intuition**: This is the textbook Two Pointers application. Because it is strictly sorted, we start at the outer edges. Sum `nums[l]` and `nums[r]`. If it matches the target, we're done. If the sum is greater than the target, `r` is too big, so `r -= 1`. If the sum is smaller, `l` is too small, so `l += 1`.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
- **Pseudocode**:
  ```python
  l, r = 0, len(numbers) - 1
  while l < r:
      curr = numbers[l] + numbers[r]
      if curr == target: return [l + 1, r + 1] # 1-indexed
      elif curr > target: r -= 1
      else: l += 1
  ```

### 2. 3Sum
- **Intuition**: `3Sum` is just `Two Sum` wrapped in a loop. We iterate `i` from 0 to N. For each `nums[i]`, the problem reduces to finding two other numbers that sum to `-nums[i]`. We use Two Pointers `(l = i + 1, r = len - 1)` for the remainder of the array. The hardest part is skipping duplicates: if `nums[i] == nums[i-1]`, we must `continue` to avoid duplicate triplets.
- **Time Complexity**: `O(N^2)` (Sorting is `O(N log N)`, traversing is `N * N`)
- **Space Complexity**: `O(1)` or `O(N)` depending on sorting implementation.
- **Pseudocode**:
  ```python
  nums.sort()
  res = []
  for i, a in enumerate(nums):
      if i > 0 and a == nums[i - 1]: continue
      l, r = i + 1, len(nums) - 1
      while l < r:
          threesum = a + nums[l] + nums[r]
          if threesum > 0: r -= 1
          elif threesum < 0: l += 1
          else:
              res.append([a, nums[l], nums[r]])
              l += 1; r -= 1
              while nums[l] == nums[l-1] and l < r: l += 1
  return res
  ```

### 3. Container With Most Water
- **Intuition**: Area = `width * height`. Width is `r - l`. Height is limited by the shorter of the two lines: `min(height[l], height[r])`. Starting at the outer edges gives us the maximum possible width. Since any inward move decreases the width, we should only move a pointer if it offers a chance at a taller line. Thus, we always move the pointer that is currently pointing to the shorter line.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
- **Pseudocode**:
  ```python
  l, r = 0, len(height) - 1
  res = 0
  while l < r:
      area = (r - l) * min(height[l], height[r])
      res = max(res, area)
      if height[l] < height[r]: l += 1
      else: r -= 1
  return res
  ```
