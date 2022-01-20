class Solution:
    def subArraySum(self,arr, n, s): 
        m = {0:-1}
        x=0
        for i in range(n):
            x+=arr[i]
            if x-s in m:
                return [m[x-s]+2, i+1]
            m[x] = i
        return [-1]