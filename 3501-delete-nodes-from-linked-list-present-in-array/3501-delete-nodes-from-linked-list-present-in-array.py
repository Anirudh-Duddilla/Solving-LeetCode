# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums_set = set(nums)  # Convert to set for O(1) lookups
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val in nums_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next