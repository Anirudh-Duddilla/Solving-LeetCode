class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::map<int, int> id_map;
        int p = 0;
        while(p < nums.size()){
            if(!id_map.count(nums[p])){id_map[nums[p]] = p;}
            if(0 < abs(id_map[nums[p]] - p) && abs(id_map[nums[p]] - p) <= k){
                return true;
            }
            else{
                id_map[nums[p]] = p;
                p += 1;
            }
        }
        return false;
    }
};