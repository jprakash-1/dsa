"""
Problem: Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""

def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    # A set to keep track of the coordinates we have already visited in our current path.
    # This prevents us from using the same letter piece twice!
    path = set()
    
    # DFS Backtracking function. 
    # (r, c) = current row & col in the grid.
    # 'i' = current index of the character we are looking for in 'word'.
    def dfs(r, c, i):
        # Base Case 1 (Success): If 'i' reached the length of 'word', we logically found all characters!
        if i == len(word):
            return True
            
        # Base Case 2 (Failure): Stop exploring if:
        # 1. We step out of bounds (r or c too small or too large).
        # 2. The character on the board doesn't match the required character in the 'word'.
        # 3. We are trying to revisit a cell that is already in our current 'path'.
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
            return False
            
        # If the cell is valid and matches, add it to our path so we don't accidentally revisit it.
        path.add((r, c))
        
        # Recursively explore all 4 adjacent directions (Down, Up, Right, Left).
        # We increase 'i' by 1 because we are looking for the NEXT character in the 'word'.
        res = (dfs(r + 1, c, i + 1) or 
               dfs(r - 1, c, i + 1) or 
               dfs(r, c + 1, i + 1) or 
               dfs(r, c - 1, i + 1))
               
        # BACKTRACK: Before returning from this function call, REMOVE the current cell from our path.
        # We do this because other separate DFS paths might need to legitimately use this cell later!
        path.remove((r, c))
        return res
        
    # We don't know where the word might start, so we must try starting the DFS 
    # from EVERY single cell on the board.
    for r in range(ROWS):
        for c in range(COLS):
            # If the DFS returns True from any starting cell, the word exists!
            if dfs(r, c, 0):
                return True
                
    # If we loop through the whole board and never find it, return False.
    return False

if __name__ == "__main__":
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"
    print(f"Input: board = {board}, word = '{word}'")
    print(f"Output: {exist(board, word)}")
