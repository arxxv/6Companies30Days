from collections import deque
class Solution:
    def max_of_subarrays(self,arr,n,k):
        dq = deque()
        ans = []
        for i in range(k):
            while dq and arr[i] >= arr[dq[-1]] :
                dq.pop()
            dq.append(i)

        for i in range(k, n):
            ans.append(arr[dq[0]])

            while dq and dq[0] <= i-k:
                dq.popleft() 
            while dq and arr[i] >= arr[dq[-1]] :
                dq.pop()
            dq.append(i)
        ans.append(arr[dq[0]])
        return ans

if __name__=="__main__":
    sol = Solution()
    print(sol.max_of_subarrays([8,5,10,7,9,4,15,12,90,13], 9, 4))
