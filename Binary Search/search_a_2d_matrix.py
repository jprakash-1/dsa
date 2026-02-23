"""
Problem: Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""

def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    
    # Step 1: Binary search to find the correct row
    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        
        # Target is larger than the largest element in this row
        if target > matrix[row][-1]:
            top = row + 1
        # Target is smaller than the smallest element in this row
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            # Target is within the range of this row
            break
            
    # If the target is not in any row's range
    if not (top <= bot):
        return False
        
    # Step 2: Binary search within the found row
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
            
    return False

if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(f"Input: matrix = {matrix}, target = {target}")
    print(f"Output: {searchMatrix(matrix, target)}")
