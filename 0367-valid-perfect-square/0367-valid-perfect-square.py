class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        if num == 1:return True
        while(l < r):
            m = (l+r)//2
            if m*m > num:
                r = m
            elif m*m < num:
                l = m + 1
            elif m*m == num:
                return True
        return False