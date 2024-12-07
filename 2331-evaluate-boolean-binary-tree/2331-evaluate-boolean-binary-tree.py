# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # res = 1
        def dfs(curr):
            if not curr.left and not curr.right:
                return bool(curr.val)
            # print("strt",curr.val)
            a = dfs(curr.left)
            b = dfs(curr.right)
            # print(curr.left.val,curr.val,curr.right.val)
            
            if curr.val == 2:
                # print("or",a,b,curr.left.val or curr.right.val)
                return a or b
            elif curr.val == 3:
                # print("and",a,b,curr.left.val and curr.right.val)
                return a and b
            
        return dfs(root)