class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 1
        while val in nums:
            if nums[idx-1] == val:
                nums.remove(nums[idx-1])
                idx-=1
            idx+=1
        return len(nums)