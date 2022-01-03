class Solution:
    def decodedString(self, s):
        def dfs(i, times, curstring):
            while i < len(s):
                while s[i].isdigit():
                    times = times*10+int(s[i])
                    i+=1
                
                if s[i] == ']':
                    return curstring, i
                
                if s[i] == '[':
                    recursive_op, end = dfs(i+1, 0, '')
                    curstring += recursive_op * times
                    i = end
                    times = 0
                else:
                    curstring += s[i]
                    
                i+=1
            return curstring, i
        
        return dfs(0, 0, '')[0]


sol = Solution()
print(sol.decodedString("3[a3[b]1[ab]]"))
