class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        visit = set()
        dontvisit = set()
        res = 0
        def bfs(row,col):
            nonlocal res
            if (row,col) in visit:return
            visit.add((row,col))
            dirs = [[1,0],[0,1],[0,-1],[-1,0]]
            
            for dr, dc in dirs:
                r, c = row+dr, col+dc
                
                if r not in range(rows) or c not in range(cols):
                    res+=1
                elif grid[r][c] == 0:
                    res += 1
                    
        for r1 in range(0,rows):
            for c1 in range(0,cols):
                if grid[r1][c1] == 1 and (r1,c1) not in visit:
                    bfs(r1,c1)
        return res