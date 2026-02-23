"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    # Base Case: If either list is empty, there is no tree to build.
    if not preorder or not inorder:
        return None
        
    # The first element in a PREORDER traversal is always the root node!
    root = TreeNode(preorder[0])
    
    # Find where this root is in the INORDER traversal.
    # Everything to the left of 'mid' is in the left subtree.
    # Everything to the right of 'mid' is in the right subtree.
    mid = inorder.index(preorder[0])
    
    # Recursively build the left subtree.
    # Preorder needs to skip the 1st element (root) and take exactly 'mid' elements.
    root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])
    
    # Recursively build the right subtree.
    # Take everything after the left subtree's elements.
    root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
    
    return root

def printLevelOrder(root):
    import collections
    res = []
    q = collections.deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res

if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(f"Input: preorder = {preorder}, inorder = {inorder}")
    root = buildTree(preorder, inorder)
    print(f"Output: {printLevelOrder(root)}")
