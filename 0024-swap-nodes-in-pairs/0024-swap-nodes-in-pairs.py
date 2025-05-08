# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(-1)
        dummy.next = head
        dum, prev, curr = dummy, head, head.next
        

        while prev and curr:
            # print("d", dum.val,"p", prev.val, "c", curr.val, "h", head.val)
            dum.next = curr
            prev.next = curr.next
            curr.next = prev

            dum = prev
            prev = prev.next
            if not prev or not prev.next: break
            curr = prev.next
            # print("d", dum.val,"p", prev.val, "c", curr.val, "h", head.val)

        return dummy.next