# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = head, head.next
        res = ListNode()
        curr = res
        s = 0
        while r:
            if not r:
                break

            if r.val != 0:
                r = r.next
            else:
                # print(l.val, r.val, s, curr.val)
                if l.next == r:
                    l.val += s
                    # print(l.val, r.val, s, curr.val)
                    if not curr.next:
                        curr.next = l
                        l = l.next
                        curr = curr.next
                        curr.next = None
                    s = 0
                    r = r.next
                s += l.val
                l = l.next

        return res.next
