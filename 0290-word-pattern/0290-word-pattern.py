class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        s_map = {}
        p_map = {}
        # pats = pattern.split("")
        for i, word in enumerate(words):
            if not s_map.get(word,None) and not p_map.get(pattern[i],None):
                s_map[word] = pattern[i]
                p_map[pattern[i]] = word
            elif s_map.get(word,None) and p_map.get(pattern[i],None):
                if s_map[word] != pattern[i]:
                    return False
            else:
                return False
    
        # print(s_map,p_map)
        
        return True