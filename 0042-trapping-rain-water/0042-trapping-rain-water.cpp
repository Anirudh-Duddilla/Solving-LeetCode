class Solution {
public:
    int trap(vector<int>& height) {
        int lft = 0;
        int rht = height.size()-1;
        int max_lft = height[lft];
        int max_rht = height[rht];
        int tot_sum = 0;
        while(lft <rht){
            if(max_lft < max_rht){
                lft += 1;
                max_lft = max(max_lft, height[lft]);
                tot_sum += max_lft - height[lft];
            }
            else{
                rht -= 1;
                max_rht = max(max_rht, height[rht]);
                tot_sum += max_rht -height[rht];
            }
            
        }
        return tot_sum;
    }
};