class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sl = list(s)
        tl = list(t)
        j = 0
        for i, c in enumerate(s):
            # print(i, j, c, tl[j])
            while j < len(tl):
                if c == tl[j]:
                    # print(i, j, c, tl[j])
                    sl.pop()
                    j += 1
                    break
                j+=1
            # print(sl)
            # print(tl)
        print(sl)

        return True if sl == [] else False
            