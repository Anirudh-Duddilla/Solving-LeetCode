class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length

        s = []

        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                # print(s)
                st, si = s.pop()
                res[si] = i - si
                # print(i, si)
                # print(t,st)
                # print(res)
            s.append([t,i])

        return res