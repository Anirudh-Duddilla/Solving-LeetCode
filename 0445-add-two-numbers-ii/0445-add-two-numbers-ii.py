# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            
            return prev

        l1curr = reverse(l1)
        l2curr = reverse(l2)

        res = self.addTwoNumbersrev(l1curr, l2curr)

        res = reverse(res)

        return res


    def addTwoNumbersrev(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1curr = l1
        l2curr = l2
        dummy = ListNode()
        res = dummy
        s = 0
        while l1curr or l2curr:
            val1 = l1curr.val if l1curr else 0
            val2 = l2curr.val if l2curr else 0
            s = val1 + val2 + s
            if s >= 10:
                v = s % 10
                res.next = ListNode(v)
                s = s // 10
            else:
                res.next = ListNode(s)
                s = 0
            res = res.next
            if l1curr:
                l1curr = l1curr.next
            if l2curr:
                l2curr = l2curr.next

        if s > 0:
            res.next = ListNode(s)

        return dummy.next
