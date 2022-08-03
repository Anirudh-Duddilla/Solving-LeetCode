class Solution {
public:
    int divisorSubstrings(int num, int k) {
        string s = to_string(num);
        int l = 0, r = 0;
        int div = 0;
        int k_num = 0;
        while(r < s.size()){
            if(r <= k-1){
                // cout << "s[r]"<<s[r]<<endl;
                k_num = k_num + ((s[r] - '0')*pow(10,(k-r-1)));
                cout << "k_num " << k_num << endl;
                cout << "r " << r <<endl;
                if(num%k_num == 0 && r-l == k-1){cout << "if " << endl;div+=1;}
                r+=1;
                continue;
            }
            // r+=1;
            cout <<"r " << r <<endl;
            k_num  = ((k_num*10) + (s[r] - '0'));
            cout << "k_num " << k_num << endl;
            k_num = k_num % lround(pow(10,k));            
            cout << "k_num " << k_num << endl;
            // cout <<"r " << r <<endl;
            if(k_num !=0 && num%k_num == 0){cout << "entrd"<<endl;div+=1;}
            r += 1;
            l += 1;
        }
        return div;
    }
};