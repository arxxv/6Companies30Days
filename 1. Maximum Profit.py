class Solution:
    def maxProfit(self, k, prices):  
        if not prices or k == 0:
            return 0
        
        dp = [float('inf')]*k
        profit = [0]*k
        
        for p in prices:
            dp[0] = min(dp[0], p)
            profit[0] = max(profit[0], p - dp[0])
            for i in range(1,k):
                dp[i] = min(dp[i], p - profit[i-1])
                profit[i] = max(profit[i], p - dp[i])
        
        return profit[-1]

sol = Solution()
print(sol.maxProfit(2, [10,22,5,75,65,80])) 