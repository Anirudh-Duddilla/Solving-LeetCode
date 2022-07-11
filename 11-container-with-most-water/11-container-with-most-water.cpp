class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, t = l+1, r = height.size() - 1;
        int result = 0;          
        while(l <= r){
            // cout << "l: "<<height[l]<<" t: "<<height[t]<<" r: "<<height[r]<<endl;
            int ara = area(height[l], r-l, height[r]);
            result = max(result, ara);
            if(height[l] < height[r]){l+=1;}
            else{r-=1;}
        }
        return result;
    }
    
    int area(int first, int length, int last){
        int prod = length * min(first, last);
        // cout << "prod: "<<prod<<endl;
        return prod;
    }
};