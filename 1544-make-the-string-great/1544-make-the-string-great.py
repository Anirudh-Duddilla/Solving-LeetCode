class Solution:
    def makeGood(self, s: str) -> str:
        stck = []
        
        for c in s:
            if stck and stck[-1].lower() == c.lower() and stck[-1] != c:
                # print(stck[-1],c)
                stck.pop()
                continue
            stck.append(c)
        
        return "".join(stck)