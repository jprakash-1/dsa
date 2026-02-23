"""
Problem: Clone Graph
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    # A hash map to map Original Node -> Cloned (Copy) Node
    # This prevents infinite loops if the graph has cycles!
    oldToNew = {}

    def dfs(node):
        # Base Case 1: We've already cloned this node before.
        # Just return the clone from our map to link it properly.
        if node in oldToNew:
            return oldToNew[node]

        # Action: Create a brand new copy of the current node (with its value).
        copy = Node(node.val)
        
        # CRITICAL STEP: Add it to our map BEFORE traversing its neighbors.
        # This prevents getting stuck in an infinite cycle!
        oldToNew[node] = copy
        
        # Recursive Step: Visit all the original node's neighbors,
        # clone them (via dfs), and add the clones to the current copy's neighbors list.
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
            
        return copy

    # Start the DFS traversal from the given input node
    return dfs(node) if node else None

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    print("Input: Custom Graph Structure")
    cloned = cloneGraph(node1)
    print(f"Output: First Node Value -> {cloned.val}, Neighbors count -> {len(cloned.neighbors)}")
