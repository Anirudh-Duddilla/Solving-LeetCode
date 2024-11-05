class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
                # r = l+1
                # continue
            res = max(res, diff)
            r+=1
            
        return res