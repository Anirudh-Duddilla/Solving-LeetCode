class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if(!m){nums1 = nums2; n = -1;}
        int l = m+n - 1;
        while(n>0 ){
            if(nums1[m-1] <= nums2[n-1]){
                nums1[l] = nums2[n-1];
                n-=1;
            }
            else{
                nums1[l] = nums1[m-1];
                nums1[m-1] = nums2[n-1];   
                if(m == 1){n-=1;l-=1;continue;}
                m-=1;
            }
            l-=1;
        }
    }
};