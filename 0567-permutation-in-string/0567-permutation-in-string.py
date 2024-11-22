class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        
        s1m, s2m = {}, {}
        s1l, s2l = [0]*26 ,[0]*26
        for s in s1:
            s1l[ord(s) - ord('a')] += 1
        l, r = 0, 0
        # print(len(s1),len(s2))
        while r < len(s2):
            # print(r)
            s2l[ord(s2[r]) - ord('a')] += 1
            if r >= len(s1) - 1:
                # print("l",l,"r",r)
                # print(s2[l],s2[r])
                # print("s1l",s1l)
                # print("s2l",s2l)
                if s1l == s2l:
                    return True
                else:
                    s2l[ord(s2[l]) - ord('a')] -= 1
                l += 1
                
            # s2l[ord(s2[r]) - ord('a')] += 1
               
            r+=1
        return False