class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        fromset = set()
        for p in paths:
            fromset.add(p[0])
            
        for p in paths:
            if p[1] not in fromset:
                return p[1]