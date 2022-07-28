class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int l = 0, r = l;
        double sum = 0;
        double avg = sum/k;
        for(int i = 0; i < nums.size(); i++){
            if(r < k){
                // cout << "l " << l << " r " <<r<<endl;
                sum += nums[i];
                // cout << "fs " << sum << endl;
                avg = sum/k;
                r+=1;
                continue;
            }
            l += 1;
            // cout << "l " << l << " r " <<r<<endl;
            sum = sum - nums[l-1] + nums[r];
            r += 1; 
            // cout << "ns " << sum << endl;
            avg = std::max(avg, sum/k);
        }
        return avg;
    }
};