class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)]
        
        rows, cols = len(board), len(board[0])
        x, y = click[0], click[1]
        
        # If the clicked cell is a mine, game over. Return the board with 'X' marked.
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        # Set for visited cells
        visited = set()
        q = deque([(x, y)])  # Queue for BFS
        
        # Helper function to count mines around a cell
        def count_mines(r, c):
            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count
        
        while q:
            row, col = q.popleft()
            
            # Skip if already visited
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            
            # Count adjacent mines
            mine_count = count_mines(row, col)
            
            # If there are mines around, mark the cell with the count
            if mine_count > 0:
                board[row][col] = str(mine_count)
            else:
                # If no adjacent mines, mark as 'B' and add neighbors to queue
                board[row][col] = 'B'
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        if board[nr][nc] == 'E':  # Only process empty cells
                            q.append((nr, nc))
        
        return board