class Solution:
    def splitArray(self, nums, x):

        l, r = min(nums), sum(nums)

        def check(m):
            y = 1
            su = nums[0]
            if su > m:
                return False
            for i in range(1, len(nums)):
                su += nums[i]
                if su > m:
                    y += 1
                    su = nums[i]
                    if su > m:
                        return False
            if y > x:
                return False
            return True

        while l <= r:
            m = l+(r-l)//2
            if check(m):
                r = m-1
            else:
                l = m+1

        return l
