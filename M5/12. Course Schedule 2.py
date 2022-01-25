from collections import defaultdict
from collections import deque


class Solution:
    def findOrder(self, n, C):
        graph = defaultdict(list)
        for u, v in C:
            graph[v].append(u)

        deg = [0]*n

        for i in range(n):
            for e in graph[i]:
                deg[e] += 1

        q = deque([])
        for i in range(n):
            if deg[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for i in graph[node]:
                deg[i] -= 1
                if deg[i] == 0:
                    q.append(i)
        if len(res) == n:
            return res
        return []
