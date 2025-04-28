class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = 0
        r = []
        if s[0] == "0":
            return res
        
        memo = {}
        def bt(sl):

            if sl in memo:
                return memo[sl]
            if sl == "":
                return  1
            elif len(sl) == 1:
                memo[sl] = 1
                return 1
            elif len(sl) == 2:
                s0, s1 = int(sl[0]), int(sl[1])
                prod = (s0*10) + s1
                if s0 == 0 or (s1 == 0 and prod > 20):
                    memo[sl] = 0
                    return 0
                if prod < 27 and s1 != 0:
                    memo[sl] = 2
                    return 2
                elif prod < 27 and s1 == 0:
                    memo[sl] = 1
                    return 1
                else:
                    memo[sl] = 1
                    return 1
            else:
                s0, s1 = int(sl[-2]), int(sl[-1])
                prod = (s0 * 10) + s1
                if s1 == 0:
                    if 1<=s0<=2:
                        memo[sl] = bt(sl[0:-2])
                    else:
                        memo[sl] = 0
                elif prod < 27 and s0 != 0:
                    memo[sl] = bt(sl[0:-1]) + bt(sl[0:-2])
                else:
                    memo[sl] = bt(sl[0:-1])
                
                print("m",memo)
                return memo[sl]

        res = bt(s)

        return res
