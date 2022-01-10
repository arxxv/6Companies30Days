class Solution:
    def colName (self, n):
        ans = ''
        arr = [0]*10000
        i = 0
        a = ord('A')
        while n > 0:
            arr[i] = n % 26
            n = int(n//26)
            i+=1
        
        for j in range(0,i-1):
            if arr[j] <= 0:
                arr[j]+=26
                arr[j+1]-=1
        
        for j in range(i,-1,-1):
            if arr[j] > 0:
                ans+=chr(a+(arr[j]-1))
        
        return ans


sol = Solution()
print(sol.colName(705))