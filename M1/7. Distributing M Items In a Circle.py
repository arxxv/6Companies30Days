import random
class Solution:
    def distribute(self, n, m, k):
        x = (m+k-1)%n
        if x > n:
            x -= n
        return x

sol = Solution()
print(sol.distribute(5, 8, 2))