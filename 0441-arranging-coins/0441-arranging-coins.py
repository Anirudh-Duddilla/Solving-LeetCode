class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        def formula(m):
            # print(m,int((m*(m+1))/2))
            return round((m*(m+1))/2)
        
        while l <= r:
            mid = (l+r)//2
            f = formula(mid)
            # print("l",l,"m",mid,"f",f,"r",r,"n",n)
            if f > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)
                # return mid
        return res