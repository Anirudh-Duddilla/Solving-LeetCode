class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0
        for i in range(0,len(nums)):
            if lsum == total - nums[i] - lsum:
                return i
            lsum += nums[i]
        return -1