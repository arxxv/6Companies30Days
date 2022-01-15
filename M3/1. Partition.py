import sys
class Solution:
    def findMin(a, n):
        sumx = sum(a)
        dp = [[0 for i in range(sumx + 1)] for j in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for j in range(1, sumx + 1):
            dp[0][j] = False

        for i in range(1, n + 1):
            for j in range(1, sumx + 1):
                dp[i][j] = dp[i - 1][j]
                if a[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - a[i - 1]]

        diff = sys.maxsize

        for j in range(sumx // 2, -1, -1):
            if dp[n][j] == True:
                diff = sumx - (2 * j)
                break
        return diff

n = int(input())
arr = list(map(int, input().split()))
print(Solution.findMin(arr, n))


