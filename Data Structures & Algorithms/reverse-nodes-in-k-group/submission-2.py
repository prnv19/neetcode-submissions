# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = cur = ListNode()

        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        
        tail = head
        i = 0
        while tail:
            i += 1
            if i == k:
                nxt_group = tail.next
                tail.next = None
                new_head = reverse(head)
                cur.next = new_head
                head.next = nxt_group
                cur = head
                head = nxt_group
                tail = nxt_group
                i = 0
            else:
                tail = tail.next

        return dummy.next 
