"""
Problem: Redundant Connection
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
Return an edge that can be removed so that the resulting graph is a tree of n nodes.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
"""

def findRedundantConnection(edges):
    # Union-Find / Disjoint Set Data Structure
    # par represents the parent root of a node. 1-indexed, so we add 1.
    par = [i for i in range(len(edges) + 1)]
    # rank represents the size of the set. Used to merge smaller sets into larger ones.
    rank = [1] * (len(edges) + 1)

    # The 'Find' function locates the root parent of a given node
    def find(n):
        p = par[n]
        # Keep traversing up the parent chain until a node is its own parent
        while p != par[p]:
            # Path compression: optimization to make future lookups faster
            par[p] = par[par[p]]
            p = par[p]
        return p

    # The 'Union' function attempts to connect two nodes
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        
        # If both nodes ALREADY share the same root parent, then adding this
        # edge will definitively create a cycle!
        if p1 == p2:
            return False

        # If they are from different sets, we merge them safely.
        # We merge the smaller rank tree INTO the larger rank tree for balance.
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
            
        return True

    # Iterate through all given edges
    for n1, n2 in edges:
        # If union returns False, it means we found the redundant edge creating the cycle!
        if not union(n1, n2):
            return [n1, n2]

if __name__ == "__main__":
    edges = [[1, 2], [1, 3], [2, 3]]
    print(f"Input: edges = {edges}")
    print(f"Output: {findRedundantConnection(edges)}")
