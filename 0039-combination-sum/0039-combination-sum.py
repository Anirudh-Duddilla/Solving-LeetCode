class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i,sm, s):
            # print("strt",i,sm,s)
            if sm == target:
                res.append(s[:])
                # print("res",i,sm,s,res)
                return res
            elif sm > target or i == len(candidates):
                # print("sm>tar",i,sm,s)
                return
            else:
                s.append(candidates[i])
                sm += candidates[i]
                dfs(i,sm, s)
                s.pop()
                sm -= candidates[i]
                dfs(i+1, sm, s)
                
            return res
        dfs(0,0,[])
        return res