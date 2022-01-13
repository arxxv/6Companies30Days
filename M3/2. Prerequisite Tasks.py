class ans:
    def isPossible(self, N, prerequisites):
        graph = [[] for _ in range(N)]
        visited = [0 for _ in range(N)]
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
            
        for i in range(N):
            if not dfs(i):
                return False
        return True