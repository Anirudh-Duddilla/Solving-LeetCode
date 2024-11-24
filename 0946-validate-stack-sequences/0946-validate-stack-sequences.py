class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        l = 0
        
        for n in pushed:
            s.append(n)
            while l < len(popped) and s and popped[l] == s[-1]:
                s.pop()
                l+=1
        
        return not s