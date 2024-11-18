class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l<r:
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 != 0:
                r -= 1
            if nums[l] % 2 != 0 and nums[r] % 2 == 0 and l<r:
                nums[l], nums[r] = nums[r], nums[l]
        return nums