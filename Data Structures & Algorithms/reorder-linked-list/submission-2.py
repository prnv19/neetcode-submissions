# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        slow.next = None

        prev, cur = None, second_head
        while cur:
            t = cur.next
            cur.next = prev
            prev, cur = cur, t
        second_head = prev

        #merge
        cur = head
        while cur and second_head:
            t1 = cur.next
            t2 = second_head.next

            cur.next = second_head
            second_head.next = t1
            cur = t1
            second_head = t2
        return None