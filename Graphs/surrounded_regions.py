"""
Problem: Surrounded Regions
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
"""

def solve(board):
    ROWS, COLS = len(board), len(board[0])

    # DFS to mark a region as "safe" (temporarily change 'O' to 'T')
    def capture(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
            return
        board[r][c] = "T" # 'T' stands for Temporary or Safe
        # Explore all four directions
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    # Step 1: Find all 'O's on the BORDER.
    # An 'O' on the border is not surrounded, and any 'O' connected to it is also safe.
    for r in range(ROWS):
        for c in range(COLS):
            # Check if it's on the edge of the board AND is an 'O'
            if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                capture(r, c) # Highlight/Save this region safely as 'T'

    # Step 2: Capture surrounded regions (O -> X)
    # The remaining 'O's were never connected to the border, so they are surrounded!
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"

    # Step 3: Uncapture unsurrounded regions (T -> O)
    # Restore the 'safe' border regions back to their original 'O' state.
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "T":
                board[r][c] = "O"

if __name__ == "__main__":
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    print(f"Input: board = {board}")
    solve(board)
    print(f"Output: {board}")
