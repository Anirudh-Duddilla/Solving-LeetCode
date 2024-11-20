class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        
        while l <= r:
            mid = (l+r)//2
            f = round((mid*(mid+1))/2)
            if f > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)
        return res