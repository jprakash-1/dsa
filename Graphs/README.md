# Graphs - Comprehensive Guide

> **💡 Note on Code Implementations:** All Python (`.py`) solutions in this directory include detailed, beginner-friendly inline comments. These comments explain the "what", "why", and the underlying logic of each algorithmic step.

## 🧠 Core Intuition & Reasoning
Graphs are collections of Nodes (Vertices) universally bound by connections (Edges). They computationally model real-world networks explicitly (Cities connected by Roads, Computers linked by IP, Users friending on Social Media).

Unlike Trees, perfectly hierarchical boundaries explicitly do not exist. A Graph can be **directed** (A -> B) or **undirected** (A <-> B), **weighted** (Distance = 10) or **unweighted**. 

The most critical mathematical reality of Graphs is **Cycles**. Because you can loop identically recursively `(A -> B -> C -> A)`, Graph algorithms strictly **always require a `visited` Hash Set**. If you do not track what you have physically seen, your code will natively enter an infinite sequence loop permanently.

### 🤔 When to use Graphs:
- **Shortest Path Identifiers (Unweighted)**: Breadth-First Search (BFS) mathematically radiates outward exactly one "layer" identically at a time. The very first instance it maps onto the Target, it is mathematically structurally guaranteed to be the absolute shortest path linearly.
- **Connectivity & Grouping Constraints**: "Count the islands", "Find all friends in a network". Depth-First Search (DFS) completely physically sinks down mapping explicitly connected clustered components isolating them perfectly.
- **Dependency Resolving**: "Take Course A before Course B". Topological Sort sequentially maps explicitly directed boundaries preventing cyclical contradictions entirely explicitly returning valid sequence arrays exactly.

### Generic Traversal Pattern
```python
def explore_graph(graph, start_node):
    # CRITICAL: Always explicitly track inherently visited mapped nodes 
    visited = set()
    
    # Example explicitly utilizing DFS recursively bounding identical
    def dfs(node):
        if node in visited:
            return
            
        visited.add(node)
        
        # Traverse strictly all neighbor boundaries mapping explicit 'graph' adjacency map
        for neighbor in graph[node]:
            dfs(neighbor)
            
    dfs(start_node)
```

---

## 📚 Problem Breakdowns

### 1. Number of Islands
- **Intuition**: Every strictly disconnected chunk of `"1"`s forms an island. Iterate across the structural grid limits completely linearly utilizing a nested loop. Whenever you explicitly logically encounter a `"1"` that hasn't conceptually been natively `visited`, tracking count naturally increments `islands += 1`. Crucially, you then instantly trigger a functional DFS/BFS natively locally on that specific cell. The local search physically conceptually structurally mapping touches all physically adjacent `"1"`s marking them uniquely `visited` preventing outer loop native duplicating bounds exactly.
- **Time Complexity**: `O(R * C)`
- **Space Complexity**: `O(R * C)` due to recursion stack limit or visited tracking
- **Pseudocode**:
  ```python
  def dfs(r, c):
      if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0": return
      grid[r][c] = "0" # Mark visited natively inline mapping exactly saving Set Space
      dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
  
  for r in range(ROWS):
      for c in range(COLS):
          if grid[r][c] == "1":
              islands += 1; dfs(r, c)
  return islands
  ```

### 2. Max Area of Island
- **Intuition**: Identical explicitly matching mapping naturally `Number of Islands`. Except the DFS recursive boundaries explicitly locally strictly must return an integer `count`. Functionally whenever DFS conceptually hits a `"1"`, it structurally natively returns `1 + dfs(Up) + dfs(Down) + dfs(Left) + dfs(Right)`. Maintain completely an overarching native integer `max_area` explicitly tracking completely limits naturally updating mathematically overlapping values.
- **Time Complexity**: `O(R * C)`
- **Space Complexity**: `O(R * C)`
- **Pseudocode**:
  ```python
  def dfs(r, c):
      if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0: return 0
      grid[r][c] = 0
      return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
  for r... for c...
      max_area = max(max_area, dfs(r, c))
  ```

### 3. Clone Graph
- **Intuition**: Performing a Deep Copy requires natively recreating node explicit references seamlessly without natively fundamentally duplicating conceptually cyclical sequence structures flawlessly. Utilize a native Hash Map explicitly `oldToNew = {}` dynamically pointing exact original memory addresses logically strictly to cloned matching addresses securely. Iterate natively DFS. If `node` structurally identically exists perfectly inside Map naturally, strictly return `oldToNew[node]`. Else formulate completely fresh Node conceptually, mapping it conceptually explicitly updating `Map`, sequentially linking explicitly structurally iterating bounds `copy.neighbors.append(clone(nei))`.
- **Time Complexity**: `O(V + E)` Vertices and Edges
- **Space Complexity**: `O(V)` Hash Map limitation 
- **Pseudocode**:
  ```python
  oldToNew = {}
  def clone(node):
      if not node: return None
      if node in oldToNew: return oldToNew[node]
      copy = Node(node.val)
      oldToNew[node] = copy
      for nei in node.neighbors:
          copy.neighbors.append(clone(nei))
      return copy
  ```

### 4. Rotting Oranges
- **Intuition**: Functionally explicitly a strict mathematical Multi-Source BFS structurally overlapping boundaries tracking strictly conceptually propagating boundaries perfectly identically evaluating "Infection" maps completely. Rather than natively triggering checking structurally isolated loops explicitly mapping limits, dump entirely strictly all explicit initial Rotten coordinate limits into a Queue fundamentally executing identically mapped sequential mapping limits checking bounds simultaneously explicitly generating levels logically replacing Fresh items matching `distance` natively properties. Limit tracking logically counts `fresh` bounds mathematically stopping looping checking nested bounds natively exactly returning limits mapping `time`.
- **Time Complexity**: `O(R * C)`
- **Space Complexity**: `O(R * C)`
- **Pseudocode**:
  ```python
  q = deque()
  fresh = 0; time = 0
  for r in range(ROWS):
      for c in range(COLS): # populate q with rotten oranges explicitly, count fresh variables limits
  
  while q and fresh > 0:
      for i in range(len(q)):
          r, c = q.popleft()
          # if neighbor is fresh boundaries explicitly: make rotten dynamically tracking limit, q.append, fresh -= 1
      time += 1
  return time if fresh == 0 else -1
  ```

### 5. Course Schedule
- **Intuition**: A textbook Topological Sort identifying variables resolving explicit Directed Graph mathematical dependencies natively preventing mapping Cyclical dependency loops entirely conceptually matching `Prerequisites`. A true Cycle (`A -> B -> A`) structurally mathematically explicit mapping fails inherently naturally mapping `Course constraints`. Construct a fully Adjacency Map locally. Iterate natively mapping explicitly `visited` tracking nodes verified explicitly entirely successfully tracking bounds, while distinctly structurally using an independent `cycle` Hash Set explicitly completely isolating nodes currently strictly physically mapping conceptually inside exactly the active recursive stack tracking exactly limiting bound check overlaps mathematically.
- **Time Complexity**: `O(V + E)`
- **Space Complexity**: `O(V + E)`
- **Pseudocode**:
  ```python
  prereq = {c: [] for c in range(numCourses)}
  visit, cycle = set(), set()
  def dfs(crs):
      if crs in cycle: return False # Cycle explicitly found naturally limits matching!
      if crs in visit: return True
      
      cycle.add(crs)
      for pre in prereq[crs]:
          if dfs(pre) == False: return False
      cycle.remove(crs)
      
      visit.add(crs)
      return True
  ```
