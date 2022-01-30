import heapq


class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        l = sorted(list(zip(efficiency, speed)), reverse=True)
        res, mod, h, mx_sum = 0, 1e9+7, [], 0
        for i in range(n):
            res = max(res, (mx_sum+l[i][1])*l[i][0])
            if len(h) < k-1:
                heapq.heappush(h, l[i][1])
                mx_sum += l[i][1]
            elif k != 1:
                x = 0
                if h:
                    x = heapq.heappop(h)
                heapq.heappush(h, max(x, l[i][1]))
                mx_sum = mx_sum - x + max(x, l[i][1])
        return int(res % mod)
