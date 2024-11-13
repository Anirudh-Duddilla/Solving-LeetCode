class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        length = len(s)
        smap, tmap = {}, {}
        
        for c1, c2 in zip(s, t):
            if ((c1 in smap and smap[c1] != c2) or
               (c2 in tmap and tmap[c2] != c1)):
                return False
            smap[c1] = c2
            tmap[c2] = c1
        return True