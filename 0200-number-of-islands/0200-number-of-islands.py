class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        res = 0
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == "1" and
                    (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))
            
        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    visit.add((r,c))
                    bfs(r,c)
                    res+=1
        return res       