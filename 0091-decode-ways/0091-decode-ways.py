class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        memo = {}

        def bt(sl):
            if sl in memo:
                return memo[sl]
            if sl == "":
                return 1
            if sl[0] == "0":
                return 0
            if len(sl) == 1:
                memo[sl] = 1
                return 1

            count = 0

            # Single digit (1â9)
            if 1 <= int(sl[-1]) <= 9:
                count += bt(sl[:-1])

            # Two digits (10â26)
            if len(sl) >= 2:
                two_digit = int(sl[-2:])
                if 10 <= two_digit <= 26:
                    count += bt(sl[:-2])

            memo[sl] = count
            return count

        return bt(s)
