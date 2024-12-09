class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l ,r = 0, len(nums) - 1
        
        while l <= r:
            m = (l+r)//2
            # m = l+((r-l)//2)
            # print(l,m,r)
            if ((m-1<0 or nums[m-1] != nums[m])
                and (m+1==len(nums) or nums[m] != nums[m+1])):
                return nums[m]
            else:
                if nums[m] == nums[m-1]:
                    leftszie = m -1
                else:
                    leftszie = m
                if leftszie % 2:
                    r = m - 1
                else:
                    l = m + 1
                    
        return nums[m]