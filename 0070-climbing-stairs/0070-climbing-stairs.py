class Solution:
    def climbStairs(self, n: int) -> int:
        res_list = [0] * (n+1)
        res_list[0] = 1
        res_list[1] = 1
        for i in range(2,n+1):
            res_list[i] = res_list[i-1] + res_list[i-2]
            
        return res_list[n]