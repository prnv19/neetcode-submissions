# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        res = ListNode()
        tail = res

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return res.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        i = 1
        if len(lists) == 1:
            return lists[0]
        elif lists == []:
            return None
    
        while i < len(lists):
            lists[i] = self.mergeTwoLists(lists[i-1], lists[i])
            i += 1
        print(len(lists))
        print(i)
        return lists[i-1]
        
        