# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        length = 0
        slw, fst = list1, list1
        
        while fst and fst.next:
            length +=1
            fst = fst.next.next
        length = length*2
    
        temp = ListNode()
        for i in range(0,b):
            if i == a-1:
                temp.next = slw.next
                # print(temp)
                curr = list2
                slw.next = curr
                slw = temp.next
                while curr.next:
                    curr = curr.next
                # print(slw,curr.val)
            # print(i,slw.val)
            slw = slw.next
        # print(slw)
        curr.next = slw
        # print(curr)
        # print(list1)
        # print(temp)
        
        return list1