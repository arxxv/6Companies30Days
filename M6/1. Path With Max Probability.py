from collections import defaultdict
import heapq


class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        p, g = [0.0] * n, defaultdict(list)
        for index, (a, b) in enumerate(edges):
            g[a].append((b, index))
            g[b].append((a, index))
        p[start] = 1.0
        heap = [(-p[start], start)]
        while heap:
            prob, cur = heapq.heappop(heap)
            if cur == end:
                return -prob
            for neighbor, index in g.get(cur, []):
                if -prob * succProb[index] > p[neighbor]:
                    p[neighbor] = -prob * succProb[index]
                    heapq.heappush(heap, (-p[neighbor], neighbor))
        return 0.0


print(Solution().maxProbability(
    3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
