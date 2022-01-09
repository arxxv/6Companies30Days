class Solution:
    def countWays(self,m):
        return m//2+1

if __name__=='__main__':
    sol = Solution()
    print(sol.countWays(4))