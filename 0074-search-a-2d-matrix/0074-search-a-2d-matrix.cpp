class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size();
        if(row == 0){return false;}
        int col = matrix[0].size();
        cout << "row " << row << "col " << col << endl;
        if(target < matrix[0][0]){return false;}
        else if(target > matrix[row-1][col-1]){return false;}
        else{
            for(int j = 0; j < row ; j++){
                if(target > matrix[j][col-1]){continue;}
                else{
                    int l = 0, r = col - 1;
                    while(l<=r){
                        int mid = (l+r)/2;
                        if (matrix[j][mid] == target){return true;}
                        else if(target <= matrix[j][mid]){
                            r = mid - 1;
                        }
                        else if(target > matrix[j][mid]){
                            l = mid+1 ;

                        }
                        
                    }
                }
            }
        }
        return false;
    }
};