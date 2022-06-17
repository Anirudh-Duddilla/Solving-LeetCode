class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()){
            return -1;
        }
        int length = nums.size();
        int first = 0;
        int last = length;
        cout << first << ' ' << last<<endl;
        int mid;
        while(last > first){
            mid = (last + first)/2;
            if(nums[mid] == target){
                cout << "mid"<<mid<< endl;
                return mid;
            }
            else if(nums.at(mid) > target){
                last = mid; 
                cout << "l" <<last<<endl;
            }
            else{
                first = mid+1;
                cout << "f"<<first << endl;
            }
        }
        return -1;
    }
};