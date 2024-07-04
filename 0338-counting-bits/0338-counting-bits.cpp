class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> ans;
        int comp=0;
        for(int i =0; i<n+1;i++){
            if(i==0){
                ans.push_back(i);
                continue;
            }
            if((i & (i - 1)) == 0){
                comp = i;
                ans.push_back(1);
            }
            else{
                ans.push_back(1+ans[i-comp]);
            }
        }
        
        return ans;
    }
};