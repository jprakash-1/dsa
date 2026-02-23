"""
Problem: Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""

def spiralOrder(matrix):
    res = []
    
    # Set up our four dynamic boundaries that will slowly close inward like a shrinking box.
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    
    # Keep spiraling as long as our boundaries haven't collapsed onto each other.
    while left < right and top < bottom:
        # Step 1: Traverse from left to right along the TOP boundary row
        for i in range(left, right):
            res.append(matrix[top][i])
        # We finished the top row, so shift the top boundary DOWN.
        top += 1
        
        # Step 2: Traverse from top to bottom along the RIGHT boundary column
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        # We finished the right column, so shift the right boundary LEFT.
        right -= 1
        
        # CRITICAL CHECK: Before doing the bottom and left paths, ensure 
        # our boundaries haven't already crossed! (This happens in non-square matrices).
        if not (left < right and top < bottom):
            break
            
        # Step 3: Traverse from right to left along the BOTTOM boundary row
        # (Note the step of -1 to go backwards)
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        # We finished the bottom row, so shift the bottom boundary UP.
        bottom -= 1
        
        # Step 4: Traverse from bottom to top along the LEFT boundary column
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        # We finished the left column, so shift the left boundary RIGHT.
        left += 1
        
    return res

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Input: matrix = {matrix}")
    print(f"Output: {spiralOrder(matrix)}")
