class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        
        # If there are only 2 steps, return the min of the first two
        if l == 2:
            return min(cost[0], cost[1])
        
        # Initialize the result array with -1 for memoization
        res_cost = [-1] * l
        
        # Base cases for the first two steps
        res_cost[0] = cost[0]
        res_cost[1] = cost[1]
        
        def recurse(n):
            # Return memoized result if already computed
            if res_cost[n] != -1:
                return res_cost[n]
            
            # Recursively calculate the cost for n-th step
            res_cost[n] = min(recurse(n-2) + cost[n], recurse(n-1) + cost[n])
            return res_cost[n]
        
        # Compute the result for the last step
        return min(recurse(l-1), recurse(l-2))
