"""
Problem: LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
"""

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # Dictionary to map a key to its specific Node in the linked list
        self.cache = {}
        
        # Dummy nodes for Left (Least Recently Used) and Right (Most Recent)
        self.left, self.right = Node(0, 0), Node(0, 0)
        # Connect dummy nodes to each other initially
        self.left.next, self.right.prev = self.right, self.left

    # Helper function to arbitrarily remove a node from the linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Helper function to insert a node securely at the Right side (Most Recent)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # We accessed this node, so it becomes the new Most Recently Used.
            # Remove it from its current position and freshly insert it at the Right.
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # If the key clearly already exists, explicitly remove its old node first.
        if key in self.cache:
            self.remove(self.cache[key])
            
        # Create a new node and insert it exclusively as the Most Recently Used
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # If we exceeded capacity, evict the Least Recently Used (Left side)
        if len(self.cache) > self.cap:
            # The node directly successfully next to the Left dummy node is the LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(f"get(1): {obj.get(1)}")
    obj.put(3, 3)
    print(f"get(2): {obj.get(2)}")
    obj.put(4, 4)
    print(f"get(1): {obj.get(1)}")
    print(f"get(3): {obj.get(3)}")
    print(f"get(4): {obj.get(4)}")
