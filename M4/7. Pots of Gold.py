class Solution:
    def findMaxCoins(self, nums):
        n = len(nums)
        if n <= 2: return max(nums)
        dp = [[0 for x in range(n)] for y in range(n)]
    
        def get(dp, i, j):
            return dp[i][j] if i <= j else 0

        for k in range(n):
            i = 0
            j = k
            while j < n:
                start = nums[i] + min(get(dp, i + 2, j), get(dp, i + 1, j - 1))
                end = nums[j] + min(get(dp, i + 1, j - 1), get(dp, i, j - 2))
                dp[i][j] = max(start, end)
                i = i + 1
                j = j + 1
    
        return dp[0][n - 1]



print(Solution().findMaxCoins(list(map(int, input().split()))))