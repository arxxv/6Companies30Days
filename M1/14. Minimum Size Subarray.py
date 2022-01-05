class Solution:
    def minSubArrayLen(self, t, A):
        ans = len(A)+1
        cursum, a, b = 0, 0, 0
        while b < len(A):
            cursum += A[b]
            while cursum >= t:
                cursum -= A[a]
                ans = min(ans, b-a+1)
                a+=1
            b+=1
        
        if ans == len(A)+1:
            return 0
        
        return ans


sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))