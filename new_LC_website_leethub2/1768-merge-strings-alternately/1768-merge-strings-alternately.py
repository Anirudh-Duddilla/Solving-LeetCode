class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 1
        for c in word2:
            # print(c, word1, i, word1[:i], word1[i:])
            word1 = word1[:i] + c + word1[i:]
            
            i+=2
        return word1