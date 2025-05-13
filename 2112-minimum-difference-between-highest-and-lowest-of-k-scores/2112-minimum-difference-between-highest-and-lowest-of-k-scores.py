class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mindif = inf
        for i in range(0, len(nums)-k+1):
            mindif = min(mindif, nums[i+k-1]-nums[i])

        return mindif

