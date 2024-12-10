class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def dfs(openn,close):
            # print(openn,close,stack)
            if openn == close == n:
                res.append("".join(stack))
                return
            if openn<n:
                stack.append("(")
                dfs(openn+1,close)
                # print("o",stack)
                stack.pop()
                # print("o",stack)
            if close < openn:
                stack.append(")")
                dfs(openn,close+1)
                # print("c",stack)
                stack.pop()
                # print("c",stack)

        dfs(0,0)       
        
        return res