class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        while(l<r):
            if not s[l].isalpha() and not s[l].isdigit():
                l+=1
                continue
            if not s[r].isalpha() and not s[r].isdigit():
                r-=1
                continue
            # print(l," : "+s[l]+"  ",r," : "+s[r])
            if(s[l].lower() != s[r].lower()):
                return False
            # print(l," : "+s[l]+"  ",r," : "+s[r])
            l+=1
            r-=1
        return True
                
        