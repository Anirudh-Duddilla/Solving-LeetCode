class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sp, tp = 0, 0
        while tp < len(t) and sp < len(s):
            if s[sp] != t[tp]:
                sp += 1
            else:
                tp += 1
                sp += 1

        # s += t[tp:]
        # print(s)

        return len(t) - tp