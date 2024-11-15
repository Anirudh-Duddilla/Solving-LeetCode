# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        length = 0
        slw = list1
        # while fst and fst.next:
        #     length +=1
        #     fst = fst.next.next
        # length = length*2
    
        temp = ListNode()
        while length < b:
            if length == a-1:
                temp.next = slw.next
                curr = list2
                slw.next = curr
                slw = temp.next
                while curr.next:
                    curr = curr.next
            slw = slw.next
            length+=1
        curr.next = slw
        return list1