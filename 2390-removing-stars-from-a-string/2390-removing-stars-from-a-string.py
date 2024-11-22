class Solution:
    def removeStars(self, s: str) -> str:
        q = deque()
        
        for c in s:
            # print(c,q)
            if c == '*':
                q.pop()
                continue
            q.append(c)
        
        w = ""
        
        for c in q:
            w += c
            
        return w