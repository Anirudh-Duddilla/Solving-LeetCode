# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:return False
        res = root.val
        stck = []
        stck.append((root,res))
        
        while stck:
            node,r = stck.pop()
            # res += node.val
            # print(node.val,r)
            if not node.left and not node.right:
                if r == targetSum:return True
                # else:
                #     print("end",r)
                #     # res -= node.val
            if node.right:
                stck.append((node.right, r+node.right.val))
            if node.left:
                stck.append((node.left, r+node.left.val))
                    
        return False
        