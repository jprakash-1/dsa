"""
Problem: Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

def rotate(matrix):
    # We will rotate the matrix layer by layer (like peeling an onion),
    # starting from the outermost boundary and moving inwards.
    l, r = 0, len(matrix) - 1
    
    while l < r:
        # In the current layer, we need to perform (r - l) individual 4-way swaps.
        for i in range(r - l):
            top, bottom = l, r
            
            # Save the top-left element in a temporary variable before we overwrite it.
            # (Note how 'i' helps us slide along the edge during the loop)
            topLeft = matrix[top][l + i]
            
            # Step 1: Move bottom-left element into the top-left position
            matrix[top][l + i] = matrix[bottom - i][l]
            
            # Step 2: Move bottom-right element into the bottom-left position
            matrix[bottom - i][l] = matrix[bottom][r - i]
            
            # Step 3: Move top-right element into the bottom-right position
            matrix[bottom][r - i] = matrix[top + i][r]
            
            # Step 4: Move the original top-left (saved earlier) into the top-right position
            matrix[top + i][r] = topLeft
            
        # We finished the entire outer layer! Shrink the boundaries inwards.
        r -= 1
        l += 1

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Input: matrix = {matrix}")
    rotate(matrix)
    print(f"Output: {matrix}")
