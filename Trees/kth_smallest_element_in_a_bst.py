"""
Problem: Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    # We use a stack to simulate recursion for an In-Order Traversal.
    # An In-Order Traversal on a BST visits nodes in strictly increasing sorted order!
    stack = []
    curr = root
    
    while stack or curr:
        # Go as far left as possible to find the smallest elements first.
        while curr:
            stack.append(curr)
            curr = curr.left
            
        # We process the most recently added node (the current smallest).
        curr = stack.pop()
        k -= 1
        
        # If we have popped 'k' elements, this node is our answer!
        if k == 0:
            return curr.val
            
        # After processing a node, we explore its right subtree to find larger elements.
        curr = curr.right
        
    return -1

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    k = 1
    print(f"Input: root = [3,1,4,null,2], k = 1")
    print(f"Output: {kthSmallest(root, k)}")
