class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = set()
        rows, cols = len(board), len(board[0])
        q = deque()
        borderls = []
        
        ls = list(itertools.product(list(range(1,rows-1)), list(range(1,cols-1))))
        for r in range(0,rows):
            for c in range(0,cols):
                if ((r,c) not in ls and
                    board[r][c] == 'O'):
                    q.append((r,c))
                    borderls.append((r,c))
                    visit.add((r,c))
        
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        # print(borderls, q)
        while q:
            row, col = q.popleft()
            
            for dr, dc in dirs:
                r, c = row+dr, col+dc
                if ( r in range(rows) and
                   c in range(cols) and
                   (r,c) not in visit and
                   board[r][c] == 'O'):
                    visit.add((r,c))
                    borderls.append((r,c))
                    q.append((r,c))
        # print(borderls)
        # print(q)
        def bfs(row,col):
            if (row, col) in visit: return
            visit.add((row,col))
            # print(row,col)
            for dr, dc in dirs:
                r, c = row+dr, col+dc
                # print((r,c) not in visit,board[r][c] == 'O',(r,c) not in borderls)
                if ( r in range(rows) and
                   c in range(cols) and
                   (r,c) not in visit and
                   board[r][c] == 'O' and
                   (r,c) not in borderls):
                    # print((r,c))
                    board[r][c] = 'X'
                    # print(board[r][c])
                    bfs(r,c)
                    
        for r in range(0,rows):
            for c in range(0,cols):
                if board[r][c] == 'O' and (r,c) not in visit:
                    board[r][c] = 'X'
                    bfs(r,c)
                    
        # print(visit)