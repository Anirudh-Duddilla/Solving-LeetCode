class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        l, r = 0, 0
        res = 0
        sm = 0
        
        while r < len(s):
            # print(l,r)
            while (r-l) < k:
                if s[r] in vowels:
                    sm += 1
                r += 1
            res = max(res,sm)
            if s[l] in vowels:
                sm -= 1
            l += 1
            
        return res