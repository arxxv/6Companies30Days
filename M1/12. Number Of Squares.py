class Solution:
    def noSquares(self, n):
        return n*(n+1)*(2*n+1)//6

sol = Solution()
print(sol.noSquares(8))