# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        s = 0
        while r:
            print(s,n, l.val,r.val)
            if s < n:
                s+=1
                r = r.next
                continue
            if not r.next:
                t = l.next
                l.next = t.next
                t.next = None
            r = r.next
            l = l.next

        if l == head:
            head = head.next
            l.next =None
        return head