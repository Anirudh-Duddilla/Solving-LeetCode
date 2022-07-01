class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // if(!nums.size()){return vector<int> result;}
        std::map<int, int> nums_map;    //Creating a map with integers of nums as key and values as number of time they repeated
        for(int i=0; i<nums.size(); i++){
            if(!nums_map.count(nums[i])){
                nums_map[nums[i]] = 1;  
            }
            else{
                nums_map[nums[i]]+=1;
            }
        }
        std::vector<std::pair<int, int>> A;
        
        for(auto &it: nums_map){
            A.push_back(it);
        }
        sort(A.begin(), A.end(), cmp);  //sorting the hash map with the values in descending order and storing each key value as pair of vectors
        std::vector<int> result;
        int j = 0;
        for(auto& it:A){
            if(j>=k){cout << j<<endl;return result;} //iterating through the pair vector until we check for k repeated elements
            cout <<A[j].first<<", ";
            result.push_back(it.first);
            j+=1;
        }
        return result;
    }
    static bool cmp(pair<int,int>& a, pair<int,int>&b){
        return a.second>b.second;
    }
};