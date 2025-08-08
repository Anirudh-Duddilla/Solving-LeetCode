class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visit = set()

        # Get the starting color
        start_color = image[sr][sc]

        # If the start color is the same as the target color, no need to do anything
        if start_color == color:
            return image
        
        def dfs(row, col):
            # If the cell is out of bounds or already visited, return
            if (row, col) in visit:
                return
            visit.add((row, col))

            # Change the color of the current cell
            image[row][col] = color

            # Define 4 possible directions (right, left, down, up)
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in dirs:
                r, c = row + dr, col + dc
                # Continue DFS if within bounds and the cell has the same color as the start color
                if 0 <= r < rows and 0 <= c < cols and image[r][c] == start_color:
                    dfs(r, c)

        # Start DFS from the initial pixel
        dfs(sr, sc)

        return image
