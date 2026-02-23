"""
Problem: Network Delay Time
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""
import collections
import heapq

def networkDelayTime(times, n, k):
    # Step 1: Build Adjacency List 
    # Maps a source node to a list of (target_node, travel_time)
    edges = collections.defaultdict(list)
    for u, v, w in times:
        edges[u].append((v, w))

    # Step 2: Dijkstra's Algorithm
    # Use a priority queue (Min-Heap) to constantly explore the path with the shortest time.
    # Store tuples of (current_total_time, current_node). Start at node 'k' at time 0.
    minHeap = [(0, k)]
    visit = set() # Keeps track of nodes that have securely received the signal!
    t = 0         # Tracks the maximum time needed for the signal to reach everyone
    
    while minHeap:
        # Pop the path with the lowest cumulative time so far
        w1, n1 = heapq.heappop(minHeap)
        
        # If we've already securely reached this node faster previously, skip this longer path.
        if n1 in visit:
            continue
            
        # We just reached node 'n1' for the first time!
        visit.add(n1)
        # Update our max timer (because every node processes concurrently, total time 
        # is just the max time it took to reach the *farthest* node).
        t = max(t, w1)
        
        # Explore the node's neighbors
        for n2, w2 in edges[n1]:
            # If a neighbor hasn't received the signal yet, 
            # push the *cumulative* time (time_to_reach_n1 + travel_time_to_n2) into the heap.
            if n2 not in visit:
                heapq.heappush(minHeap, (w1 + w2, n2))
                
    # If the set of visited nodes equals 'n', everyone got the signal!
    # If not, some nodes were disconnected and unreachable.
    return t if len(visit) == n else -1

if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(f"Input: times = {times}, n = {n}, k = {k}")
    print(f"Output: {networkDelayTime(times, n, k)}")
