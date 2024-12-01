class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = inf
        s = 0
            
        while r < len(nums):
            s += nums[r]
            r+=1
            while s >= target:
                res = min(res, r-l)
                s -= nums[l]
                l += 1
        return 0 if res == inf else res