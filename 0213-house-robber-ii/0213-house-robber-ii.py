class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[-1]
        elif len(nums) == 2:
            return max(nums[-1], nums[-2])
        else:

            res1 = [0] * (n-1)
            res1[0], res1[1] = nums[0], max(nums[0],nums[1])

            for i in range(2,n-1):

                res1[i] = max(res1[i-1], res1[i-2]+ nums[i])

            # print("r1",res1)

            res2 = [0] * (n)
            res2[1], res2[2] = nums[1], max(nums[1],nums[2])
            # print("r2", res2)
            for i in range(2,n):
                # print("i", i, "n[i]", nums[i], "r2[i]", res2[i])
                # print("r2[i-1]", res2[i-1],"r2[i-2]", res2[i-2], "n[i]", nums[i])
                res2[i] = max(res2[i-1], res2[i-2]+ nums[i])
                # print("r2", res2)


        return max(res1[-1], res2[-1])
