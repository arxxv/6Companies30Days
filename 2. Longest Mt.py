class Solution:
    def longestMountain(self, arr):

        leftArr = [0 for i in range(len(arr))]
        rightArr = [0 for i in range(len(arr))]
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                leftArr[i] = leftArr[i-1]+1
            else:
                leftArr[i] = 0
        
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > arr[i+1]:
                rightArr[i] = rightArr[i+1]+1
            else:
                rightArr[i] = 0
                    
        ans = 0
        for i in range(len(arr)):
            if leftArr[i] * rightArr[i] != 0: 
                ans = max(ans, leftArr[i]+rightArr[i])
        
        return ans+1 if ans!=0 else 0         

if __name__=='__main__':
    sol = Solution()
    print(sol.longestMountain([2,1,4,7,3,2,5]))