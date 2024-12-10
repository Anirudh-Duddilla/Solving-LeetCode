# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = []
        res = []
        
        def dfs(root):
            # print(stack)
            stack.append(str(root.val))
            
            if not root.left and not root.right:
                res.append("->".join(stack))
            else:
                if root.left:
                    dfs(root.left)
                    stack.pop()
                # stack.pop()
                if root.right:
                    dfs(root.right)
                    stack.pop()
                
        dfs(root)
        return res