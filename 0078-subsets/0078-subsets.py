class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = []
        def dfs(i,s):
            if i == len(nums):
                res.append(s)
                # print("end",i,res,s)
                return res
            else:

                # print(res,s)
                # print(res,s)
                s.append(nums[i])
                s1 = s.copy()
                # print("b",res,s)
                dfs(i+1, s)
                # print("a",i,res,s)
                # res.append(s)
                s1.pop()
                dfs(i+1, s1)
                # print(i,res,s)
                # res.append(s1)
            # print(i,res,s)
            return res
        
        dfs(0,s)
        
        return res