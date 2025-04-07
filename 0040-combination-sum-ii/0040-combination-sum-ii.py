class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, sm, s):
            # print("i: ", i, "sm: ", sm, "s: ", s)
            if sm == target :
                res.append(s[:])
                return
            elif sm > target or i >= len(candidates):
                return
            else:
                s.append(candidates[i])
                dfs(i+1,sm + candidates[i], s)
                s.pop()
                while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i += 1
                dfs(i+1,sm, s)
                
            return res
        dfs(0,0,[])
        return res