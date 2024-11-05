class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        # stck.append(s[0])
        for c in s:
            if (c is ')' or c is ']' or c is '}') and len(stck)==0:
                # print(len(stck), stck)
                return False
            if c is ')':
                # print(c, stck[-1])
                if stck[-1] is not '(':return False
                stck.pop()
            elif c is '}':
                # print(c, stck[-1])
                if stck[-1] is not '{':return False
                stck.pop()
            elif c is ']':
                # print(c, stck[-1])
                if stck[-1] is not '[':return False
                stck.pop()
            else:
                stck.append(c)
            # print(c, stck, stck[-1])
            
        return len(stck)==0
                