class Solution:
    def numDecodings(self, s: str) -> int:
        
        M = 1e9+7
        def fun(i, memo={}):
            if i == len(s):
                return 1
            if s[i] == '0': 
                return 0
            if i in memo: 
                return memo[i]
            
            tempcount = 0
            tempcount = (fun(i+1, memo) % M + tempcount % M) % M
            
            if i != len(s)-1:
                n = int(s[i])*10+int(s[i+1])
                if n < 27:
                    tempcount = (fun(i+2, memo) % M + tempcount % M) % M  
                    
            memo[i] = tempcount
            return tempcount
        
        ans = fun(0)
        return ans
            