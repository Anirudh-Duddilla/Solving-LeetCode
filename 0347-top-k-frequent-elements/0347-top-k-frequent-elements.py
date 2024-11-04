class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        res = []
        
        for n in nums:
            if n not in nums_map.keys():
                nums_map[n] = 1
            else:
                nums_map[n] += 1
        
        sorted_dict = dict(sorted(nums_map.items(), key=lambda item: item[1], reverse=True))
        k1= k
        for key, val in sorted_dict.items():
            if k > 0:
                res.append(key)
                k-=1
            else:
                return res
        return res
            
                
        