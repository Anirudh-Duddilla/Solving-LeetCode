class Solution {
public:
    int rob(vector<int>& nums) {
        int curr = 0;
        int prev = 0;
        int next = 0;
        int sz = nums.size();
        
        for(int i=0; i<nums.size()-1;i++){
            next = std::max(prev + nums[i], curr);
            prev = curr;
            curr = next;
        }
        int rob1 = curr;
        prev = 0;
        curr = 0;
        next = 0;
        for(int i=1; i<nums.size();i++){
            next = std::max(prev + nums[i], curr);
            prev = curr;
            curr = next;
        }
        int rob2 = curr;
        
        return std::max(nums[0],std::max(rob1,rob2));
    }
};