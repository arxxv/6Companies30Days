from collections import defaultdict

class Solution:
    def findWinner(self, votes):
        d = defaultdict(int)
        for st in votes:
            d[st] += 1
        mx = 0
        ans = ""
        for entry in d:
            key = entry
            val = d[entry]
            
            if (val > mx):
                mx = val
                ans = key

            elif (val == mx and
                ans > key):
                ans = key
        return ans

print(Solution().findWinner(votes = [ "john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john" ]))