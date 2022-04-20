class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            if target - nums[i] in nums:
                if nums[i] == target - nums[i] and nums.count(nums[i]) >= 2:
                    return [i, nums.index(nums[i],i+1)]
                elif nums[i] == target - nums[i] and nums.count(nums[i]) < 2: continue
                else:return [i, nums.index(target-nums[i])]
                
        