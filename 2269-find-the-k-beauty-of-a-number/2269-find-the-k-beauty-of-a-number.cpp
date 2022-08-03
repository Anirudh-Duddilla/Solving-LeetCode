class Solution {
public:
    int divisorSubstrings(int num, int k) {
        string s = to_string(num);
        int l = 0, r = 0;
        int div = 0;
        int k_num = 0;
        while(r < s.size()){
            if(r <= k-1){
                k_num = k_num + ((s[r] - '0')*pow(10,(k-r-1)));
                if(num%k_num == 0 && r-l == k-1){cout << "if " << endl;div+=1;}
                r+=1;
                continue;
            }
            k_num  = ((k_num*10) + (s[r] - '0'));
            k_num = k_num % lround(pow(10,k));            
            if(k_num !=0 && num%k_num == 0){cout << "entrd"<<endl;div+=1;}
            r += 1;
            l += 1;
        }
        return div;
    }
};