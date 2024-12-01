class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = inf
        s = 0
        for r in range(0,len(nums)):
            s += nums[r]
            while s >= target:
                res = min(res, r-l+1)
                s -= nums[l]
                l += 1
        # while r < len(nums):
        #     print("l",l,"r",r,"s",s,"r",res,"r-l+1",r-l)
        #     if s >= target:
        #         res = min(res, r-l)
        #         s -= nums[l]
        #         l += 1
        #     else:
        #         s += nums[r]
        #         r += 1
        return 0 if res == inf else res