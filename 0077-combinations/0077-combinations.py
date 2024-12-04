class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(i, s):
            if len(s) == k:
                res.append(s[:])
                return
            if i > n or len(s) > k:
                return
            else:
                s.append(i)
                dfs(i+1,s)
                s.pop()
                dfs(i+1,s)
                
            return res
        dfs(1,[])
        
        return res