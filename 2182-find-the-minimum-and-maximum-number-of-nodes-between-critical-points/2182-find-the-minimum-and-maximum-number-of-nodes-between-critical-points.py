# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mind, maxd = inf, -1

        prev, curr = head, head.next
        i, j, k = 0, 0, 1
        while curr.next:

            if prev.val > curr.val < curr.next.val or prev.val < curr.val > curr.next.val:
                # print("i", i, "j", j, "k", k)
                # print("mind", mind)
                # print("maxd", maxd)
                i = k if i == 0 else i
                maxd = max(maxd, k - i) if maxd <= 0 else k - i
                if j != 0:
                    mind = min(mind, k - j) if mind != inf else k - j

                j = k
            prev = curr
            curr = curr.next
            k += 1

        mind = mind if mind != inf else -1
        maxd = maxd if maxd > 0 else -1

        return [mind, maxd]
