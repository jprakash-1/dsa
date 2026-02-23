"""
Problem: Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

def numIslands(grid):
    # Edge case: Empty grid means 0 islands.
    if not grid:
        return 0

    ROWS, COLS = len(grid), len(grid[0])
    visit = set() # Keeps track of land cells we've already counted
    islands = 0

    # Depth-First Search (DFS) to explore all connected land of a single island
    def dfs(r, c):
        # Base Case / Stop Condition: 
        # 1. Out of grid boundaries
        # 2. It's water ("0")
        # 3. We've already visited this piece of land
        if (r not in range(ROWS) or 
            c not in range(COLS) or 
            grid[r][c] == "0" or 
            (r, c) in visit):
            return
            
        # Mark this specific land cell as visited
        visit.add((r, c))
        
        # Now, recursively explore all 4 adjacent directions (Down, Up, Right, Left)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # Main Loop: Scan through every single cell in the grid
    for r in range(ROWS):
        for c in range(COLS):
            # If we find UNVISITED land ("1"), it MUST be a brand new island!
            if grid[r][c] == "1" and (r, c) not in visit:
                islands += 1 # Count the new island
                # Trigger DFS to find and mark ALL connected land for this new island
                dfs(r, c)
                
    return islands

if __name__ == "__main__":
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print(f"Input: grid = {grid}")
    print(f"Output: {numIslands(grid)}")
