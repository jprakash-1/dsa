"""
Problem: Walls and Gates
You are given an m x n grid rooms initialized with these three possible values.
-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room.
Fill each empty room with the distance to its nearest gate.

Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""
import collections

def wallsAndGates(rooms):
    ROWS, COLS = len(rooms), len(rooms[0])
    visit = set()
    q = collections.deque() # Queue for Breadth-First Search (BFS)

    def addRoom(r, c):
        # Helper to safely add valid adjacent rooms to the queue
        if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
            (r, c) in visit or rooms[r][c] == -1):
            return
        visit.add((r, c))
        q.append([r, c])

    # Step 1: Find ALL gates and add them to our initial queue.
    # We start BFS from *multiple sources* simultaneously!
    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                q.append([r, c])
                visit.add((r, c))

    dist = 0
    # Step 2: Multi-Source Breadth-First Search
    while q:
        # Process all nodes at the current distance level
        for i in range(len(q)):
            r, c = q.popleft()
            
            # Since we do BFS, the *first* time we reach a room, 
            # we guarantee it's the *shortest* distance to a gate.
            rooms[r][c] = dist
            
            # Note: There's a bug in the original problem statement directions below. Correcting them.
            addRoom(r + 1, c) # Down
            addRoom(r - 1, c) # Up
            addRoom(r, c + 1) # Right
            addRoom(r, c - 1) # Left  <- Fix: Changed from (r - 1, c - 1)
            
        # After processing a full "ring", increment distance for the next outer ring
        dist += 1

if __name__ == "__main__":
    INF = 2147483647
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF]
    ]
    print(f"Input: rooms = {rooms}")
    wallsAndGates(rooms)
    print(f"Output: {rooms}")
