class Solution:
    def encode(self, s):
        ans = ''
        c, cnt = s[0], 1
        for i in range(1, len(s)):
            if s[i] == c:
                cnt+=1
            else:
                ans+=c+str(cnt)
                cnt = 1
                c = s[i]
        
        ans+=c+str(cnt)
        return ans
sol = Solution()
print(sol.encode("abbbcdddd"))
