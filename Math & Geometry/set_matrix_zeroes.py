"""
Problem: Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

def setZeroes(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    
    # We will use the very FIRST row and FIRST column of the matrix to flag 
    # which other rows/cols need to be zeroed out. This saves space!
    # However, cell matrix[0][0] overlaps for both the first row AND first column.
    # We use matrix[0][0] to track the first COLUMN, and a separate variable for the first ROW.
    rowZero = False
    
    # Phase 1: Scan the entire matrix to mark zero rows and columns.
    for r in range(ROWS):
        for c in range(COLS):
            # If we find a zero anywhere...
            if matrix[r][c] == 0:
                # Mark its column in the first row.
                matrix[0][c] = 0
                # Mark its row in the first column (or use rowZero if it's the very first row).
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
                    
    # Phase 2: Use those marks to actually set the interior cells to zero.
    # (We skip the first row/col for now so we don't accidentally erase our tracking marks!)
    for r in range(1, ROWS):
        for c in range(1, COLS):
            # If the row's flag OR the col's flag is triggered, turn this cell to 0.
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
                
    # Phase 3: Finally, handle the first column based on matrix[0][0]
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0
            
    # Phase 4: Handle the first row based on our special 'rowZero' variable
    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0

if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(f"Input: matrix = {matrix}")
    setZeroes(matrix)
    print(f"Output: {matrix}")
