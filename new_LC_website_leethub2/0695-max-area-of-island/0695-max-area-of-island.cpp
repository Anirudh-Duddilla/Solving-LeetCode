class Solution {
public:
    int area = 0;
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        
        int result = 0;
        int Ar = 0;
        for (int i = 0; i < m; i++) {
            int n = grid[i].size();
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    cout << "Grid["<<i<<"]["<<j<<"] "<<grid[i][j] << endl;
                    area = dfs(grid, i, j, m, n);
                    result++;
                }
                // cout << Ar << " "<<area << " "<<result<<endl;
                Ar = std::max(area,Ar);
                area = 0;
            }
        }
        
        return Ar;
    }
private:
    int dfs(vector<vector<int>>& grid, int i, int j, int m, int n) {
        
        // cout << area << " "<<i <<" "<< j <<endl;
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0) {
            return area;
        }
        area++;
        grid[i][j] = 0;
        
        dfs(grid, i - 1, j, m, n);
        dfs(grid, i + 1, j, m, n);
        dfs(grid, i, j - 1, m, n);
        dfs(grid, i, j + 1, m, n);
        
        return area;
    }
};