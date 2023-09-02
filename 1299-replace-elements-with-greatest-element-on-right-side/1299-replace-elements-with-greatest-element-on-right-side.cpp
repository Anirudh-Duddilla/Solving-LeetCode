class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int length = arr.size()-1;
        int high = arr[length];
        arr[length] = -1;
        int temp = 0;
        for(int i = length-1; i >-1; i--){
            if(high < arr[i]){
                temp = high;
                high = arr[i];
                arr[i] = temp;
                continue;
            }
            arr[i] = high;
        }
        return arr;
    }
};