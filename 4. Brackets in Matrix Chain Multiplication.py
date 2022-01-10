class Solution:
    def __init__(self):
        self.c ='A'
        self.ans = []

    def outp(self,i,j,bracket):
        if i == j:
            self.ans.append(self.c)
            i = ord(self.c[0])
            i += 1
            self.c = chr(i)

        else:
            self.ans.append('(')
            self.outp(i,bracket[i][j],bracket)
            self.outp(bracket[i][j] + 1 ,j,bracket)
            self.ans.append(')')
        return  ''.join(self.ans)
    
    def matrixChainOrder(self, arr, n):
        
        n = n-1
        dp = [[0 for i in range(n)] for i in range(n)]
        bracket = [[0 for i in range(n)] for i in range(n)]
        
        ans = []
        for g in range(n):
            i = 0
            j = g
            while i<n and j<n:
                if g == 0:
                    dp[i][j] = 0
                elif g == 1:
                    dp[i][j] = arr[i]*arr[j]*arr[j+1]

                else:
                    mi = 111111111
                    for k in range(i,j):
                        lc = dp[i][k]
                        rc = dp[k+1][j]
                        tm = arr[i]*arr[k+1]*arr[j+1]
                        mc = tm+lc+rc
                        if mc<mi:
                            mi = mc
                            
                    bracket[i][j] = k
                    dp[i][j]= mi

                i+=1
                j+=1
                
        return self.outp(0,n-1,bracket)


if __name__ == '__main__':
        sol = Solution()
        print(sol.matrixChainOrder([1,2,3,4,5], 5))
