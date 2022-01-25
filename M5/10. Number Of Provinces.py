class Solution:
    def findCircleNum(self, nodes):
        n = len(nodes)
        vis = [False]*n
        
        def dfs(node):
            vis[node] = True
            for i in range(n):
                if nodes[node][i] and not vis[i]:
                    dfs(i)

        ans = 0
        for i in range(n):
            if not vis[i]:
                ans += 1
                dfs(i)
        return ans
