"""
Problem: Number of Connected Components in an Undirected Graph
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
"""

def countComponents(n, edges):
    # Union-Find / Disjoint Set Approach
    
    # Initially, every node is its own separate component (parent is itself)
    par = [i for i in range(n)]
    # 'rank' (or size) of each component. Initially, all components have size 1.
    rank = [1] * n

    # Find Function: Finds the absolute "root" parent of a given node
    def find(n1):
        res = n1
        # Traverse up the parent chain until the node is its own parent
        while res != par[res]:
            # Path Compression: Point directly to grandparent to flatten the tree structure!
            par[res] = par[par[res]] 
            res = par[res]
        return res # Return the root parent

    # Union Function: Connects two nodes together into the same component
    def union(n1, n2):
        # First, find the root parents of both nodes
        p1, p2 = find(n1), find(n2)
        
        # If they already share the same root parent, they are ALREADY connected!
        if p1 == p2:
            return 0 # 0 means we did NOT connect two separate components
            
        # Optimization (Union by Rank): Attach the smaller tree under the bigger tree
        if rank[p2] > rank[p1]:
            par[p1] = p2       # Make p2 the parent of p1
            rank[p2] += rank[p1] # p2's size increases by p1's size
        else:
            par[p2] = p1
            rank[p1] += rank[p2]
            
        return 1 # 1 means we successfully connected two separate components

    # We start assuming 'n' separate components.
    res = n
    
    # For every edge given, we try to unite the two nodes.
    for n1, n2 in edges:
        # If they unite successfully, it means two separate pieces joined into one!
        # So we decrease our total disconnected component count by 1.
        res -= union(n1, n2)
        
    return res

if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(f"Input: n = {n}, edges = {edges}")
    print(f"Output: {countComponents(n, edges)}")
