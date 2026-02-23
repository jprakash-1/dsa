"""
Problem: Rotting Oranges
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""
import collections

def orangesRotting(grid):
    # Queue for Breadth-First Search (BFS)
    q = collections.deque()
    time, fresh = 0, 0
    ROWS, COLS = len(grid), len(grid[0])
    
    # Step 1: Initial Grid Scan
    # We need to find ALL currently rotten oranges to start our BFS from multiple sources.
    # We also count the fresh oranges so we know when we are done.
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                q.append([r, c]) # Add rotten orange coordinates to the queue
                
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    # Step 2: Multi-Source BFS
    # Continue as long as we have rotten oranges spreading AND fresh oranges left to rot.
    while q and fresh > 0:
        # We want to process all currently rotten oranges at the SAME TIME (this represents 1 minute passing)
        for i in range(len(q)):
            r, c = q.popleft()
            
            # Look at all 4 adjacent cells
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                # If adjacent cell is out of bounds or NOT a fresh orange, skip it.
                if (row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1):
                    continue
                    
                # Oh no! The fresh orange becomes rotten!
                grid[row][col] = 2
                
                # Add the newly rotten orange to the queue so it can spread next minute.
                q.append([row, col])
                fresh -= 1 # We have one less fresh orange now.
                
        # After processing all oranges for this level/minute, increment the timer.
        time += 1
        
    # Step 3: Check if we succeeded
    # If fresh == 0, all oranges rotted, return the time. Otherwise, some are unreachable, return -1.
    return time if fresh == 0 else -1

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(f"Input: grid = {grid}")
    print(f"Output: {orangesRotting(grid)}")
