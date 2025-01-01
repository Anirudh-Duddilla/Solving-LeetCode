class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        res = ""

        for i in range(len(s)):
            j,k = i,i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if (k-j+1) > reslen:
                    res = s[j:k+1]
                    reslen = k-j+1
                j-=1
                k+=1
            j,k = i,i+1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if (k-j+1) > reslen:
                    res = s[j:k+1]
                    reslen = k-j+1
                j-=1
                k+=1

        return res
