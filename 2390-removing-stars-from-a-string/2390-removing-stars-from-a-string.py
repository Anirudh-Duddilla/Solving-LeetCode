class Solution:
    def removeStars(self, s: str) -> str:
        q = []
        
        for c in s:
            if c == '*':
                q.pop()
                continue
            q.append(c)
        
        w = ""
        
        for c in q:
            w += c
            
        return w