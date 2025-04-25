class Solution:
    def countSubstrings(self, s: str) -> int:
        reslen = 0
        def pal(i,j, n, s1):
            rl = 0
            while i >=0 and j < n and s1[i] == s1[j]:
                if j - i >= 0:
                    rl+=1
                i, j = i-1, j+1
            return rl

        def palsubstr(s):
            n = len(s)
            reslen = 0
            for i in range(0, n):
                reslen+=pal(i,i,n,s)
                if (i+1) < n and s[i] == s[i+1]:
                    reslen+=pal(i,i+1,n,s)
            return reslen

        reslen = palsubstr(s)
        return reslen
            