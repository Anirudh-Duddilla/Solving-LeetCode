class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visit = set()
        # srcolor = image[sr][sc]
        # image[sr][sc] = color
        
        def dfs(row,col):
            if (row,col) in visit:return
            visit.add((row,col))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]

            for dr, dc in dirs:
                r, c = row+dr, col+dc
                if (r in range(rows) and
                    c in range(cols) and
                    (r,c) not in visit and
                    image[r][c] == image[sr][sc]):
                    image[r][c] = color
                    dfs(r,c)
        dfs(sr,sc)
        image[sr][sc] = color
        
        return image