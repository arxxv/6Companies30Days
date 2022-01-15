class Solution:
    def FindMaxSum(self, nums, n):
            if n == 0: return 0
            if n == 1: return nums[0]
            if n == 2: return max(nums)
            
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
            return dp[-1]

print(Solution().FindMaxSum([5,5,10,100,10,5], 6))