class Solution {
public:
    int characterReplacement(string s, int k) {
        int l=0, r=0, maxf = 0;
        int win_len = 0, res = 0;;
        std::map<char, int> char_map;
        while(r<s.size()){
            // cout << win_len <<" " << maxf<<" " << res<<" "<<l<<" "<<r<<endl;
            if(!char_map.contains(s[r])){
                char_map[s[r]] = 0;
            }
            // else{
            char_map[s[r]] +=1 ;
            win_len = r-l+1;
            std::map<char, int>::iterator it  = char_map.begin(); 
            while(it != char_map.end()){
                // cout<<it->second<<endl;
                if(maxf < it->second){
                    maxf = it->second;
                }
                it++;
            }
            // cout<< win_len<<" "<<maxf<<endl;
            if((win_len - maxf) > k){
                char_map[s[l]] -= 1;
                l+=1;
                maxf = 0;
                // continue;
            }
                // else{l+=1;}
            // }
            // cout<<win_len<<" "<< maxf<<" "<<s[r]<<" "<<char_map[s[r]]<<" "<<l<<" "<<r<<endl;
            res = std::max(res, r-l+1);
            r+=1;            
        }
        // res = r-l;
        return res;
    }
};