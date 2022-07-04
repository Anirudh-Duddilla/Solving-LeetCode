class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(),1);
        int prefix = 1;
        for(int i=0; i<nums.size(); i++){
            result[i] = prefix;
            prefix*=nums[i];
        }
        int postfix = 1;
        for(int j = nums.size()-1; j>=0;j--){
            
            result[j] *= postfix;
            postfix*=nums[j];
        }
        return result;
    }
};