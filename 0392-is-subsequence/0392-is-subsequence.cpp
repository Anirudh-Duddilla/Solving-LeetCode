class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(s.size() == 0 && t.size()==0){return true;}
        else if(s.size()>0 && t.size() == 0){return false;}
        else if(s.size() == 0 && t.size()>0){return true;}
        if(s.size() > t.size()){
            return false;
        }
        else if(s.size()==t.size()){
            
            for(int i =0;i<s.size();i++){
                // cout << s[i] <<" " <<t[i]<<endl;
                if(s[i]!=t[i]){return false;}
            }
            return true;
        }
        else{
                int i =0;
                for(int j = 0; j<t.size();j++){
                    if(t[j] == s[i]){
                        i = i+1;
                    }
                    if(i == s.size()){ return true;}
                }
        }
        return false;
    }
};