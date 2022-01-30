class Solution:
    def height(self, n):
        s, ans, i = 0, 0, 1
        while(s < n):
            s += i
            i += 1
            ans += 1
        if s == n:
            return ans
        return ans-1


print(Solution().height(10))
