class Solution:
    def climbStairs(self, n: int) -> int:
        res_list = [0] * 2
        res_list[0] = 1
        res_list[1] = 1
        total = res_list[1]
        for i in range(2,n+1):
            total = res_list[0] + res_list[1]
            res_list[0],res_list[1] = res_list[1],total
        return total