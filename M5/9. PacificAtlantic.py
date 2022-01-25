class Solution(object):
    def pacificAtlantic(self, matrix):

        def dfs(matrix, i, j, visited, n, m):
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited[i][j] = True
            for dir in moves:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or matrix[x][y] < matrix[i][j]:
                    continue
                dfs(matrix, x, y, visited, n, m)

        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])

        pac = [[False]*m for _ in range(n)]
        atl = [[False]*m for _ in range(n)]

        ans = []

        for i in range(n):
            dfs(matrix, i, 0, pac, n, m)
            dfs(matrix, i, m-1, atl, n, m)
        for j in range(m):
            dfs(matrix, 0, j, pac, n, m)
            dfs(matrix, n-1, j, atl, n, m)

        for i in range(n):
            for j in range(m):
                if pac[i][j] and atl[i][j]:
                    ans.append([i, j])
        return ans
