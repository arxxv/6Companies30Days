import sys


class Solution:
    def getMoneyAmount(self, n):

        def solve(l, r, dp={}):
            if l >= r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            ans = sys.maxsize
            for i in range(l, r+1):
                ans = min(ans, i+max(solve(l, i-1, dp), solve(i+1, r, dp)))

            dp[(l, r)] = ans
            return ans

        return solve(1, n)


print(Solution().getMoneyAmount(10))
