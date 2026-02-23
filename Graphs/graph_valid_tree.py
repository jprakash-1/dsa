"""
Problem: Graph Valid Tree
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
"""

def validTree(n, edges):
    if not n:
        return True

    # 1. Build the Adjacency List to represent our undirected graph
    adj = {i: [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visit = set()

    # 2. Depth-First Search to detect cycles and explore connected nodes
    # We pass 'prev' node to avoid mistakenly treating the edge we just came from as a cycle!
    def dfs(i, prev):
        # If we visit a node we've already seen (and it's NOT the direct parent we came from),
        # then we have naturally found a cycle! A valid tree CANNOT have cycles.
        if i in visit:
            return False

        visit.add(i)
        
        # Check all neighboring nodes
        for j in adj[i]:
            # Do not go back to the node we immediately came from!
            if j == prev:
                continue
            
            # If any downward path detects a cycle, the whole thing fails
            if not dfs(j, i):
                return False
                
        # No cycles found in this sub-graph!
        return True

    # A graph is a valid tree ONLY IF:
    # Condition 1: It has NO cycles (dfs returns True)
    # Condition 2: It is fully CONNECTED (we visited all 'n' nodes in one DFS pass)
    return dfs(0, -1) and n == len(visit)

if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(f"Input: n = {n}, edges = {edges}")
    print(f"Output: {validTree(n, edges)}")
