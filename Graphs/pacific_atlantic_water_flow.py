"""
Problem: Pacific Atlantic Water Flow
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
"""

def pacificAtlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set() # Sets to store coordinates that can flow to Pacific / Atlantic respectively

    # DFS from the Ocean INWARDS, finding cells that are >= the previous height.
    def dfs(r, c, visit, prevHeight):
        # Base Case: Stop if out of bounds, already visited, or
        # the current cell is LOWER than the previous (water can't flow UP).
        if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
            return
            
        visit.add((r, c)) # Mark as connected to this specific ocean
        
        # Check all 4 surrounding cells
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    # 1. Run DFS starting from the Top (Pacific) and Bottom (Atlantic) rows
    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    # 2. Run DFS starting from the Left (Pacific) and Right (Atlantic) columns
    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

    res = []
    # 3. Any coordinate present in BOTH 'pac' and 'atl' sets is a valid answer!
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
                
    return res

if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print("Input: matrix provided in code")
    print(f"Output: {pacificAtlantic(heights)}")
