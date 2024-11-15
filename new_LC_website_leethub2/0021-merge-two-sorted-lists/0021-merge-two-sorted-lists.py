# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        e = l
        p = None
        while list1 or list2:
            if not list1:
                e.next = list2
                break
            elif not list2:
                e.next = list1
                break
            elif list1.val >= list2.val:
                p = list2
                list2 = list2.next
            else:
                p = list1
                list1 = list1.next
            e.next = p
            e = e.next
        return l.next
    