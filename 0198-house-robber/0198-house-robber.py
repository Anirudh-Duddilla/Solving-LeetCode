class Solution:
    def rob(self, nums: List[int]) -> int:
        
        l = len(nums)
        if l == 1:
            return nums[0]
        
        # Initialize the DP array
        res_cost = [0] * l
        res_cost[0] = nums[0]
        res_cost[1] = max(nums[0], nums[1])
        
        for i in range(2, l):
            res_cost[i] = max(res_cost[i - 2] + nums[i], res_cost[i - 1])
            
        
        
        return res_cost[-1]