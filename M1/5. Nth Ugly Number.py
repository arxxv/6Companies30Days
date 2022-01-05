class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        dp = [0]*n
        dp[0] = 1
        c = 1
        
        i2, i3, i5 = 0, 0, 0
        
        while c < n:
            nxt2, nxt3, nxt5 = dp[i2]*2, dp[i3]*3, dp[i5]*5
            
            nxt = min(nxt2,nxt3,nxt5)
            dp[c] = nxt
            c+=1
            
            if nxt2 == nxt: i2+=1
            if nxt3 == nxt: i3+=1
            if nxt5 == nxt: i5+=1
        
        return dp[n-1]
