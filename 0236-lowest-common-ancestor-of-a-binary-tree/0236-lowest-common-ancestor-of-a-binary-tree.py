# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        elif root == p or root == q:
            return root
        
        pr = self.lowestCommonAncestor(root.left, p, q)
        qr = self.lowestCommonAncestor(root.right, p, q)
            
        if pr and qr:
            return root
        else:
            if pr and not qr:
                return pr
            if qr and not pr:
                return qr
        if not pr and not qr:
            return None