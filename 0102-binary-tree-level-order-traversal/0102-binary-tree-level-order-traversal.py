# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        while q:
            qlen = len(q)
            t = []
            for i in range(qlen):
                node = q.popleft()
                # print(node)
                if node:
                    t.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if t:                
                res.append(t)
        return res
            