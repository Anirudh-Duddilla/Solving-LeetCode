# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        s = deque()
        curr = root
        q.append(curr)
        s.append(curr)
        while q and s:
            nq = q.popleft()
            ns = s.popleft()
            # print(nq.val,ns.val)
            if nq and ns and nq.val != ns.val:
                return False
            elif not nq or not ns:
                break
            else:
                if nq.left or ns.right:
                    q.append(nq.left)
                    s.append(ns.right)
                if nq.right or ns.left:
                    q.append(nq.right)
                    s.append(ns.left)
        
        # print(q)
        return True if q == s else False