# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fst, slw = head, head
        while fst and fst.next:
            fst = fst.next.next
            slw = slw.next
            if fst == slw:return True
        
        return False