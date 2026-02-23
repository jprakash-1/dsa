# Arrays & Hashing - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
At the heart of almost all algorithmic optimizations involving arrays and strings is the **Time-Space Tradeoff**. We want to avoid nested loops (which result in `O(N^2)` time complexity). The most direct way to do this is by spending extra memory (`O(N)` space) to remember what we've previously seen. 

**Hash Maps (Dictionaries)** and **Hash Sets** are the ultimate tools for this. They allow us to store and retrieve data in average `O(1)` constant time. Behind the scenes, a Hash Map uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. 

When you iterate through an array, instead of looking forward to find a match (which takes `O(N)` time for each element), you look *backward* at your Hash Map to see if the complement or required element has already been processed. This reduces quadratic `O(N^2)` searches to linear `O(N)` passes.

### 🤔 When to use Hash Maps/Sets:
- **Frequency Counting**: Any time you hear "find the most frequent," "group by character counts," or "check for duplicates." A Hash Map is perfect for building histograms of data.
- **Lookup/Existence Checking**: When you need to answer the question "Have I seen this value before?" in `O(1)` time, preventing redundant searches.
- **Mapping Complements**: In problems like *Two Sum*, you're looking for a `target - current_value`. A Hash Map stores `current_value` as you iterate, so you can instantly check if the complement exists.
- **Index Tracking**: When you not only need to know *if* a value exists, but *where* it is located (e.g., mapping `value -> index` to calculate distances between elements).

### Generic Pseudocode Pattern
```python
def solve(nums):
    # Use {} if you need to store metadata (like indices or counts)
    # Use set() if you only care about boolean existence
    seen = {} 
    
    for i, num in enumerate(nums):
        # 1. Check if the element (or its complement) is in our memory
        if condition_met(num, seen):
            return result
            
        # 2. Store the current element's state for future lookups
        seen[num] = i # or seen[num] = seen.get(num, 0) + 1
        
    return default
```

---

## 📚 Problem Breakdowns

### 1. Group Anagrams
- **Intuition**: Anagrams have the exact same character frequencies. Sorting a string works, but takes `O(K log K)`. Counting the characters takes `O(K)`. We use an array of size 26 to count character frequencies, convert that array into a tuple, and use it as a key in a Hash Map.
- **Time Complexity**: `O(N * K)` where `N` is number of strings, `K` is max length of string.
- **Space Complexity**: `O(N * K)`
- **Pseudocode**:
  ```python
  res = defaultdict(list)
  for s in strs:
      count = [0] * 26
      for char in s: count[ord(char) - ord('a')] += 1
      res[tuple(count)].append(s)
  return res.values()
  ```

### 2. Top K Frequent Elements
- **Intuition**: Instead of using a Heap (`O(N log K)`) or sorting the counts (`O(N log N)`), we use **Bucket Sort**. The frequency of any element can be at most `N`. We create an array of lists `freq` where the index represents the frequency, and the list contains numbers with that frequency.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Pseudocode**:
  ```python
  count = {}
  for n in nums: count[n] = 1 + count.get(n, 0)
  freq_buckets = [[] for i in range(len(nums) + 1)]
  for num, freq in count.items(): freq_buckets[freq].append(num)
  # iterate freq_buckets backwards to collect K elements
  ```

### 3. Encode and Decode Strings
- **Intuition**: To safely encode strings containing any character, we prepend the *length* of the string followed by a special delimiter like `#`. `"code"` becomes `"4#code"`. During decoding, we read the integer length until the `#`, then slice exactly that many characters.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Pseudocode**:
  ```python
  encode: res += str(len(s)) + "#" + s
  decode: while i < len(s): read length until '#', slice s[j:j+length], move pointer
  ```

### 4. Product of Array Except Self
- **Intuition**: Division isn't allowed. The product for `nums[i]` is exactly `(product of all left elements) * (product of all right elements)`. We use the output array to store the prefix products directly. Then, we do a second right-to-left pass, multiplying the stored prefix by a running `postfix` value.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)` (excluding output array)
- **Pseudocode**:
  ```python
  res = [1] * N
  prefix = 1
  for i in range(N): res[i] = prefix; prefix *= nums[i]
  postfix = 1
  for i in range(N-1, -1, -1): res[i] *= postfix; postfix *= nums[i]
  ```

### 5. Valid Sudoku
- **Intuition**: A Sudoku board has 3 constraints: rows, columns, and 3x3 sub-boxes. We use Hash Sets to ensure uniqueness. The key insight is identifying the 3x3 board: the coordinate `(r // 3, c // 3)` uniquely identifies which of the 9 sub-boxes a cell belongs to.
- **Time Complexity**: `O(9^2)` -> `O(1)`
- **Space Complexity**: `O(9^2)` -> `O(1)`
- **Pseudocode**:
  ```python
  rows, cols, squares = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
  for r in range(9):
      for c in range(9):
          val = board[r][c]
          if val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]: return False
          # add val to respective sets
  return True
  ```

### 6. Longest Consecutive Sequence
- **Intuition**: Finding consecutive sequences in an unsorted array is hard. If we convert it to a Hash Set, lookups become `O(1)`. The critical trick: a number is the *start* of a sequence ONLY if `(num - 1)` is NOT in the set. If it is the start, we simply count upward `(num + 1)`, `(num + 2)` checking the set to find the full length.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Pseudocode**:
  ```python
  numSet = set(nums)
  max_length = 0
  for n in nums:
      if (n - 1) not in numSet:
          length = 1
          while (n + length) in numSet: length += 1
          max_length = max(max_length, length)
  return max_length
  ```
