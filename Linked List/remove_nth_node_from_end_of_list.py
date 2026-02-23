"""
Problem: Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Dummy node to handle edge cases like removing the head itself.
    dummy = ListNode(0, head)
    
    # We use two pointers starting from dummy and head.
    left = dummy
    right = head
    
    # First, move the 'right' pointer forward by exactly 'n' steps.
    # This creates a gap of 'n' nodes between 'left' and 'right'.
    while n > 0 and right:
        right = right.next
        n -= 1
        
    # Now, move both pointers forward at the same uniform speed.
    # Because of the gap, when 'right' hits the end, 
    # 'left' will be pointing exactly at the node BEFORE the one we want to remove!
    while right:
        left = left.next
        right = right.next
        
    # Delete the target node by bypassing it.
    left.next = left.next.next
    
    return dummy.next

def printList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    print(f"Input: head = [1, 2, 3, 4, 5], n = {n}")
    res = removeNthFromEnd(head, n)
    print(f"Output: {printList(res)}")
