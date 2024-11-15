class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minm = nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                return min(minm,nums[l])
            mid = (r+l)//2
            minm = min(minm, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
        return minm
            