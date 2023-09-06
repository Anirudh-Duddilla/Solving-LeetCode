class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = 0, r = 1;
        int k = 0; 
        while(r<nums.size()){
            // cout << l << " "<< r<<endl;
            // cout << nums[l]<<" " <<nums[r]<<endl;
            if(nums[l] == nums[r]){
                // cout<<r<<endl;
                r += 1;
            }
            else{
                l+=1;
                nums[l] = nums[r];
                r+=1;
            }
        }
        return l+1;
    }
};