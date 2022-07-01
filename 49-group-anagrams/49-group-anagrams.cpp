class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // cout <<strs[0].size();
        std::map<string, vector<string>> score_map = score(strs);
        vector<vector<string>> result;
        for(const auto &[key, value]: score_map){
            result.push_back(score_map[key]);
        }
        return result;
    }
    std::map<string, vector<string>> score(vector<string>& strs){
        std::map<string, vector<string>> score_map;
        for(string s: strs){
            string temp = s;
            sort(s.begin(),s.end());
            score_map[s].push_back(temp);            
        }
        return score_map;
    }
};