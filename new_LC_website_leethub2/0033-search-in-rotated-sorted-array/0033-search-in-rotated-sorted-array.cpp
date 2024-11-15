class Solution {
public:
    int search(vector<int>& nums, int target) {
        int fst = 0;
        int lst = nums.size() - 1;

        while(fst <= lst){
            int mid = (lst + fst)/2;
            if(nums[mid] == target){return mid;}
            if(nums[fst] <= nums[mid]){
                if (nums[mid] < target  || nums[fst] > target){
                    fst = mid + 1;
                }
                else{
                    lst = mid -1;

                }
            }
            else{
                if (nums[mid] > target  || nums[lst] < target){
                    lst = mid - 1;
                }
                else{
                    fst = mid + 1;
                }
            }
        }
        return -1;
    }
};