"""
Problem: Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    # Hash Map to link old nodes to their new deep copies.
    oldToCopy = {None: None}
    
    # Pass 1: Clone all nodes without linking them yet.
    cur = head
    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next
        
    # Pass 2: Connect the next and random pointers using our map.
    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
        
    return oldToCopy[head]

if __name__ == "__main__":
    node1 = Node(7)
    node2 = Node(13)
    node1.next = node2
    node2.random = node1
    print(f"Input: Linked List with Random Pointers")
    res = copyRandomList(node1)
    print(f"Output: Copied List Node1 Val -> {res.val}, Node2 Val -> {res.next.val}")
