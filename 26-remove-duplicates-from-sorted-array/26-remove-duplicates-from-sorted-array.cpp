class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if( !nums.size()){return 0;}
        int l = 0, r = l;
        for(int i = 0; i < nums.size(); i++){
            r = i;
            if(nums[l] != nums[r]){
                swap(nums[l+1], nums[r]);
                l+=1;
            }
            // cout << l << " " << r << endl;
        }
        return l+1;
    }
};