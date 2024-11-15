class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list_map = {}
        for i in range(0,len(nums)):
            if nums[i] not in list_map.keys():
                list_map[nums[i]] = 1
            else:
                list_map[nums[i]] += 1
                return True
            
        return False
        