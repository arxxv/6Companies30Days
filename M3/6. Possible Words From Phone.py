class Solution:
    def __init__(self):
        self.ans = []
        self.map = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

    def possibleWords(self, s, N):
        
        def helper(next, i):
            if i > len(s)-1:
                self.ans.append(next)
                return
            
            cur = self.map[int(s[i])-2]
            for j  in range(len(cur)):
                helper(next+cur[j], i+1)
        
        if s == None or len(s) < 1:
            return self.ans
        helper("", 0)
        return self.ans

print(Solution().letterCombinations("23", 2))