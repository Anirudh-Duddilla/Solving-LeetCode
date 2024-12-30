class Solution:
    def firstUniqChar(self, s: str) -> int:
        sdict = defaultdict(list)
        slist = list(s)
        for i, c in enumerate(slist):
            sdict[c].append(i)
        res = inf
        for key in sdict:
            if len(sdict[key]) == 1:
                res = min(res, sdict[key][0])

        if res == inf:
            return -1
        return res