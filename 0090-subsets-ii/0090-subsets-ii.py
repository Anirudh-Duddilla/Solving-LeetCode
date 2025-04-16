class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(n, s):
            if n == len(nums):
                # print("E i",n, "s", s, "r", res)
                if s not in res:
                    res.append(s[:])
            else:
                # print("a i", n, "nums[i]", nums[n], "s", s)#,"r",res)
                s.append(nums[n])
                dfs(n+1, s)
                s.pop()
                # print("p i", n, "nums[i]", nums[n], "s", s)#,"r",res)
                dfs(n+1, s)

            return res
                

        dfs(0, [])
        print(res)
        return res