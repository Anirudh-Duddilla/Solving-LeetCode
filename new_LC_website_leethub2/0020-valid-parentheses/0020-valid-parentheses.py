class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for c in s:
            if (c is ')' or c is ']' or c is '}') and len(stck)==0:
                return False
            if c is ')':
                if stck[-1] is not '(':return False
                stck.pop()
            elif c is '}':
                if stck[-1] is not '{':return False
                stck.pop()
            elif c is ']':
                if stck[-1] is not '[':return False
                stck.pop()
            else:
                stck.append(c)
            
        return len(stck)==0
                