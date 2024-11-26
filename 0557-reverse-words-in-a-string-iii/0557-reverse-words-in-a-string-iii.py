class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, 0
        sl = list(s)
        while r < len(sl):
            # print(l,s[l],r,s[r])
            
            if r+1 < len(sl) and sl[r+1]!=" ":
                r+=1
            else:
                m = r
                while l < r:
                    # print(l,sl[l],r,sl[r],m)
                    sl[l], sl[r] = sl[r],sl[l]
                    l += 1
                    r -= 1
                l = m+2
                r = m + 2
                # print(l,r)
        # print(sl)
        return "".join(sl)