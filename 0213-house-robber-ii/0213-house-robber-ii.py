class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        def simple_rob(nums):
            n = len(nums)
            print(nums)
            if len(nums) == 1:
                return nums[0]
            prev, curr = nums[0], max(nums[0], nums[1])

            for i in range(2,n):

                prev, curr = curr, max(curr, prev + nums[i])

            return curr

        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))