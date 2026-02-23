"""
Problem: Reorder List
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head:
        return
        
    # Step 1: Find the middle of the linked list using Slow and Fast pointers.
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # Step 2: Reverse the second half of the linked list.
    # 'second' is the start of the second half.
    second = slow.next
    # We sever the connection between the first and second half.
    prev = slow.next = None
    
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
        
    # Step 3: Merge the two halves.
    # 'first' points to the head, 'second' points to the new head of reversed half.
    first, second = head, prev
    while second:
        # Save next pointers before modifying them.
        tmp1, tmp2 = first.next, second.next
        
        # Insert the 'second' node right after 'first'.
        first.next = second
        second.next = tmp1
        
        # Move pointers forward for the next iteration.
        first, second = tmp1, tmp2

def printList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(f"Input: [1, 2, 3, 4]")
    reorderList(head)
    print(f"Output: {printList(head)}")
