class Solution:
    def PrintMinNumberForPattern(self, s):
        next, Dindex = 1, 0
        ans = []
        if s[0] == 'I':
            ans += [1, 2]
            Dindex = 1

        else:
            ans += [2, 1]
            Dindex = 0

        next = 3
        for i in range(1, len(s)):
            if s[i] == 'I':
                ans.append(next)
                next+=1
                Dindex = i+1
            else:
                ans.append(ans[i])
                for k in range(i, Dindex-1, -1):
                    ans[k]+=1
                next+=1
        return ans

sol = Solution()
print(sol.PrintMinNumberForPattern("DIIDDDI"))

# D   I   I   D   D   D   I
# 21  3   7   6   5   4   8