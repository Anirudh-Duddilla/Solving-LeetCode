class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int sz = cost.size();
        for(int i = sz-3; i>-1;i--){
            // cout<<cost[i]<<" " <<cost[i+1]<<" "<<cost[i+2]<<endl;
            cost[i] += std::min(cost[i+1],cost[i+2]);
        }
        return min(cost[0],cost[1]);
    }
};