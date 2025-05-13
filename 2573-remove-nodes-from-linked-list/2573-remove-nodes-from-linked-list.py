# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt

            return prev

        head = reverse(head)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        max_val = head.val

        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
            

        head = reverse(dummy.next)

        return head

    