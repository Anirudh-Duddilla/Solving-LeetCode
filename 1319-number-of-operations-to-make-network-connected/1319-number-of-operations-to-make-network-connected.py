class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        visit = set()
        nums = [i for i in range(0, n)]
        sz = [0] * n
        l, r = 0, 0
        def find(num):
            while num != nums[num]:
                num = nums[num]
            return num
        
        def union(a, b):
            nonlocal l,r
            i = find(a)
            j = find(b)
            if i == j:
                r += 1
                return
            sz[i] += 1
            nums[i] = j
            l += 1
            return

        for a,b in connections:
            union(a,b)
        
        if r < n-l-1:
            return -1
        elif r > n-l-1:
            return n-l-1
        else:
            return r
