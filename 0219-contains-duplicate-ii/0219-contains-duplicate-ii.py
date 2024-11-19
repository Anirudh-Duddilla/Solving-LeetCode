class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        list_map = {}
        for i in range(0,len(nums)):
            if nums[i] not in list_map.keys():
                list_map[nums[i]] = i
            else:
                if abs(list_map[nums[i]] - i) <= k:
                    return True
                else:
                    list_map[nums[i]] = i
            
        return False