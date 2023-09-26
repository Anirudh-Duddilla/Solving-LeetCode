class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int l = 0;
        int r = 0;
        int s = 0;
        int res = 0;
        while(r<arr.size()){
            // cout <<"s "<<s<<" r "<<r<<endl;
            while((r-l)<k){
                s+=arr[r];
                // cout <<"s "<<s<<" r "<<r<<endl;
                r+=1;
            }
            if(s>=k*threshold){
                // cout<<"entrd"<<endl;
                res+=1;
            }
            s-=arr[l];
            l+=1;
            // cout <<"s "<<s<<" l "<<l<<" r "<<r<<endl;
            // r+=1;
        }
        return res;
    }
};