class Solution:
    def leaders(self, arr, size):
        mxr = arr[size-1]  
        ans = []
        ans.append(mxr)  
        for i in range( size-2, -1, -1):       
            if mxr < arr[i]:       
                ans.append(arr[i])
                mxr = arr[i]
    
        return ans
    
         
arr = [16, 17, 4, 3, 5, 2]
print(Solution().leaders(arr, len(arr)))