class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        fresh = []
        fcount = 0
        time = 0
        q = deque()
        rows,cols = len(grid),len(grid[0])
        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fcount+=1
        # print(q,fcount)
        while q:
            row, col = q.popleft()
            visit.add((row,col))
            # print(row,col)
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in dirs:
                r,c = row+dr,col+dc
                if ( r in range(rows) and
                   c in range(cols) and
                   (r,c) not in visit and
                   (r,c) not in fresh):
                    if grid[r][c] == 1:
                        # print("r:",r,"c:",c)
                        fresh.append((r,c))
                        visit.add((r,c))
                        fcount-=1
            if not q and fresh:
                # print("F:",fresh,fcount)
                q .extend(fresh)
                # print("Q:",q)
                fresh = []
                time+=1
                
        if fcount > 0: return -1
        return time