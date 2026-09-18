# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            s = 0
            node = ListNode()
            s += l1.val if l1 else 0
            s += l2.val if l2 else 0
            s += carry

            node.val = s if s < 10 else s % 10
            carry = 1 if s >= 10 else 0
            
            cur.next = node
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next

        