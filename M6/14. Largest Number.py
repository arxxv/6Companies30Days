class Solution:

    def findMaximumNum(self, s, k):
        self.mx = s

        def solve(s, k):
            if k == 0:
                return
            n = len(s)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if s[i] < s[j]:
                        s = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                        if s > self.mx:
                            self.mx = s
                        solve(s, k - 1)
                        s = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
        solve(s, k)
        return self.mx
