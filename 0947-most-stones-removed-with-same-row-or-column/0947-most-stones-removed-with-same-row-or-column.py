class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = [i for i in range(len(stones))]
        rank = [i for i in range(len(stones))]
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(x,y):
            a = find(x)
            b = find(y)
            if a == b:
                return 0
            if a != b:
                if rank[a] < rank[b]:
                    a, b = b, a
            rank[a] += rank[b]
            parent[b] = parent[a]
            return 1
            
        X = {}
        Y = {}
        count = 0
        for i, (x,y) in enumerate(stones):
            if x in X:
                count += union(i,X[x])
            else:
                X[x] = i
            if y in Y:
                count += union(i,Y[y])
            else:
                Y[y] = i
                
        return count
            