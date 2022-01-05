class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        dp = [0]*n
        dp[0] = 1
        c = 1
        
        i2,i3,i5=0,0,0
        
        while c < n:
            n2, n3, n5 = dp[i2]*2, dp[i3]*3, dp[i5]*5
            
            x = min(n2,n3,n5)
            dp[c] = x
            c+=1
            
            if n2 == x: i2+=1
            if n3 == x: i3+=1
            if n5 == x: i5+=1
        
        return dp[n-1]
