class Solution:
    def doOverlap(self, L1, R1, L2, R2):
        
        if L1[0] > R2[0] or L2[0] > R1[0] or R1[1] > L2[1] or L1[1] < R2[1]:
            return 0
        return 1
        
sol = Solution()
print(sol.doOverlap((0,10),(10, 0),(5,5),(15,0)))