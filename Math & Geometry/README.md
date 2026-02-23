# Math & Geometry - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
Math and Geometry problems heavily diverge from standard data structure manipulation (like tracking pointers or dynamically caching array limits). Instead, they strictly computationally require you to conceptually identify a completely rigid **mathematical formula, geometric property, or matrix simulation pattern**.

Once you mathematically identify the specific behavioral rule (e.g., Matrix Rotation fundamentally equals Matrix Transposition followed exactly by Matrix Reversal), the actual coding implementation is usually extremely short and relies strictly on purely `O(1)` space native operations. 

The biggest conceptual hurdle here is identifying the hidden math laws and safely handling native integer numerical bounds (like overflows).

### 🤔 When to use Math & Geometry hacks:
- **Matrix Rotations / Spiral Traversals**: If the prompt asks you to physically morph a 2D Array structurally without extra space conceptually. It inherently implies a mathematical swapping formula mapping indices `(i, j)` to `(j, i)`, etc.
- **Power / Multiplication / Division Restrictions**: Problems asking you to calculate `Pow(x, n)` or `Divide Two Integers` strictly *without* using the native language operators (`**`, `*`, `/`). These inherently conceptually require binary manipulation constraints or logarithm-based `O(log N)` recursive breaking bounds.
- **Coordinate Grids / Points / Slopes**: Identifying rectangles or mapping slopes explicitly mathematically between arrays of `(X, Y)` coordinate limits. The mathematical slope formula `(y2 - y1) / (x2 - x1)` or conceptually distance computations `sqrt((x2-x1)^2 + (y2-y1)^2)` natively apply.

### Generic Conceptual Patterns
- **Matrix Rotation**: Instead of holding 4 coordinates and rotating them in a wildly complex nested loop, mathematically:
  1. **Transpose** the array: Swapping `matrix[i][j]` exactly with `matrix[j][i]`. (Turns columns into rows).
  2. **Reverse** the array rows: Explicitly `matrix[i].reverse()`. 
  This identically perfectly simulates an exact 90-degree mathematical rotation.
- **Math Overflow Prevention**: In languages natively restricting 32-bit integers (unlike Python which handles arbitrary limits natively), always strictly enforce boundary checking bounds mathematically testing `result > MAX_INT / 10` before appending parameters mathematically.

---

## 📚 Problem Breakdowns

### 1. Rotate Image
- **Intuition**: To rotate an image 90 degrees structurally in-place mapping bounds identically without allocating a dummy matrix, map the physical four corners. Identify exactly `left`, `right`, `top`, `bottom`. Isolate specifically the `top_left` explicitly mathematically natively. Then mathematically shift the entire sequence: Bottom-Left moves to Top-Left -> Bottom-Right moves to Bottom-Left -> Top-Right moves to Bottom-Right -> The saved Top-Left specifically moves to Top-Right. Conceptually cleanly mapping a 4-way cyclical variable swap limits checking loops.
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(1)` completely natively in-place
- **Pseudocode**:
  ```python
  l, r = 0, len(matrix) - 1
  while l < r:
      for i in range(r - l):
          top, bottom = l, r
          topLeft = matrix[top][l + i]
          
          # Move bottom-left natively to top-left
          matrix[top][l + i] = matrix[bottom - i][l]
          # Move bottom-right natively to bottom-left
          matrix[bottom - i][l] = matrix[bottom][r - i]
          # Move top-right natively to bottom-right
          matrix[bottom][r - i] = matrix[top + i][r]
          # Move sequentially saved natively top-left into top-right explicitly
          matrix[top + i][r] = topLeft
      r -= 1; l += 1
  ```

### 2. Spiral Matrix
- **Intuition**: Simulating mathematical movement structurally mapping a strict sequence explicit boundary: Right -> Down -> Left -> Up. Maintain 4 exact boundary pointers: `left`, `right`, `top`, `bottom`. Mathematically loop adding values sequentially explicitly across the `top` row boundary conceptually natively, then structurally increment `top += 1` purely so we functionally never touch it natively again exactly. Repeat sequentially structurally checking the nested bounds entirely looping identically.
- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(1)` (excluding the output array list limits)
- **Pseudocode**:
  ```python
  left, right = 0, len(matrix[0])
  top, bottom = 0, len(matrix)
  res = []
  while left < right and top < bottom:
      for i in range(left, right): res.append(matrix[top][i])
      top += 1
      for i in range(top, bottom): res.append(matrix[i][right - 1])
      right -= 1
      if not (left < right and top < bottom): break
      for i in range(right - 1, left - 1, -1): res.append(matrix[bottom - 1][i])
      bottom -= 1
      for i in range(bottom - 1, top - 1, -1): res.append(matrix[i][left])
      left += 1
  return res
  ```

### 3. Pow(x, n)
- **Intuition**: Linearly explicitly mapping `x * x * x...` for `N` explicitly identically inherently causes a `Time Limit Exceeded` specifically for massive values of `N`. We mathematically conceptually identically optimize bounds using **Divide and Conquer**. Mathematically: `x^n` is identically exactly logically `(x^(n/2))^2`. If `n` mathematically natively is exactly explicitly Even, perfectly map tracking `half * half`. If `n` conceptually inherently maps strictly Odd natively, mathematically return conceptually `half * half * x` checking properties bounds explicitly natively wrapping parameters logically testing tracking loops.
- **Time Complexity**: `O(log N)` dynamically mathematically checking limits
- **Space Complexity**: `O(log N)` recursively call stack parameters mapping
- **Pseudocode**:
  ```python
  def helper(x, n):
      if x == 0: return 0
      if n == 0: return 1
      
      res = helper(x, n // 2)
      res = res * res
      
      return x * res if n % 2 else res
  
  res = helper(x, abs(n))
  return res if n >= 0 else 1 / res
  ```

### 4. Multiply Strings
- **Intuition**: Mathematically structurally simulating native 5th-grade integer multiplication explicitly tracking limits bounds exactly arrays checking digits identically mapped. You functionally loop the exact arrays identically nested backwards tracing arrays checking exactly evaluating variables explicitly mapping boundaries testing `digit = int(num1[i]) * int(num2[j])`. You functionally trace checking variables `i+j` and `i+j+1` mapping explicitly the structural `carry` arrays limits explicitly conceptually array natively mapping values evaluating limits.
- **Time Complexity**: `O(M * N)`
- **Space Complexity**: `O(M + N)` limits explicit array bounds checking variables
- **Pseudocode**:
  ```python
  if "0" in [num1, num2]: return "0"
  res = [0] * (len(num1) + len(num2))
  num1, num2 = num1[::-1], num2[::-1]
  
  for i1 in range(len(num1)):
      for i2 in range(len(num2)):
          digit = int(num1[i1]) * int(num2[i2])
          res[i1 + i2] += digit
          
          # Carry mathematically tracking
          res[i1 + i2 + 1] += (res[i1 + i2] // 10)
          res[i1 + i2] = res[i1 + i2] % 10
          
  res, beg = res[::-1], 0
  while beg < len(res) and res[beg] == 0: beg += 1
  return "".join(map(str, res[beg:]))
  ```
