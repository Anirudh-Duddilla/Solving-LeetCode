class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if(!m){nums1 = nums2; n = -1;}
        int l = m+n - 1;
        // m -=1;n-=1;
        while(n>0 ){
            // cout << "m: " << nums1[m-1]<< " n: " << nums2[n-1]<< " l: " << nums1[l] << endl;
            // cout << nums1[l]<<endl;
            if(nums1[m-1] <= nums2[n-1]){
                cout <<"entrd if"<<endl;
                nums1[l] = nums2[n-1];
                cout << "m: " << nums1[m-1]<< " n: " << nums2[n-1]<< " l: " << nums1[l] << endl;
                n-=1;
            }
            else{
                cout <<"entrd el"<<endl;
                nums1[l] = nums1[m-1];
                nums1[m-1] = nums2[n-1];   
                cout << "m: " << nums1[m-1]<< " n: " << nums2[n-1]<< " l: " << nums1[l] << endl;
                if(m == 1){n-=1;l-=1;continue;}
                m-=1;
                // n-=1;

            }
            l-=1;
        }
    }
};