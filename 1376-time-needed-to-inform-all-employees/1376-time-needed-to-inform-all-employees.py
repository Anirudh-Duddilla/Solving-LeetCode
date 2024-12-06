class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        res = 0
        for i in range(0,n):
            adj[manager[i]].append(i)
                
        q = deque()
        q.append((headID,0))

        while q:
            node, time = q.popleft()
            res = max(res, time)
            for emp in adj[node]:
                q.append((emp, time+informTime[node]))
            
        return res