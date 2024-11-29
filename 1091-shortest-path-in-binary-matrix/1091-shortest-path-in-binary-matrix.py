class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[ROWS-1][COLS-1] != 0:
            return -1
        visit = set()
        q = deque([(0,0,1)])
        visit.add((0,0))
        dirs = [[-1,-1],[-1,0],[-1,1],
               [0,-1],[0,1],
               [1,-1],[1,0],[1,1]]
        
        while q:
            row, col, length = q.popleft()
            if row == ROWS-1 and col == COLS-1:
                return length
            for dr,dc in dirs:
                r, c = row+dr, col+dc
                if (r in range(ROWS) and
                   c in range(COLS) and
                   grid[r][c] == 0 and
                   (r,c) not in visit):
                    q.append((r,c,length+1))
                    visit.add((r,c))
                    
        return -1