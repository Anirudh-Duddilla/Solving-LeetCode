class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for s in words:
            l, r = 0, len(s) - 1
            while l<=r:
                if l == r:
                    return s
                # print("l",l,f"s[{l}]",s[l],f"s[{r}]",s[r],"r",r,)
                if s[l] != s[r]:
                    break
                l+=1
                r-=1
                
            if l!=r and s[l] == s[r]:
                return s
        return ""
