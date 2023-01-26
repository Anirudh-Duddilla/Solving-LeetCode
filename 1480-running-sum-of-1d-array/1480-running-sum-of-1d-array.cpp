class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> running_sum;
        int sum = 0;
        for(int i=0; i<nums.size();i++){
            sum += nums[i];
            running_sum.push_back(sum);
        }
        return running_sum;
    }
};