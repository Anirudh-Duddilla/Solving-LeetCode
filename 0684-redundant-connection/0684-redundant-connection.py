class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        arr = [i for i in range(len(edges)+1)]
        sz = [1]*(len(edges)+1)
        res = []
        # print(arr, sz)        
        
        def find(x):
            # print(x, arr[x])
            while x != arr[x]:
                x = arr[x]
            return x
                
        def same(a,b):
            return find(a) == find(b)
            
        def unite(a,b):
            nonlocal res
            # print(a,b)
            i = find(a)
            j = find(b)
            # print(same(i,j))
            if same(i,j): res = [i,j]
            # print(i,j,arr,sz)
            # if same(i,j):return [i,j]
            if sz[i] <= sz[j]:
                i, j = j, i
            sz[i]+=1
            arr[i] = j
        
        for i, j in edges:
            unite(i,j)
            if res: return [i,j]

        return res