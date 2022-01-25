class Solution:
    def maxDistance(self, g):
        n = len(g)
        q = []
        mx = -1
        
        dp = [[-1]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if g[i][j] == 1:
                    q.append((i,j))
                    dp[i][j] = 0
        
        
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        while len(q):
            p = q.pop(0)
            i, j = p[0], p[1]
            for di, dj in d:
                x, y = i+di, j+dj
                if x < 0 or x >= n or y < 0 or y >= n or g[x][y] == 1 or dp[x][y] != -1:
                    continue
                q.append((x,y))
                dp[x][y] = dp[i][j]+1
                mx = max(mx, dp[x][y])
                    
        return mx