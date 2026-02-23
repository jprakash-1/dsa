# Tries (Prefix Trees) - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
A Trie (pronounced "try", stemming from re**trie**val) is fundamentally an N-ary Tree uniquely optimized for storing and retrieving strings. 

Instead of storing an entire string inside a single node (like a standard Binary Search Tree might do), a Trie distributes a string character-by-character along a vertical path. The root is completely empty. Its children represent the first letters of all stored words. Their children represent the second letters, and so on.

This overlapping structure makes it incredibly space-time efficient for **Prefixes**. If you store `"apple"` and `"app"`, they share the exact same structural nodes `a -> p -> p`. The only difference is a boolean flag `is_end_of_word` marked on the second `p` and the `e`.

### 🤔 When to use Tries:
- **Auto-Complete & Dictionary Generation**: Any feature typing characters sequentially expecting a localized predictive dropdown menu.
- **Prefix Matching `startswith()`**: Standard Hash Sets check if exactly `"apple"` exists in `O(1)`. But checking if *any* word starts with `"app-"` using a Hash Set requires explicit string manipulation. A Trie does both full-word mapping and prefix checking natively in `O(L)` time (where L is the length of the string).
- **Matrix String Validations**: Advanced problems like *Word Search II*, where you are exploring a grid of characters and need to instantly know if your current path is a valid prefix before bothering to continue exploring.

### Generic Node Structure Pattern
```python
class TrieNode:
    def __init__(self):
        # A dictionary mapping explicit Characters to their respective child TrieNodes.
        # e.g., {'a': TrieNode1, 'b': TrieNode2}
        self.children = {} 
        
        # Crucial bounding flag indicating a full word explicitly halts at this specific node.
        self.is_end_of_word = False 
```

---

## 📚 Problem Breakdowns

### 1. Implement Trie (Prefix Tree)
- **Intuition**: Standard fundamental implementation. 
  - **Insert**: Iterate character by character sequentially. If a character is cleanly missing from the `cur.children` map, instantiate a new `TrieNode`. Move the pointer strictly down. Finally, manually explicitly flip `endOfWord = True` at the final node.
  - **Search**: Traverse vertically matching string characters mapping dynamically. If any character is missing natively, return `False`. If the loop finishes smoothly, return whether the `endOfWord` boolean is exactly `True`.
  - **StartsWith**: Identical dynamically to `Search`, except if the loop finishes successfully, return `True` unconditionally, completely ignoring the `endOfWord` flag.
- **Time Complexity**: `O(L)` for insert, search, startsWith (L = length of string)
- **Space Complexity**: `O(T)` where T is total characters across all unique branch formations.
- **Pseudocode**:
  ```python
  class Trie:
      def __init__(self): self.root = TrieNode()
      
      def insert(self, word):
          cur = self.root
          for c in word:
              if c not in cur.children: cur.children[c] = TrieNode()
              cur = cur.children[c]
          cur.endOfWord = True
  ```

### 2. Design Add and Search Words Data Structure
- **Intuition**: Identical explicitly to a basic Trie, but with replacing wildcard constraint `"."`. If we see a standard character, we safely branch down exactly `children[c]`. However, if we evaluate `"."`, it mathematically equals *any possible character*. Thus, we must iteratively recursively execute DFS branching down **all** available children currently explicitly existing on that node. If *any* branch evaluating recursively returns `True`, the entire wildcard maps successfully.
- **Time Complexity**: `O(L)` for clean insert. For search with `.`, worst-case natively `O(26^L)` exploring all sub-branches entirely.
- **Space Complexity**: `O(T)` mapping strictly.
- **Pseudocode**:
  ```python
  def search(self, word):
      def dfs(j, root):
          cur = root
          for i in range(j, len(word)):
              c = word[i]
              if c == ".":
                  # Explore all available distinct paths inherently
                  for child in cur.children.values():
                      if dfs(i + 1, child): return True
                  return False
              else:
                  if c not in cur.children: return False
                  cur = cur.children[c]
          return cur.word # Use the boolean variable limit
      return dfs(0, self.root)
  ```

### 3. Word Search II
- **Intuition**: Running standard `Word Search I` looping through an array of 10,000 words against a grid is mathematically insanely slow. Instead, heavily insert all 10,000 words strictly into a native **Trie**. Then, run DFS mapping across the grid strictly once. As you move natively cell-by-cell `r, c`, cross-reference your path directly against the Trie structure. If your grid letter sequence logically doesn't exist explicitly in the `TrieNode.children`, prune the DFS path entirely instantly avoiding massive useless loops.
- **Time Complexity**: `O(M * N * 4^L)` (where L is max length of word in Trie)
- **Space Complexity**: `O(T)` for total exact Trie Size
- **Pseudocode**:
  ```python
  # After explicitly building Trie out of 'words' array
  def dfs(r, c, node, word):
      if (r < 0 or c < 0 or r == ROWS or c == COLS or 
          (r, c) in visit or board[r][c] not in node.children):
          return
      
      visit.add((r, c))
      node = node.children[board[r][c]]
      word += board[r][c]
      if node.isWord: res.add(word)
      
      dfs(r + 1, c, node, word); dfs(r - 1, c, node, word)
      dfs(r, c + 1, node, word); dfs(r, c - 1, node, word)
      visit.remove((r, c)) # Backtrack cleanly limits
  ```
