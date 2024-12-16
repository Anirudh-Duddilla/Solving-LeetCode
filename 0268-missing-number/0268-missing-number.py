class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        s = int((l*(l+1))/2)
        res = 0
        
        for n in nums:
            res = res + n
            
        # print(s,res)
        return s-res