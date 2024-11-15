class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        res = 0
        max_area = 0
        def bfs(r,c):
            nonlocal res
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
                    grid[r][c] == 1 and
                    (r,c) not in visit):
                        res+=1
                        # print(res)
                        visit.add((r,c))
                        q.append((r,c))
            
        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    res = 1
                    visit.add((r,c))
                    bfs(r,c)
                    max_area = max(max_area,res)
        return max_area       