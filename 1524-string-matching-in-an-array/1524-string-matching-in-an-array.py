class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(0, len(words)):
            for j in range(0, len(words)):
                if i == j:
                    continue
                else:
                    if words[i] in words[j] and words[i] not in res:
                        res.append(words[i])

        return res