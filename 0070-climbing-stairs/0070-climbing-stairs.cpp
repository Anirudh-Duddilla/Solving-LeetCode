class Solution {
public:
    std::array<int, 46> cache;
    int climbStairs(int n) {
        if(cache.size()){
            if(cache[n]>0){return cache[n];}
            if(n < 2){return 1;}
            // else if(n == 1){return 1;}
            else{cache[n] = climbStairs(n-1)+climbStairs(n-2);}
            
        // return 1;
        }
        return cache[n];
    }
};