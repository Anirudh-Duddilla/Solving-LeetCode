class Solution:
    def fib(self, n: int) -> int:

        a, b = 0, 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            res = [0] * (n+1)
            res[0], res[1] = a, b
            for i in range(2, n+1):
                res[i] = res[i -1] + res[i-2]
            return res[n]
        