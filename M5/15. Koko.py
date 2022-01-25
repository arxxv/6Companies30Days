class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        l = 1
        r = max(piles)
        
        while l < r:
            m = l + (r-l)//2
            x = 0
            for i in piles:
                x+=math.ceil(i/m)
            if x > h:
                l = m+1
            else:
                r = m
        return r