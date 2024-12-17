class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l == 2:
            return min(cost[0],cost[1])
        res_cost = [-1] * (len(cost))
        
        def recurse(n):
            
            if n == 0:
                # print(0)
                res_cost[0] = cost[0]
                return res_cost[0]
            elif n == 1:
                # print(1)
                res_cost[1] = cost[1]
                return res_cost[1]
            else:
                if res_cost[n] != -1:
                    return res_cost[n]
                    # print(res_cost,n)
                else:
                    # print(n,n-2,n-1)
                    res_cost[n] = min(recurse(n-2)+cost[n],recurse(n-1)+cost[n])
                    # print(res_cost,n,n-2,n-1)
                return res_cost[n]
                
        recurse(l - 1)
        
        print(res_cost)
        
        return min(res_cost[l-1], res_cost[l-2])