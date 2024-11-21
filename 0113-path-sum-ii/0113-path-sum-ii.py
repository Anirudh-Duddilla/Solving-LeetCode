# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        l = []
        
        def findpaths(node,s,l):
            if not node: return
            
            s += node.val
            l.append(node.val)
            # print("r",node.val,"s",s,"l",l)
            
            if not node.left and not node.right and s == targetSum:
                paths.append(list(l))
                print(paths)
                
            findpaths(node.left,s,l)
            findpaths(node.right,s,l)
            l.pop()
            # print("r",node.val,"s",s,"l",l)
        findpaths(root,0,l)
        return paths