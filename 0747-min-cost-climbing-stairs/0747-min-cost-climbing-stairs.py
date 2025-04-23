class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0] * len(cost)

        res[0], res[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            # print("r[i-2]", res[i-2], "r[i-1]", res[i-2], "c[i]", cost[i])
            res[i] = min(cost[i]+res[i-1], cost[i]+res[i-2])
        
        # print(res)

        return min(res[-1], res[-2])