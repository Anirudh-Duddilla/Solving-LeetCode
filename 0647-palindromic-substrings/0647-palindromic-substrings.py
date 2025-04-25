class Solution:
    def countSubstrings(self, s: str) -> int:
        sl = list(s)
        # res = []
        reslen = 0
        def pal(i,j, n, s1):
            # r = []
            rl = 0
            while i >=0 and j < n and s1[i] == s1[j]:
                if j - i >= 0:
                    # print("eif", i, j+1, s1[i:j+1])
                    # r.append(s1[i:j+1])
                    rl+=1
                i, j = i-1, j+1
                
            # print("s1",s1,"r",r)
            return rl

        def palsubstr(s):
            n = len(s)
            reslen = 0
            for i in range(0, n):
                odd = pal(i,i,n,s)
                if odd !="":
                    # res.extend(odd)
                    reslen+=odd
                # print("reso", reslen)
                # print("o", odd, "i",i)
                if (i+1) < n and s[i] == s[i+1]:
                    even = pal(i,i+1,n,s)
                    if even !="":
                        # res.extend(even)
                        reslen+=even
                    # print("e", even,"i",i,"i+1",i+1)
                    # print("rese", reslen)
            return reslen
        reslen = palsubstr(s)
        # print(res)
        return reslen
            