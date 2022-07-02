class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min, max;
        int dif = 0;
        min = max = prices[0];
        for(int i=1; i<prices.size(); i++){
            if(prices[i] > max){
                max = prices[i];
            }
            else if(prices[i] < min){
                min = max = prices[i];
            }
            if(dif < (max-min)){
                dif = max - min;
            }
        }
        return dif;
    }
};