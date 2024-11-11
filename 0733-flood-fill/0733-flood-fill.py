class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visit = set()
        srcolor = image[sr][sc]
        # visit.add((sr,sc))
        image[sr][sc] = color
        
        def dfs(row,col):
            if (row,col) in visit:return
            visit.add((row,col))
            # print(row,col)
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]

            for dr, dc in dirs:
                r, c = row+dr, col+dc
                # print("r ",r,"c ",c,"i ",image[r][c],"col ",color)
                if (r in range(rows) and
                    c in range(cols) and
                    (r,c) not in visit and
                    image[r][c] == srcolor):
                    image[r][c] = color
                    # visit.add((r,c))
                    # print("e: ",r,c,image[r][c],color)
                    dfs(r,c)
        dfs(sr,sc)
        
        return image