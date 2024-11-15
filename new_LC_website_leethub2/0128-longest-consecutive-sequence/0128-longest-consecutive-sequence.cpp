class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set< int> arr_set(begin(nums), end(nums));
        int longest = 0;
        for(int i = 0; i<nums.size(); i++){
            if(!arr_set.count(nums[i]-1)){
                int length = 0;
                while(arr_set.count(nums[i] + length)){
                    length+=1;
                }
                longest = max(longest, length);
            }
        }
        return longest;
    }
};