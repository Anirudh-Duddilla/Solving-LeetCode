class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        sumcur = 0
        for n in nums:
            if sumcur < 0:
                sumcur = 0
            sumcur += n
            maxsum = max(maxsum, sumcur)
            
        return maxsum