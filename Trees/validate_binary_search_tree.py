"""
Problem: Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

Example 1:
Input: root = [2,1,3]
Output: true
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    # Helper function that recursively checks if a node is within valid boundaries.
    def valid(node, left, right):
        # An empty node is technically a valid BST.
        if not node:
            return True
            
        # If the node's value violates the strict min/max boundaries, it is invalid!
        if not (left < node.val < right):
            return False
            
        # Recursively validate both children.
        # When going Left, the current node's value becomes the new strict MAXIMUM boundary.
        # When going Right, the current node's value becomes the new strict MINIMUM boundary.
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
    # Start the check with the root node.
    # Initially, it can be any possible value from negative infinity to positive infinity.
    return valid(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print("Input: [2,1,3]")
    print(f"Output: {isValidBST(root)}")
