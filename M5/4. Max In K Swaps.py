class Solution:
    def findMaximumNum(self, s, k):
        self.mx = s

        def swap(s, i, c):
            s = list(s)
            s[i], s[c] = s[c], s[i]
            return ''.join(s)

        def solve(s, k, c):
            if k == 0:
                return
            n = len(s)
            mx = s[c]
            mxptr = c
            for i in range(c+1, n):
                if mx < s[i]:
                    mx = s[i]
                    mxptr = i

            if mx != s[c]:
                k -= 1

            for i in range(n-1, c-1, -1):
                if s[i] == mx:
                    s = swap(s, i, c)
                    if s > self.mx:
                        self.mx = s
                    solve(s, k, c+1)
                    s = swap(s, i, c)

        solve(s, k, 0)


s = "129814999"
k = 4
sol = Solution()
sol.findMaximumNum(s, k)
print(sol.mx)
