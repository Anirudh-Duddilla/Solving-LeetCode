class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        final = set()

        for a,b in paths:
            start.add(a)
            final.add(b)
        return [b for b in final if b not in start][0]