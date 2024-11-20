class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visit = set()
        q = deque()
        
        rows, cols = len(grid), len(grid[0])
        ls = list(itertools.product(list(range(1,rows-1)), list(range(1,cols-1))))
        for i in range(0,rows):
            for j in range(0,cols):
                if ((i == 0 or i == rows - 1 or 
                    j == 0 or j == cols - 1) and 
                   grid[i][j] == 1):
                    # print("fl")
                    grid[i][j] = 2
                    q.append((i,j))
        
        dirs = [[1,0],[0,1],[0,-1],[-1,0]]
                    
        while q:
            row, col = q.popleft()
            if (row,col) in visit:continue
            visit.add((row,col))
            
            for dr, dc in dirs:
                r, c = row+dr, col+dc
                
                if (r in range(1,rows-1) and
                   c in range(1,cols-1) and
                   (r,c) not in visit and
                   grid[r][c] == 1):
                    grid[r][c] = 2
                    q.append((r,c))
        res = 0
        # print(grid)
        for rw in range(1,rows-1):
            for cl in range(1,cols-1):
                if grid[rw][cl] == 1 and (rw,cl) not in visit:
                    res += 1
                    visit.add((rw,cl))
        
        return res