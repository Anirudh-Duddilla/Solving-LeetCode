class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        reverse(digits.begin(), digits.end());
        int co = 1;
        int i = 0;
        while(co){
            if (i<digits.size()){
                if(digits[i] == 9){
                    digits[i] = 0;
                }
                else{
                    digits[i] += 1;
                    co = 0;
                }
            }
            else{
                digits.push_back(1);
                co = 0;
            }
            i+=1;
        }
        reverse(digits.begin(), digits.end());
        return digits;
    }
};