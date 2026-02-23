"""
Problem: Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root):
    # We use a Depth First Search (DFS) helper function.
    # 'maxVal' keeps track of the maximum value we've seen on this specific path from the root.
    def dfs(node, maxVal):
        if not node:
            return 0
            
        # Is this node a "good" node?
        # Yes, if its value is >= the largest value we've seen on the way down.
        res = 1 if node.val >= maxVal else 0
        
        # Update our max value threshold for the children.
        maxVal = max(maxVal, node.val)
        
        # Recursively search the left and right subtrees, passing the maxVal down.
        res += dfs(node.left, maxVal)
        res += dfs(node.right, maxVal)
        
        return res
        
    # Start the DFS traversal.
    # The root node's initial path maximum is simply its own value.
    return dfs(root, root.val) if root else 0

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    print("Input: [3,1,4,3,null,1,5]")
    print(f"Output: {goodNodes(root)}")
