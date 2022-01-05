class Solution:
    def missingAndDuplicate(arr):
        n = len(arr)
        sum, sumsq = n*(n+1)/2, n*(n+1)*(2*n+1)/6
        for i in arr:
            sum -= i
            sumsq -= i**2
        
        m = (sumsq/sum+sum)/2
        r = m - sum
        return [r, m]


