class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = []
        def dfs(i,s):
            if i == len(nums):
                res.append(s)
                # print("len",i, res,s)
                return res
            else:
                s.append(nums[i])
                s1 = s.copy()
                # print("bef",i, res,s)
                dfs(i+1, s)
                s1.pop()
                print("aft",i, res,s1)
                dfs(i+1, s1)
            #     print("all",i, res)
            # print("end",i, res,s,s1)
            return res
        
        dfs(0,s)
        
        return res