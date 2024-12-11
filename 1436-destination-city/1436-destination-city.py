class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # adj = defaultdict(list)
        fromset = set()
        toset = set()
        for i, j in paths:
            fromset.add(i)
            toset.add(j)
            
        newset = toset.difference(fromset)
        
        print(fromset)
        print(toset)
        print(newset, newset.difference(fromset).pop())
        return newset.difference(fromset).pop()
#             # print(i,j)
#             if adj.get(i,[]) == []:
#                 adj[i].append(j)
#             else:
#                 adj[i].append(j)
        
#         visit = set()
#         s = set(adj.keys())
        
#         for i in adj:
#             visit.add(adj[i])
            
            
        # print(adj)