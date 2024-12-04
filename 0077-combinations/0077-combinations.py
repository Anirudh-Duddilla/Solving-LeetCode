class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(i, s):
            # If the combination is of size k, add it to the result
            if len(s) == k:
                res.append(s[:])  # Append a copy of the current combination
                return
            # If we've used all elements or reached the limit, stop recursion
            if i > n:
                return
            # Include the current number and recurse with the next number
            s.append(i)
            dfs(i + 1, s)
            s.pop()  # Backtrack, remove the last number
            # Do not include the current number and recurse with the next number
            dfs(i + 1, s)
        # Start DFS from number 1
        dfs(1, [])
        return res