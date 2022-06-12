class Solution {
public:
    bool isPalindrome(string s) {
        int l = s.length();
        int b = 0, e = l-1;
        
        while(b < e){
            
            if(isupper(s[b]) || isupper(s[e])){
                s[b] = tolower(s[b]);
                s[e] = tolower(s[e]);
                continue;
            }
            else if( !isalnum(s[b])){
                // cout << "entered"<<"\n";
                
                b++;
                continue;
            }
            else if( !isalnum(s[e])){
                // cout << "entered"<<"\n";
                e--;
                continue;
            }
            
            if(s[b] != s[e]){return false;}

            b++;
            e--;
            
        }
        return true;
    }
};