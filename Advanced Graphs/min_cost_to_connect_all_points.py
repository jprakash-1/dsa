"""
Problem: Min Cost to Connect All Points
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
"""
import heapq

def minCostConnectPoints(points):
    N = len(points)
    # Step 1: Build the Adjacency List representing the graph.
    # We map each point (index i) to a list of its neighbors.
    # Each neighbor is stored as [cost_to_reach, neighbor_index]
    adj = {i: [] for i in range(N)}
    
    # Calculate the Manhattan distance between EVERY pair of points (complete graph)
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            # It's an undirected graph, so add the edge to both points!
            adj[i].append([dist, j])
            adj[j].append([dist, i])
            
    # Step 2: Prim's Algorithm to find the Minimum Spanning Tree (MST)
    res = 0      # Total minimum cost
    visit = set() # Keeps track of points we've already securely connected
    
    # Min-Heap to cleanly pick the currently available edge with the LOWEST COST.
    # Start at point 0 with cost 0: [cost, point_index]
    minH = [[0, 0]]
    
    # We continue until ALL 'N' points are in our 'visit' set
    while len(visit) < N:
        # Pop the cheapest available connection from our heap
        cost, i = heapq.heappop(minH)
        
        # If we already connected this point, just ignore it and pull the next one.
        if i in visit:
            continue
            
        # We found a new point to connect!
        res += cost       # Add its connection cost to our total
        visit.add(i)      # Mark it as connected
        
        # Now, grab all the edges going OUT of this newly connected point
        for neiCost, nei in adj[i]:
            # If the neighbor isn't connected yet, throw the potential path into the heap!
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei])
                
    return res

if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(f"Input: points = {points}")
    print(f"Output: {minCostConnectPoints(points)}")
