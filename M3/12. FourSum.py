class Solution:
    def fourSum(self, nums, target):
        def ksum(nums, t, k):
            ans = []
            if not nums:
                return ans
        
            avg_val = t//k
            if avg_val < nums[0] or nums[-1] < avg_val:
                return ans
            
            if k == 2: return twosum(nums, t)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1]!=nums[i]:
                    for subset in ksum(nums[i+1:], t-nums[i], k-1):
                        ans.append(sorted([nums[i]]+subset))
            return sorted(ans)
        
        def twosum(nums, t):
            ans = []
            s = set()
            for i in range(len(nums)):
                if len(ans) == 0 or ans[-1][1] != nums[i]:
                    if t -nums[i] in s:
                        ans.append([t-nums[i], nums[i]])
                s.add(nums[i])
                
            return ans
        
        
        nums.sort()
        return ksum(nums, target, 4)