class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        l = 0
        
        while l < len(asteroids):
            # print(l, s, asteroids[l])
            if s and asteroids[l] < 0 and s[-1] > 0:
                if s[-1] < -asteroids[l]:
                    s.pop()
                elif s[-1] == -asteroids[l]:
                    s.pop()
                    l += 1
                    continue
                else:
                    l+=1
                    continue
            else:
                s.append(asteroids[l])
                l += 1
                
        return s