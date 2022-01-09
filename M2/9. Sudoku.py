class Solution:
    def isValid(self, b):
        n = len(b)
        s = set()
        for i in range(n):
            for j in range(n):
                if b[i][j] != 0:
                    x = str(b[i][j])+'r'+str(i)
                    y = str(b[i][j])+'c'+str(j)
                    z = str(b[i][j])+'b'+str(i//3)+str(j//3)
                    if x in s or y in s or z in s:
                        return 0
                    
                    s.add(x)
                    s.add(y)
                    s.add(z)
        return 1