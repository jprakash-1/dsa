"""
Problem: Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical).
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0]]
Output: 6
"""

def maxAreaOfIsland(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set() # To ensure we don't count the same piece of land twice

    # DFS function to calculate the area of a single connected island
    def dfs(r, c):
        # Base Case: Stop and return area 0 if:
        # 1. We step out of the grid boundaries
        # 2. We step into water (0)
        # 3. We revisit a piece of land we've already counted
        if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
            grid[r][c] == 0 or (r, c) in visit):
            return 0
            
        # Mark current land cell as visited
        visit.add((r, c))
        
        # The area is 1 (for the current cell) PLUS the area of any connected land
        # in all 4 directions (Down, Up, Right, Left)
        return (1 + dfs(r + 1, c) + dfs(r - 1, c) + 
                    dfs(r, c + 1) + dfs(r, c - 1))

    area = 0
    # Iterate through every cell in the matrix
    for r in range(ROWS):
        for c in range(COLS):
            # When we hit an unvisited piece of land, we run DFS to find its total size
            if grid[r][c] == 1 and (r, c) not in visit:
                # Update our max area if this newly found island is bigger
                area = max(area, dfs(r, c))
                
    return area

if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0]]
    print(f"Input: grid = {grid}")
    print(f"Output: {maxAreaOfIsland(grid)}")
