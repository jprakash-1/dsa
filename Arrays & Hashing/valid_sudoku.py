"""
Problem: Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""
import collections

def isValidSudoku(board):
    # A Sudoku board has 9 rows, 9 columns, and 9 isolated 3x3 sub-boxes.
    # We need to firmly ensure that digits 1-9 don't repeat in any of these 3 specific areas.
    # We use Hash Sets for O(1) instant checking to see if we've seen a number before!
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    # The creative trick: We uniquely identify each 3x3 box by integer dividing its coordinates: (r/3, c/3)
    squares = collections.defaultdict(set)  

    for r in range(9):
        for c in range(9):
            # If the current cell is empty (indicated by a '.'), there is nothing to validate. Skip it.
            if board[r][c] == ".":
                continue
                
            # Check if this exact number has *already* been seen in this specific row, column, or 3x3 box.
            # If so, the board is mathematically invalid immediately!
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            
            # Since we haven't seen it yet, we safely record the number as "seen" in our 3 tracking sets.
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
            
    # If we sequentially loop through the entire board without finding any repeats, it's valid!
    return True

if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"Input: board is provided in code")
    print(f"Output: {isValidSudoku(board)}")
