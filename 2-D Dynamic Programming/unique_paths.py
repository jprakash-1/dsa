"""
Problem: Unique Paths
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28
"""

def uniquePaths(m, n):
    # This array represents the BOTTOM-MOST row of our grid.
    # Why all 1s? Because from any point along the very bottom row, 
    # there is exactly ONE way to reach the bottom-right corner (just keep going right!).
    row = [1] * n
    
    # We work our way UPWARDS from the second-to-last row, up to the very top row (m-1 times).
    for _ in range(m - 1):
        # We start building the new row directly above the current one.
        # The right-most cell is always 1, because you can only go down from there.
        newRow = [1] * n
        
        # We work our way LEFTWARDS, starting from the second-to-last column.
        for j in range(n - 2, -1, -1):
            # The number of unique paths from the CURRENT square is the sum of:
            # 1. Paths from the square to the RIGHT (newRow[j + 1])
            # 2. Paths from the square directly BELOW (row[j])
            newRow[j] = newRow[j + 1] + row[j]
            
        # The row we just built becomes the "row below" for the next iteration going up.
        row = newRow
        
    # After we reach the very top row, the first element (index 0) represents the
    # top-left corner (our starting point), holding the total number of unique paths!
    return row[0]

if __name__ == "__main__":
    m = 3
    n = 7
    print(f"Input: m = {m}, n = {n}")
    print(f"Output: {uniquePaths(m, n)}")
