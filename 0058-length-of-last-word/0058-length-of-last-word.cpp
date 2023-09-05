class Solution {
public:
    int lengthOfLastWord(string s) {
        int cnt = 0;
        int res = cnt;
        for(char c:s){
            if(c == '/0'){
                break;
            }
            else if(c == ' '){
                cnt  = 0;
                
                continue;
            }
            cnt +=1;
            res = cnt;
        }
        return res;
    }
};