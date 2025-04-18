class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)

        for a, b in prerequisites:
            adj_list[a].append(b)

        def dfs(i):
            if i in rec_stack:
                return False
            if i in visited:
                return  True

            rec_stack.add(i)
            for c in adj_list[i]:
                if not dfs(c):
                    return False
            
            rec_stack.remove(i)
            visited.append(i)

            return True

        visited = []
        rec_stack = set()
        for key in range(numCourses):
            if not dfs(key):
                return []

        return visited