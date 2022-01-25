class Solution:
    def numberOfBoomerangs(self, p):
        n = 0
        for a, b in p:
            counter = {}
            for x, y in p:
                k = (x-a)**2+(y-b)**2
                if k in counter:
                    n += 2*counter[k]
                    counter[k] += 1
                else:
                    counter[k] = 1
        return n
