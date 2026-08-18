"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        hashmap = {}
        cur = head
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next
        dummy = copy = Node(-1)
        while head:
            copy.next = hashmap[head]
            copy.next.random = hashmap.get(head.random)
            head = head.next
            copy = copy.next
        return dummy.next

        