class Solution:
    def lengthOfLongestAP(self, A, n):
        ans = 2       
        n = len(A)
        if n <= 2:
            return n
        dp = [2]*n
        A.sort()
   
        for j in range(n-2, -1, -1):
            i= j-1
            k= j+1
            while(i>=0 and k<n):
                if A[i]+A[k] == 2*A[j]:
                    dp[j] = max(dp[k]+1,dp[j])
                    ans = max(ans, dp[j])
                    i-=1
                    k+=1
                elif A[i]+A[k] < 2*A[j]:
                    k += 1
                else:
                    i -= 1
   
        return ans 
   
a = [1,7,10,13,14,19]
print(Solution().lengthOfLongestAP(a,len(a)))