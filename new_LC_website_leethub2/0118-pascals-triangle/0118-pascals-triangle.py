class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        sm = 0
        if numRows == 1:
            return res
        
        for i in range(1,numRows):
            l, r, e = -1,0,len(res[i-1])
            ls = []
            while r<=e:
                if l == -1:
                    sm = 0+res[i-1][r]
                elif r == e:
                    sm = 0+res[i-1][l]
                else:
                    sm = res[i-1][l]+res[i-1][r]
                ls.append(sm)
                l+=1
                r+=1
            res.append(ls)
        return res