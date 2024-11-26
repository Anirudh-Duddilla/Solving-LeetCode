class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = nums[0], 1
        for i,n in enumerate(nums):
            if i != 0:
                # print(i,n,res,count)
                if res == n:
                    count += 1
                else:
                    count -= 1
                    if count == 0:
                        res = n
                        count += 1
        return res