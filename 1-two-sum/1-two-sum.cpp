class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map< int, int>omap;
        int i =0;
        for(i; i<nums.size(); i++){
            if(omap.count(target-nums[i])){
                return vector<int> {omap[target-nums[i]], i};
            }
            else{
                omap[nums[i]] = i;
            }
        }
        return vector<int> {omap[target-nums[i]], i};
    }
};