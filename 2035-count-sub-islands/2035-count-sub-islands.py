class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or 
                grid2[r][c] == 0 or (r, c) in visit):
                return True
            
            visit.add((r, c))
            res = grid1[r][c]
            
            res &= dfs(r - 1, c)
            res &= dfs(r + 1, c)
            res &= dfs(r, c - 1)
            res &= dfs(r, c + 1)
            return res
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visit:
                    count += dfs(r, c)
        return count