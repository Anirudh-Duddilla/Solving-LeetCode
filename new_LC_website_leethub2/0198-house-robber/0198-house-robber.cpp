class Solution {
public:
    int rob(vector<int>& nums) {
        
        int curr = 0;
        int prev = 0;
        int next = 0;
        
        for(int i=0; i<nums.size();i++){
            next = std::max(prev + nums[i], curr);
            prev = curr;
            curr = next;
        }
        return curr;
    }
};