class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t = "balloon"
        t_map = {}
        s_map = {}
        for c in t:
            t_map[c] = t_map.get(c,0)
            s_map[c] = s_map.get(c,0) + 1
        r = 0
        while r < len(text):
            if text[r] in t_map.keys():
                t_map[text[r]] += 1
            r+=1
        
        if 0 in t_map.values():return 0
        else:
            cnt = inf
            for key, val in t_map.items():
                cnt = min(cnt,t_map[key]//s_map[key])
                
        return cnt