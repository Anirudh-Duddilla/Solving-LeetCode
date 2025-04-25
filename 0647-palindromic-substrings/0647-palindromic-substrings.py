class Solution:
    def countSubstrings(self, s: str) -> int:
        sl = list(s)
        res = []
        def pal(i,j, n, s1):
            r = []
            while i >=0 and j < n and s1[i] == s1[j]:
                if j - i >= 0:
                    # print("eif", i, j+1, s1[i:j+1])
                    r.append(s1[i:j+1])
                i, j = i-1, j+1
                
            # print("s1",s1,"r",r)
            return r

        def palsubstr(s):
            n = len(s)
            for i in range(0, n):
                odd = pal(i,i,n,s)
                if odd !="":
                    res.extend(odd)
                # print("reso", res)
                # print("o", odd, "i",i)
                if (i+1) < n and s[i] == s[i+1]:
                    even = pal(i,i+1,n,s)
                    if even !="":
                        res.extend(even)
                # print("e", even,"i",i,"i+1",i+1)
                    # print("rese", res)
        palsubstr(s)
        # print(res)
        return len(res)
            