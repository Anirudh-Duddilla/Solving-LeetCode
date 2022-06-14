class Solution {
public:
    bool isValid(string s) {
        std :: stack < char > stk;
        for( char c:s){
            if( (c == ')' || c == ']' || c == '}') && stk.empty()){
                return false;
            }
            else{
                switch(c){
                    case '}':
                        if(stk.top() != '{'){return false;}
                        else{stk.pop(); continue;}
                    case ')':
                        if(stk.top() != '('){return false;}
                        else{stk.pop(); continue;}
                    case ']':
                        if(stk.top() != '['){return false;}
                        else{stk.pop(); continue;}
                }
            }
            stk.push(c);
        }
        return stk.empty();
    }
};