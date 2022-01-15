class Solution:
    def generate(self, N):
        arr = ["1"]
        if N == 1:
            return arr
        
        def add1(a):
            a, i, c = list(a), len(a)-1, 0
            while i >= 0:
                if a[i] == '0': a[i], c = '1', 0; break
                else: a[i], c = '0', 1
                i-=1
            if c: a.insert(0, '1')
            return ''.join(a)
            

        for i in range(2, N+1):
            arr.append(add1(arr[-1]))
        return arr



print(Solution().generate(10))



        