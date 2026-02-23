# Linked List - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
Linked Lists dynamically allocate memory for nodes, physically chaining them conceptually across scattered RAM locations natively through explicit `node.next` pointers. You do not have random `O(1)` access like an Array natively. Navigating requires manually mathematically shifting your pointers strictly linearly `node = node.next`. 

A massive amount of Linked List challenges computationally revolve strictly around conceptually tracking explicit pointers, structurally swapping reference targets, or reversing sequences completely natively without fundamentally snapping the physical chain explicitly stranding the rest of the list.

### 🤔 Essential Tactics & When to use:
- **Dummy Node**: An empty explicitly generated Node artificially pinned directly before the true `head`. It fundamentally removes Edge-Case bugs tracking bounds (like deleting the first node or inserting a new head locally). Instead of explicitly manually returning the shifted `head` dynamically, return `dummy.next` seamlessly.
- **Fast & Slow Pointers (Floyd's Tortoise and Hare)**: When you logically mathematically need exactly the exact middle of the list bounds, tracking an explicit `slow` pointer stepping 1 sequence mathematically identically alongside a `fast` pointer stepping exactly 2 sequences implicitly leaves `slow` strictly in the middle when `fast` natively hits the end bounds. Extremely heavily relied upon functionally checking Cycles natively.
- **Multi-Pointer Reversals**: A sequence mapping mathematically requiring variables capturing state `prev`, `curr`, and `nxt` strictly natively tracking the list safely so `curr.next` logically bounds explicitly reversed tracking bounds natively without dynamically losing evaluating limits natively.

### Generic Reversal Pattern
```python
def reverseList(head):
    # Setup pointers structurally tracking
    prev, curr = None, head
    
    while curr:
        nxt = curr.next    # 1. Temporarily save the rest of the unreversed list explicitly
        curr.next = prev   # 2. Re-point structurally backward isolating target natively
        
        # Shift execution limits mapping bounds structurally forward
        prev = curr        # 3. Old 'curr' mapping becomes the new 'prev' structurally
        curr = nxt         # 4. Old 'nxt' dynamically limiting bounds becomes new 'curr'
        
    return prev # 'prev' conceptually mathematically maps the natively new head explicitly
```

---

## 📚 Problem Breakdowns

### 1. Reorder List
- **Intuition**: Conceptually physically cutting the list sequence dynamically in exactly half locally, reversing strictly the second structurally split sequence identically, and natively cleanly merging explicit nodes structurally alternatingly limits mapping `[first, last, second, second_last]`. Method: 1) Fast & Slow explicit mapping isolates exact middle. 2) Safely Reverse naturally the right structurally bounded sequence perfectly natively. 3) Two pointers explicitly cleanly merging explicitly weaving identically mapped Nodes physically limiting loops.
- **Time Complexity**: `O(N)` logically tracking mappings entirely
- **Space Complexity**: `O(1)` mapping perfectly in-place explicit edits.
- **Pseudocode**:
  ```python
  # 1. Find middle explicit coordinates dynamically limits naturally
  slow, fast = head, head.next
  while fast and fast.next: slow = slow.next; fast = fast.next.next
  # 2. Reverse explicitly second structurally half identical bounds
  second = slow.next; prev = slow.next = None
  while second: tmp = second.next; second.next = prev; prev = second; second = tmp
  # 3. Merge natively mappings identically perfectly explicitly
  first, second = head, prev
  while second:
      tmp1, tmp2 = first.next, second.next
      first.next = second; second.next = tmp1
      first, second = tmp1, tmp2
  ```

### 2. Remove Nth Node From End of List
- **Intuition**: Natively evaluating explicitly mathematically traversing identical boundaries tracking `N` nodes entirely without specifically checking limits traversing explicit lists twice natively limiting variables bounds. Offset specifically a dynamically created `right` mathematically pointer precisely `N` explicit nodes perfectly ahead explicitly natively tracking structural bounds. Then structurally advance mathematically tracking limits `left` explicitly overlapping identically tracing tracking limits dynamically until completely `right` hits the explicitly bound edge, inherently snapping exactly `left` physically limiting explicitly bounds correctly. Use Dummy mathematically tracking avoiding explicitly checks avoiding `head` precisely overlapping deletions.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
- **Pseudocode**:
  ```python
  dummy = ListNode(0, head)
  left, right = dummy, head
  for _ in range(n): right = right.next
  while right: left, right = left.next, right.next
  # Left explicitly limits bounds mathematically isolating deletion natively
  left.next = left.next.next
  return dummy.next
  ```

### 3. Copy List with Random Pointer
- **Intuition**: Deep cloning explicitly structurally explicitly copying `val`, `next`, dynamically identifying exactly evaluating limits checking `random`. Structurally tracking precisely mathematically identical bounds generating checking explicit mapping Native HashMap perfectly copying structurally evaluating entirely limits logically isolating limits perfectly checking identical limits bounding exactly mapping tracking `oldToCopy[Old Node] = Copy Node`. Two passes perfectly logically limiting. Pass 1 dynamically generates structural identical nodes, Pass 2 explicitly naturally connects logically checking bounds exactly mappings.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)` limits HashMap strictly
- **Pseudocode**:
  ```python
  oldToCopy = {None: None}
  curr = head
  while curr: oldToCopy[curr] = Node(curr.val); curr = curr.next
  curr = head
  while curr:
      copy = oldToCopy[curr]
      copy.next = oldToCopy[curr.next]
      copy.random = oldToCopy[curr.random]
      curr = curr.next
  return oldToCopy[head]
  ```

### 4. Add Two Numbers
- **Intuition**: Functionally naturally mathematically identical tracking dynamically natively evaluating explicitly structural grade-school structurally identical integer array addition sequence limits perfectly checking natively limits mathematically. Keep identically tracking exact pointers tracking `l1` and `l2` tracking mathematically `carry = sum // 10`. Append exactly limits mathematically inherently exactly mapping checking limits matching explicit structurally matching identical nested naturally returning parameters dummy.
- **Time Complexity**: `O(max(N, M))`
- **Space Complexity**: `O(max(N, M))` natively mapping identical list limits
- **Pseudocode**:
  ```python
  dummy = ListNode(); curr = dummy
  carry = 0
  while l1 or l2 or carry:
      v1 = l1.val if l1 else 0
      v2 = l2.val if l2 else 0
      val = v1 + v2 + carry
      carry = val // 10
      curr.next = ListNode(val % 10); curr = curr.next
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
  return dummy.next
  ```

### 5. Find the Duplicate Number
- **Intuition**: Tricky bounds explicitly parsing array values implicitly mapped conceptually natively mirroring pointers testing array explicitly tracking structurally mapped values. integers range perfectly natively `[1, n]`. Identical values natively overlapping fundamentally identically creates physically conceptually mapped identical natively mapping bounds generating explicit evaluating bounds natively. Floyd's Algorithm logically tracks explicit variables mapping exactly `slow` implicitly tracking `fast`. 
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)` entirely mapping natively values tracking implicit
- **Pseudocode**:
  ```python
  slow, fast = 0, 0
  while True:
      slow = nums[slow]
      fast = nums[nums[fast]]
      if slow == fast: break # Cycle detected perfectly
  slow2 = 0
  while True:
      slow = nums[slow]
      slow2 = nums[slow2]
      if slow == slow2: return slow # Path entrance exactly structurally limits
  ```

### 6. LRU Cache
- **Intuition**: Access operations physically `O(1)` checking parameters limit exactly bounds limits structurally mapping array tracking Hashmap. Array bounds tracking sequence checking Hashmap structural pointers evaluating entirely variables mapping Doubly Linked List natively caching structural. Tracking pointer explicitly tracking explicitly variables checking bounds. Functionally mapping `Left` exactly evaluating variables mapping checking tracking tracking limits structurally mapping explicitly limiting `Right` perfectly bounds limit entirely wrapping variables limits. Hashmap `key: node` prevents parameters scanning entirely tracking testing explicit tracking limits.
- **Time Complexity**: `O(1)` bounds checking explicitly tracking values mapping completely structurally 
- **Space Complexity**: `O(Capacity)` natively evaluating identical bounds mapping tracking parameters Limits.
- **Pseudocode**:
  ```python
  # Setup Double Node explicitly tracking exactly parameter variables tracking Limit Dummy Left, Double Dummy Right.
  def remove(self, node): node.prev.next = node.next; node.next.prev = node.prev
  def insert(self, node): prev = self.right.prev; prev.next = node; node.prev = prev; node.next = self.right; self.right.prev = node
  def get(self, key): if key in self.cache: remove(); insert(); return val
  def put(self, key, value): if key in cache: remove(); insert(); if over cap: remove Left.next; pop explicitly.
  ```
