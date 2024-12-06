# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_list = []
        total = 0
        q = deque()
        q.append(root)
        
        while q:
            curr = q.popleft()
            if low <= curr.val <= high:
                total+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                continue
            elif low > curr.val:
                curr = curr.right
            elif high < curr.val:
                curr = curr.left
            if curr:
                q.append(curr)
        return total
            