class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        visit = set()
        nums = [i for i in range(0, n)]
        sz = [0] * n
        l, r = 0, 0
        def find(num):
            while num != nums[num]:
                # print("f",num, nums[num], nums,sz)
                num = nums[num]
            return num
        
        def union(a, b):
            nonlocal l,r
            # print("a",a,"b",b)
            i = find(a)
            j = find(b)
            # print("i",i,"j",j)
            # print("u","a",a,"i",i,"b",b,"j",j,nums)
            if i == j:
                # nums[a] = nums[b]
                # print(a,i,b,j)
                r += 1
                return
            
            # if sz[i] < sz[j]:
            #     print("e", i,j,sz[i],sz[j])
            #     i, j = j, i
            #     l+=1
            # print("as","a",a,"i",i,"b",b,"j",j,nums)
             
            sz[i] += 1
            nums[i] = j
            l += 1
            # print("s","a",a,"i",i,"b",b,"j",j,nums,sz)
            return

        for a,b in connections:
            union(a,b)
        
        print(l,r,n-l-1)
        if r < n-l-1:
            return -1
        elif r > n-l-1:
            return n-l-1
        else:
            return r
         
        return -1