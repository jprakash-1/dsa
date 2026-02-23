"""
Problem: Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    res = []
    # Use a double-ended queue (deque) for O(1) pops from the left.
    q = collections.deque()
    if root:
        q.append(root)
        
    # Standard Breadth-First Search (BFS) template.
    while q:
        # 'val' stores the node values for the current level.
        val = []
        # Loop strictly through the nodes currently in the queue (one exact level).
        for i in range(len(q)):
            node = q.popleft()
            val.append(node.val)
            
            # Add the children of the current node to the queue for the NEXT level.
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        # Append the completed level to our final result list.
        res.append(val)
        
    return res

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(f"Input: [3,9,20,null,null,15,7]")
    print(f"Output: {levelOrder(root)}")
