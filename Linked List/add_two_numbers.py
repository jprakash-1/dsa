"""
Problem: Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Dummy node acts as a safe starting point.
    dummy = ListNode()
    cur = dummy
    
    # Carry stores the tens digit if addition goes over 9.
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        # Calculate raw sum.
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        
        # Attach new node.
        cur.next = ListNode(val)
        
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy.next

def printList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print("Input: l1 = [2,4,3], l2 = [5,6,4]")
    res = addTwoNumbers(l1, l2)
    print(f"Output: {printList(res)}")
