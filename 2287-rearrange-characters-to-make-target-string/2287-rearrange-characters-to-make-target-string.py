class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        t_map = {}
        s_map = {}
        for c in target:
            t_map[c] = t_map.get(c,0)
            s_map[c] = s_map.get(c,0) + 1
        
        for c in s:
            if c in t_map.keys():
                t_map[c] += 1
        
        if 0 in t_map.values():return 0
        else:
            cnt = inf
            for key, val in t_map.items():
                cnt = min(cnt,t_map[key]//s_map[key])
                
        return cnt