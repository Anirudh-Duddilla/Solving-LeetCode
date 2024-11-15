class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        
        def dfs(room):
            visit.add(room)
            for i in rooms[room]:
                if i not in visit:
                    dfs(i)
                    
        dfs(0)
        
        return len(visit)==len(rooms)