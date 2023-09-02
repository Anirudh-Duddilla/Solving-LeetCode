class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0;
        int r = s.size()-1;
        char c;
        while(l<r){
            c = s[r];
            s[r] = s[l];
            s[l] = c;
            l += 1;
            r -= 1;
        }
    }
};