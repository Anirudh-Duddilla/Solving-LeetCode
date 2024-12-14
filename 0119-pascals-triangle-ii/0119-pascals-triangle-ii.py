class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def recurse(n):
            if n == 0:
                return [1]
            else:
                s = recurse(n-1)
                q = []
                for i in range(len(s)):
                    if i == 0:
                        q.append(0+s[i])
                    else:
                        q.append(s[i-1]+s[i])
                    
                q.append(1)
                
                return q
            

        return recurse(rowIndex)