# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque()
        res = []
        level = 0
        q.append(root)
        while q:
            qlen = len(q)
            t=[]
            level+=1
            for i in range(qlen):
                if level%2 != 0:
                    node = q.popleft()
                    if not node:
                        continue
                    t.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    node = q.pop()
                    t.append(node.val)
                    if not node:
                        continue
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
            #     print(node.val, i, q)
            # print(t)
            res.append(t)
        
        return res            