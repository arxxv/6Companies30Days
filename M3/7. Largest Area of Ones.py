class Solution:
    def findMaxArea(self, G):
        n, m = len(G), len(G[0])
        moves = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
        visited = [[False for i in range(m)] for j in range(n)]
        def fun(i, j, c):
            visited[i][j] = True
            for mv in moves:
                x, y = i+mv[0], j+mv[1]
                if x >= 0 and y >= 0 and x < n and y < m and G[x][y] and not visited[x][y]:
                    c[0]+=1
                    fun(x, y, c)
        
        ans = -1
        for i in range(n):
            for j in range(m):
                if G[i][j] and not visited[i][j]:
                    c = [1]
                    fun(i, j, c)
                    ans = max(ans, c[0])
        return ans

print(Solution().findMaxArea([[0, 0, 1, 1, 0],[1, 0, 1, 1, 0],[0, 1, 0, 0, 0],[0, 0, 0, 0, 1]]))