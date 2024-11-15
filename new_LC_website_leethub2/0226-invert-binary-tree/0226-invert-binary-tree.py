# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        if not curr : return curr
        if not curr.left and not curr.right:
            return curr
        self.invertTree(curr.left)
        self.invertTree(curr.right)
        tmp = curr.right
        curr.right = curr.left
        curr.left = tmp
        return curr