class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        res = 0
        while l <= r:
            m = (l+r)//2
            s = m*m
            print("l",l,"m",m,"r",r,"s",s,"x",x,"res",res)
            if s > x:
                r = m - 1
            else:
                res = max(res,m)
                l = m + 1
            
        return res