class Solution:
    def equalPartition(self, n, nums):
        
        def rec(s, i, memo={}):
            if i == len(nums) or s < 0: return False
            if s == 0: return True
            if str(i)+' '+str(s) in memo : return memo[str(i)+' '+str(s)]
            
            memo[str(i)+' '+str(s)] = rec(s-nums[i], i+1) or rec(s, i+1)
            return memo[str(i)+' '+str(s)]
        
        s = sum(nums)
        if s%2!=0:
            return False
        return rec(s/2,0)

print(Solution().equalPartition(4, list(map(int, input().split()))))