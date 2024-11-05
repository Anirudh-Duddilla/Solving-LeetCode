class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res  = 0
        if len(s) == 0: return 0
        sset = set()
        l, r = 0, 0
        while r<len(s):
            if s[r] not in sset:
                sset.add(s[r])
                r+=1
            else:
                # print(l, s[l],r, s[r], sset)
                sset.discard(s[l])
                l+=1
            res = max(res, len(sset))
        return res