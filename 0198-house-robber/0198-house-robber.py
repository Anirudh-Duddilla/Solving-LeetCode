class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[-1]
        # elif len(nums) == 2:
        #     return max(nums[-1], nums[-2])
        else:

            res = [0] * len(nums)
            res[0], res[1] = nums[0], max(nums[0],nums[1])
            for i in range(2,len(nums)):

                res[i] = max(res[i-1], res[i-2]+ nums[i])

            # print(res)

        return max(res[-1], res[-2])
