class Solution:
    def displayContacts(self, n, contact, s):
        contset = set(contact)
        t = ''
        ans = []
        for i in s:
            t+=i
            temp = []
            for c in contset:
                if c.startswith(t):
                    temp.append(c)
            if len(temp) == 0:
                temp.append(0)
            ans.append(sorted(temp))
        return ans

sol = Solution()
n = int(input())
c = input().split()
s = input()
print(sol.displayContacts(n,c,s))


