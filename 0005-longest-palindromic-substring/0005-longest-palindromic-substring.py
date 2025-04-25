class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""


        def trav(i,j):
            while i >=0 and j < len(s) and s[i] == s[j]:
                i, j = i-1, j+1
            # print(s[i+1:j])
            return s[i+1:j]

        longest = ""
        for i in range(0,len(s)):
            odd = trav(i,i)
            if len(odd) > len(longest):
                longest = odd

        # for i in range(0,len(s)):
            even = trav(i, i+1)
            if len(even) > len(longest):
                longest = even

            

        return longest