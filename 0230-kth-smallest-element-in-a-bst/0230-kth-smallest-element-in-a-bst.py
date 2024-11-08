# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k1, res = k,0
        
        def dfs(node):
            nonlocal k1, res
            
            if not node: return
            
            dfs(node.left)
            k1-=1
            if k1 == 0:
                res =  node.val
                return
            dfs(node.right)
            
        dfs(root)
        return res