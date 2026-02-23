"""
Problem: Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
"""
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    res = []
    # Start our BFS queue with the root node.
    q = collections.deque([root])
    
    while q:
        rightSide = None
        qLen = len(q)
        
        # Traverse every node exactly on the current level.
        for i in range(qLen):
            node = q.popleft()
            if node:
                # As we go left-to-right, 'rightSide' keeps getting reliably updated.
                # When the loop finishes, it will hold the rightmost node's real value!
                rightSide = node
                
                # Enqueue children for the next level.
                q.append(node.left)
                q.append(node.right)
                
        # If we found at least one valid node on this level, safely add the rightmost one.
        if rightSide:
            res.append(rightSide.val)
            
    return res

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(f"Input: [1,2,3,null,5,null,4]")
    print(f"Output: {rightSideView(root)}")
