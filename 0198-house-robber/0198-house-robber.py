class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        res_cost = [-1] * l
        
        res_cost[0] = nums[0]
        if l > 1:
            res_cost[1] = max(nums[0],nums[1])
        
        def recurse(n):
            
            if res_cost[n] == -1:
                # print(n,n-2,n-1,nums[n-2], nums[n-1])
                res_cost[n] = max(recurse(n-2)+nums[n],recurse(n-1))
                # print(n,n-2,n-1)
                # print(res_cost[n], res_cost[n-2],res_cost[n-1],res_cost)
            return res_cost[n]
                
        recurse(l-1)
        
        # print(res_cost)
        
        return res_cost[-1]