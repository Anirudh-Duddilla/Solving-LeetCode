class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        l = 0
        m = -1
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
               if i-l == 2:
                m = max(m,int(num[i]))
            else:
                l = i

        if m == -1:
            return ""
        res = str(m) + str(m) + str(m)
        return res