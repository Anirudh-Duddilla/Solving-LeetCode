class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int l = 0, r = l;
        double sum = 0, avg = sum/k;
        while(r < nums.size()){
            if(r < k){
                sum += nums[r];
                avg = sum/k;
                r+=1;
                continue;
            }
            l += 1;
            sum = sum - nums[l-1] + nums[r];
            r += 1; 
            avg = std::max(avg, sum/k);
        }
        return avg;
    }
};