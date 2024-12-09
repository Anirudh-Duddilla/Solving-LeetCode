class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mono_inc = True
        mono_dec = True
        
        for i in range(len(nums)-1):
            if not (nums[i] <= nums[i+1]):
                mono_inc = False
            if not (nums[i] >= nums[i+1]):
                mono_dec = False
                
        return mono_inc or mono_dec