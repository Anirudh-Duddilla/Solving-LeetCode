class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0, n+1):
            x = 1
            count = 0
            while x <= i:
                # print(x,i,count)
                if x & i:
                    count+=1
                x = x << 1
            res.append(count)
            
        return res