class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s = defaultdict(int)
        t = defaultdict(int)
        
        for t1,t2 in trust:
            s[t1] += 1
            t[t2] += 1
            
        for i in range(1,n+1):
            if s[i] == 0 and t[i] == n-1:
                return i
        return -1