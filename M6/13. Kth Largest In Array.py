class Solution:
    def kthLargestNumber(self, nums, k):
        return sorted(nums, key=int, reverse=True)[k-1]
