class Solution:
    def hammingWeight(self, n: int) -> int:
        x = 1
        res = 0
        while x<=n:
            if n & x:
                res += 1
            x = x << 1
            
        return res