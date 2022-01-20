class Solution:
    def amendSentence(self, s):
        s = list(s)
        ans = []
        for i in range(len(s)):
            if s[i] >= 'A' and s[i] <= 'Z':
                s[i] = chr(ord(s[i]) + 32)
                if i != 0:
                    ans.append(" ")
                ans.append(s[i])
            else:
                ans.append(s[i])
        return ''.join(ans)

print(Solution().amendSentence("BruceWayneIsBatman"))