class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size()-1;
        vector<int>v;
        while(l<r){
            int cursum = numbers[l]+numbers[r];
            // cout <<"l "<< l<<" r " << r << " cursum "<<cursum<<endl;
            if(cursum == target){ v={l+1,r+1};break; }
            else if(cursum>target){r-=1;}
            else{l+=1;}
        }
        return v;
    }
};