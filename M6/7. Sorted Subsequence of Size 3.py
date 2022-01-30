class Solution:
    def find3Numbers(self, nums, n):
        small = [0]*(n+1)
        large = [0]*(n+1)

        mn, mx = 1e9, -1e9
        for i in range(n-1):
            mn = min(mn, nums[i])
            small[i+1] = mn
        for i in range(n-1, 0, -1):
            mx = max(mx, nums[i])
            large[i-1] = mx
        for i in range(1, n-1):
            if small[i] < nums[i] < large[i]:
                return [small[i], nums[i], large[i]]
        return []


print(Solution().find3Numbers([1, 2, 1, 1, 3], 5))
