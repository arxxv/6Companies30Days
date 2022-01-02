class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        p1, product, ans = 0, 1, 0
        for p2 in range(len(a)):
            product *= a[p2]

            while product >= k:
                product //= a[p1]
                p1 = p1+1
            
            ans += (p2-p1+1)

        return ans

sol = Solution()
print(sol.countSubArrayProductLessThanK([1,2,3,4],4, 10))
