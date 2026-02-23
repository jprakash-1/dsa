"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    cur = root
    
    # We leverage the main property of a Binary Search Tree:
    # Left descendants are smaller, Right descendants are larger!
    while cur:
        # If BOTH p and q are strictly GREATER than the current node...
        # Their Lowest Common Ancestor must conceptually be in the Right subtree.
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        # If BOTH p and q are strictly LESS than the current node...
        # Their Lowest Common Ancestor must conceptually be in the Left subtree.
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        # If one is greater and one is less (or one equals the current node)...
        # We have cleanly found the split point! The current node IS the Lowest Common Ancestor.
        else:
            return cur

if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    p = root.left
    q = root.right
    print(f"Input: root = [6,2,8], p = 2, q = 8")
    res = lowestCommonAncestor(root, p, q)
    print(f"Output: {res.val}")
