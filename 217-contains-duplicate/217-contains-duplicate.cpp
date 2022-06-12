class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std :: unordered_map < int, int > map;
        int counter = 0;
        for(int i =0; i<nums.size(); i++){
            // cout << nums[i] <<": "<<map.count(nums[i])<< " ";
            
            if (map.count(nums[i]) == 0){
                // cout << 'e'<<std::endl;
                map[nums[i]] = counter+1;
            }
            else{
                map[nums[i]] += 1;
            }
            if (map[nums[i]] > 1){ return true;}
            // cout << map[nums[i]]<<std::endl;
        }
        return false;
    }
};