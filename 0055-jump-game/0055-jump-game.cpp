class Solution {
public:
    bool canJump(vector<int>& nums) {
        int i = 0;
        int j = 0;
        int m = 0;
        while(i <= m){
            if(m >= nums.size()-1){return true;}
            j = std::max(nums[i], nums[m]);
            m = std::max(m, i+j);
            i++;
        }
        return false;
    }
};