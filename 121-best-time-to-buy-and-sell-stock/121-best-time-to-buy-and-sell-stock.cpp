class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min, max;
        int dif = 0;
        min = max = prices[0];
        for(int i=1; i<prices.size(); i++){
            max = std::max(max,prices[i]);
            if(prices[i] < min){
                min = max = prices[i];
            }
            dif = std::max(dif,(max-min));
        }
        return dif;
    }
};