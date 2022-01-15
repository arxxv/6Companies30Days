class Solution:
    def isBridge(self, V, adj, c, d):
        def connected(V, adj):
            
            visited = [False]*V
            def dfs(v):
                if visited[v] == True:
                    return
                visited[v] = True
                for i in adj[v]:
                    dfs(i)
            
            before = 0
            for i in range(V):
                if visited[i]:
                    continue
                before += 1
                dfs(i)
            
            if d in adj[c]:
                adj[c].remove(d)
            else: return 0
            if c in adj[d]:
                adj[d].remove(c)
            else: return 0
            
            after = 0
            
            visited = [False]*V
            for i in range(V):
                if visited[i]:
                    continue
                after += 1
                dfs(i)
            
            return 1 if before != after else 0
            
        return connected(V, adj)