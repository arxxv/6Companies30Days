import bisect

class Solution:
    def checkArray(self, a, b, n, m) :
        lis= []
        s = set()
        for i in b:
            s.add(i)
        for i in a:
            if i in s:
                it = bisect.bisect_left(lis, i)
                if it == 0:
                    lis.append(i)
                else:
                    it = i
        return n+m-2*len(lis)
 
 
a = [1,2,5,3,1]
b = [1,3,5,3]
print(Solution().checkArray(a, b, len(a), len(b)))



