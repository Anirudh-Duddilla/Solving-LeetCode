# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l, r = head, head
        s = 1
        if k == 1:
            tl = l
        while r and r.next:
            # print(l.val,r.val)
            if s < k:
                s += 1
                tl = r
                # l = l.next
                r = r.next
                if s == k: r= r.next
                continue
                
            l = l.next
            r = r.next
        if k == 1:
            tl.val, r.val = r.val, tl.val
            return head
        if not r:
            tl.next.val, l.val = l.val, tl.next.val
            return head
        tr = l
        
        tl.next.val, tr.next.val = tr.next.val,tl.next.val
        return head
