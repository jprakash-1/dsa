# Binary Search - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
Binary Search is the ultimate tool for navigating **sorted sequences** (arrays, matrices, or abstract search spaces). Instead of scanning sequentially which takes `N` operations (linear time), Binary Search consistently divides the search space exactly in half.

By evaluating a midpoint against a target condition, you mathematically eliminate 50% of the remaining possibilities with a single `if` check. This rapid halving reduces a massive search space `N` down to just `1` in `log2(N)` steps, achieving an incredibly fast `O(log N)` runtime. (E.g., searching 1 million items takes at most 20 checks).

The core difficulty of Binary Search is not the halving mechanism itself, but rather carefully defining what the *search space* is, and accurately defining the structural boundaries `left` and `right`.

### 🤔 When to use Binary Search:
- **Sorted Array Searching**: The canonical trigger. If the problem states "sorted array" and asks for a target or an extreme limit, Binary Search is almost definitely expected over an `O(N)` loop.
- **Rotated Sorted Arrays**: Arrays shifted structurally around a pivot (e.g., `[4,5,6,1,2,3]`). Although they look broken, they always consist of two perfectly sorted halves. You can identify which half the midpoint falls into and search accordingly.
- **Matrix Searching**: A 2D matrix where every row is conceptually strictly sorted and connected smoothly to the next row can be flattened conceptually into a 1D array purely by index math (`row = index // COLS`, `col = index % COLS`).
- **Binary Search on Answer (Parameter Searching)**: An advanced technique. If you are asked to "find the minimum capacity" or "find the maximum speed" and the problem behavior is *monotonic* (meaning: if speed `X` works, all speeds `> X` also work; if `X` fails, all speeds `< X` also fail), you can binary search the *answers themselves* between the minimum possible capability and the maximum possible capability.

### Generic Pseudocode Pattern
```python
def binary_search(arr, target):
    # Establish full search boundary
    l, r = 0, len(arr) - 1
    
    # Must use <= if the target can exist precisely when window shrinks to 1 item
    while l <= r:
        # Avoids numerical integer overflow in languages natively like Java/C++
        mid = l + (r - l) // 2 
        
        if arr[mid] == target:
            return mid # Element found
        elif arr[mid] < target:
            l = mid + 1 # Target must be strictly to the right
        else:
            r = mid - 1 # Target must be strictly to the left
            
    return -1
```

---

## 📚 Problem Breakdowns

### 1. Search a 2D Matrix
- **Intuition**: A strictly sorted matrix (`row_i[-1] < row_{i+1}[0]`) is computationally mathematically equivalent to a single long sorted 1D array logically split. We could do a single binary search using modulo index math, but it's often cleaner to do **Two Consecutive Binary Searches**. The first binary search evaluates strictly looking at the First and Last element of every row to physically map and isolate the correct Row. The second binary search isolates the exact localized column within that specific row.
- **Time Complexity**: `O(log M + log N)` -> `O(log(M*N))`
- **Space Complexity**: `O(1)`
- **Pseudocode**:
  ```python
  top, bot = 0, len(matrix) - 1
  while top <= bot:     # Find strictly the correct Row
      row = (top + bot) // 2
      if target > matrix[row][-1]: top = row + 1
      elif target < matrix[row][0]: bot = row - 1
      else: break       # Row mathematically found!
  if not (top <= bot): return False
  
  l, r = 0, len(matrix[0]) - 1
  while l <= r:         # Find localized target explicitly inside row
      m = (l + r) // 2
      if target > matrix[row][m]: l = m + 1
      elif target < matrix[row][m]: r = m - 1
      else: return True
  return False
  ```

### 2. Koko Eating Bananas
- **Intuition**: A prime example of **Binary Search on Answer**. Koko's speed `k` exists mathematically between `1` (the slowest possible speed) and `max(piles)` (the fastest necessary speed since she can only eat one pile per hour). The relationship is strictly monotonic: the faster `k` is, the strictly shorter the hours required. We Binary Search `k`. For a selected `mid` speed, we linearly loop checking how many hours it takes. If she can finish `(hours <= h)`, record the success but try to find an explicitly slower minimum valid speed `(r = mid - 1)`. If she fails inherently, she must eat strictly faster `(l = mid + 1)`.
- **Time Complexity**: `O(N * log(Max Pile Size))` Where N is piles length
- **Space Complexity**: `O(1)`
- **Pseudocode**:
  ```python
  l, r = 1, max(piles)
  res = r
  while l <= r:
      k = (l + r) // 2
      hours = 0
      for p in piles: hours += math.ceil(p / k)
      if hours <= h: res = min(res, k); r = k - 1
      else: l = k + 1
  return res
  ```

### 3. Find Minimum in Rotated Sorted Array
- **Intuition**: A rotated array mathematically looks like two upward ascending lines separated by a cliff. We want the absolute bottom of the structural cliff. The critical check mapping bounds: if `nums[l] < nums[r]`, the subarray is perfectly sorted unbroken globally, therefore `nums[l]` is mathematically the absolute minimum. If not, evaluate the midpoint. If `nums[mid] >= nums[l]`, the left half is structurally perfectly sorted, meaning the cliff inherently rests strictly in the right half `(l = mid + 1)`. Else, the cliff rests on the left side explicitly.
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
- **Pseudocode**:
  ```python
  res = nums[0]
  l, r = 0, len(nums) - 1
  while l <= r:
      if nums[l] < nums[r]: res = min(res, nums[l]); break
      m = (l + r) // 2
      res = min(res, nums[m])
      if nums[m] >= nums[l]: l = m + 1
      else: r = m - 1
  return res
  ```

### 4. Search in Rotated Sorted Array
- **Intuition**: Similar logic structure limiting bounds tracing `Find Minimum`. First, determine mathematically strictly which half of the array is perfectly sorted unbroken natively checking `nums[l] <= nums[mid]`. Once you establish the explicitly sorted half, purely natively mathematically check if the `target` bounds fall logically within that perfect strictly structured range. If it does, search that half. If it doesn't, search the other conceptually broken half.
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
- **Pseudocode**:
  ```python
  l, r = 0, len(nums) - 1
  while l <= r:
      mid = (l + r) // 2
      if target == nums[mid]: return mid
      if nums[l] <= nums[mid]:    # Left is strictly sorted
          if target > nums[mid] or target < nums[l]: l = mid + 1
          else: r = mid - 1
      else:                       # Right is strictly sorted
          if target < nums[mid] or target > nums[r]: r = mid - 1
          else: l = mid + 1
  return -1
  ```

### 5. Time Based Key-Value Store
- **Intuition**: We are tasked with building a `HashMap` where `keys` securely point to strictly multiple `values` inherently bound specifically by appending `timestamps`. Because the problem mathematically guarantees timestamps are explicitly added strictly in **increasing chronological order**, the values lists inside the map are inherently structurally sorted. To efficiently return natively the largest timestamp `<= target`, execute a Binary Search directly explicitly on the mapped lists.
- **Time Complexity**: `O(1)` for strictly set(), `O(log N)` for get() natively.
- **Space Complexity**: `O(N)` scaling structurally bounding map.
- **Pseudocode**:
  ```python
  def get(self, key, timestamp):
      res = ""
      values = self.store.get(key, [])
      l, r = 0, len(values) - 1
      while l <= r:
          m = (l + r) // 2
          if values[m][1] <= timestamp:
              res = values[m][0]
              l = m + 1
          else: r = m - 1
      return res
  ```
