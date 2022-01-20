class Solution:
    def AllParenthesis(self,n):
        global ans
        ans = []
        def helper(s, l, r):
            if l == 0 and r == 0:
                ans.append(s)
                return
            if l > 0:
                helper(s+'(',l-1,r)
            if r > l:
                helper(s+')',l,r-1)
        helper('', n, n)
        return ans

print(Solution().AllParenthesis(3))