class Solution {
public:
    
    bool iss(string s){
            char c = s[0];
            if(c == '+' || c == 'D' || c == 'C'){
                return true;
            }
            return false;
        }
    int calPoints(vector<string>& operations) {
        stack<int> stk;
        int lst = 0;
        int lstbt1 = 0;
        int sum = 0;
        int tot_sum = 0;
        
        for(int i=0;i<operations.size();i++){
            char c = operations[i][0];
            if(iss(operations[i])){
                if(c == '+'){
                    cout <<"entrd +"<<endl;
                    lst = stk.top();
                    stk.pop();
                    lstbt1 = stk.top();
                    // stk.pop();
                    stk.push(lst);
                    sum = sum + lst + lstbt1;
                    cout << "sum "<<sum<<endl;
                    cout << stk.top() <<endl;
                    stk.push(lst+lstbt1);
                    cout << stk.top() <<endl;                    
                }
                else if(c == 'D'){
                    cout <<"entrd D"<<endl;
                    lst = stk.top();
                    // stk.pop();
                    sum = sum + (2*lst);
                    cout << "sum "<<sum<<endl;
                    stk.push(2*lst);
                    cout << stk.top() <<endl;
                }
                else{
                    cout <<"entrd C"<<endl;
                    lst = stk.top();
                    sum = sum - lst;
                    cout << "sum "<<sum<<endl;
                    stk.pop();
                    // cout << stk.top() <<endl;
                }
            }
            else{
                lst = std::stoi(operations[i]);
                sum+=lst;
                cout << "sum "<<sum<<endl;
                stk.push(lst);
                cout << stk.top() <<endl;
            }
        }
        return sum;
    }
};