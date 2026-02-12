# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # 1. Setup Dummy Node
        # This ensures we always have a 'node before' even if left = 1
        dummy = ListNode(0)
        dummy.next = head
        follow = dummy
        
        # 2. Advance to the reversal point
        # 'follow' will stop at the node immediately before 'left'
        curr = head
        for _ in range(1, left):
            follow = follow.next
            curr = curr.next
            
        # 3. Perform Sub-segment Reversal
        # 'stagnant' tracks the node that will become the new tail of this segment
        prev = None
        stagnant = curr
        i = left
        while i <= right:
            temp = curr.next  # Keep track of the rest of the list
            curr.next = prev  # Reverse the link
            prev = curr       # Move prev forward
            curr = temp       # Move curr forward
            i += 1
            
        # 4. Re-stitch the list
        # follow.next connects the 'before' part to the new 'front' (prev)
        # stagnant.next connects the 'new tail' to the 'after' part (curr/temp)
        follow.next = prev
        stagnant.next = curr
        
        return dummy.next