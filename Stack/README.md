# Stack - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
A Stack operates tightly on a **LIFO (Last-In, First-Out)** principle via array `append()` (push) and `pop()` operations. 

In algorithms, Stacks are the ultimate tool for **"remembering deferred tasks"** or **"saving state."** If you are processing elements linearly but encounter something that forces you to pause evaluating the *current* element until some *future* condition is met, a Stack safely holds the paused elements in chronological order. When the future condition is finally satisfied, you pop backward, resolving the most recently deferred task first.

This LIFO nature makes Stacks the iterative equivalent of Recursion (the runtime Call Stack).

### 🤔 When to use Stacks:
- **Pair Matching**: Parentheses validation, HTML tag validation. Whenever a closing symbol explicitly must match the most recently opened symbol.
- **String Parsing/Evaluation**: Evaluating Reverse Polish Notation, calculating mathematical string expressions (`"3 + (2 * 4)"`), or simulating directory standardizations (`"../dir/./"`).
- **Monotonic Sequence Queries**: "Find the Next Greater Element", "Find the Next Warmer Day." When you need to resolve limits on elements based solely on upcoming data peaks or valleys.

### 📈 Monotonic Stack Pattern
A crucial advanced use case. A Monotonic Stack strictly guarantees its elements are always sorted (e.g., strictly decreasing). If a new element arrives that breaks the sorted rule, you `pop()` the smaller elements out of the stack *until* the rule holds again. The act of popping represents discovering the "Next Greater Element" for those popped values.

```python
def monotonic_decreasing_stack(arr):
    stack = [] # Stores (value, original_index)
    res = [-1] * len(arr)
    
    for i, curr_val in enumerate(arr):
        # While current value breaks the decreasing rule (it is BIGGER than the top of stack)
        while stack and stack[-1].val < curr_val:
            # We found the "next greater element" for the item at the top of the stack!
            popped_item = stack.pop()
            res[popped_item.index] = curr_val
            
        # Push current element to wait for its own next greater element
        stack.append((curr_val, i)) 
        
    return res
```

---

## 📚 Problem Breakdowns

### 1. Min Stack
- **Intuition**: Pushing and popping natively run in `O(1)`. But returning the `getMin()` in `O(1)` normally requires searching. The trick is recognizing that the "minimum" state maps perfectly directly onto the stack state. We maintain alongside our main stack a secondary stack (`minStack`). Every time we push a value `x`, the `minStack` pushes `min(x, minStack[-1])`. As elements are popped, the `minStack` perfectly unwinds its historical minimums inline.
- **Time Complexity**: `O(1)` for all operations
- **Space Complexity**: `O(N)`
- **Pseudocode**:
  ```python
  def push(self, val):
      self.stack.append(val)
      val = min(val, self.minStack[-1] if self.minStack else val)
      self.minStack.append(val)
      
  def pop(self):
      self.stack.pop(); self.minStack.pop()
  ```

### 2. Evaluate Reverse Polish Notation (RPN)
- **Intuition**: Postfix notation implicitly removes the need for parentheses because operator precedence is defined by linear order. If the token is a number, we don't know what to do with it yet, so we "save" it on the Stack. If the token is an operator `(+, -, *, /)`, it mathematically applies to the two most recently saved numbers. We pop `b`, pop `a`, evaluate `a [operator] b`, and push the new result back to be used later.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Pseudocode**:
  ```python
  stack = []
  for t in tokens:
      if t == '+': stack.append(stack.pop() + stack.pop())
      # Watch out for subtraction and division order: a - b, a / b
      elif t == '-': a, b = stack.pop(), stack.pop(); stack.append(b - a)
      elif t == '*': stack.append(stack.pop() * stack.pop())
      elif t == '/': a, b = stack.pop(), stack.pop(); stack.append(int(b / a))
      else: stack.append(int(t))
  return stack[0]
  ```

### 3. Generate Parentheses
- **Intuition**: We need all well-formed combinations of `n` pairs. This requires exploring branched decisions, making Backtracking perfectly suited. A global stack string conceptually tracks our ongoing combination. The math logic constraints: 1) We can safely add an open parenthesis `(` if `open < n`. 2) We can cleanly safely add a closed parenthesis `)` ONLY if `closed < open`.
- **Time Complexity**: `O(4^n / sqrt(n))` (Catalan Number computation branch bounds)
- **Space Complexity**: `O(N)` call stack memory limiting depth to `2*N`
- **Pseudocode**:
  ```python
  def backtrack(openN, closedN):
      if openN == closedN == n: res.append("".join(stack)); return
      if openN < n:
          stack.append("(")
          backtrack(openN + 1, closedN)
          stack.pop()
      if closedN < openN:
          stack.append(")")
          backtrack(openN, closedN + 1)
          stack.pop()
  backtrack(0, 0)
  ```

### 4. Daily Temperatures
- **Intuition**: We want the "Next Warmer Day". This requires tracking historical cooler days until a warm day arises. We use a **Monotonic Decreasing Stack**, holding pairs of `[temperature, index]`. For every new day, if its temp is hotter than the top of our stack, we have successfully found the answer for that older day! Pop it off, compute the index limits `duration = current_i - popped_i`, and continue checking deeper down the stack iteratively.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Pseudocode**:
  ```python
  res = [0] * len(temperatures)
  stack = [] # pair: [temp, index]
  for i, t in enumerate(temperatures):
      while stack and t > stack[-1][0]:
          stackT, stackI = stack.pop()
          res[stackI] = i - stackI
      stack.append([t, i])
  return res
  ```

### 5. Car Fleet
- **Intuition**: Math defines arrival time conceptually as `(target - position) / speed`. If a car starting further behind physically finishes in faster or explicitly identical time as the car directly ahead of it, it collides into a Fleet exactly bottlenecked precisely by the slower car ahead. We sort cars descending by position (closest to target first). We push arrival times to a Stack. If `stack[-1]` (car behind) `<= stack[-2]` (car in front), they collide, so we pop the faster car entirely, effectively merging them.
- **Time Complexity**: `O(N log N)` due to sorting 
- **Space Complexity**: `O(N)`
- **Pseudocode**:
  ```python
  pair = [[p, s] for p, s in zip(position, speed)]
  stack = []
  for p, s in sorted(pair)[::-1]: # Reverse Sorted
      stack.append((target - p) / s)
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
          stack.pop()
  return len(stack)
  ```
