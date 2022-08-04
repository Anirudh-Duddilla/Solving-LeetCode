class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::map<int, int> id_map;
        int p = 0;
        while(p < nums.size()){
            if(!id_map.count(nums[p])){id_map[nums[p]] = p;}
            // cout << "p " <<p << endl;
            // cout << "m_val " << id_map[nums[p]]<<endl;
            // cout << (0 < abs(id_map[nums[p]] - p) && abs(id_map[nums[p]] - p) <= k) << endl;
            if(0 < abs(id_map[nums[p]] - p) && abs(id_map[nums[p]] - p) <= k){
                return true;
            }
            else{
                // cout << "dif " << abs(id_map[nums[p]] - p) << endl;
                // cout << "m_key " << nums[p] << endl;
                // cout << "m_val " << id_map[nums[p]]<<endl;
                id_map[nums[p]] = p;
            }
            p += 1;
        }
        return false;
    }
};