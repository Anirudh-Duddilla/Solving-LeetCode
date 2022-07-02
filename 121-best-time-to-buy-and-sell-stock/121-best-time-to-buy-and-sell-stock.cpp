class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min = prices[0];
        int dif = 0;
        // min = max = prices[0];
        for(int i=1; i<prices.size(); i++){
            // max = std::max(max,prices[i]);
            min = std::min(min,prices[i]);
            dif = std::max(dif,(prices[i]-min));
        }
        return dif;
    }
};