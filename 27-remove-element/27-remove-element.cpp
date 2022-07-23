class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if(!nums.size()){return 0;}
        int s = 0, e = nums.size();
        while(s<=e-1){
            if(nums[s] == val && nums[e-1] != val){
                swap(nums[s], nums[e-1]);
                e -= 1;
            }
            else if(nums[e-1] == val){e-=1; continue;}
            s+=1;
        }
        // if(s == 0 && nums[s] == val){return s;}
        return e;
    }
};