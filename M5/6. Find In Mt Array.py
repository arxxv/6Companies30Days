class Solution:

    def findInMountainArray(self, T, A):
        rightSide = False

        def peak(A):
            l, r = 0, A.length()-1
            while l < r:
                m = l+(r-l)//2
                a = A.get(m-1) if m != 0 else - 1
                b = A.get(m)
                c = A.get(m+1) if m != A.length()-1 else -1

                if a < b < c:
                    l = m+1
                elif a > b > c:
                    r = m
                elif a < b and b > c:
                    return m
            return -1

        def bs(A, T, l, r):
            while l < r:
                m = l+(r-l)//2
                x = A.get(m)
                if x == T:
                    return m
                elif x > T:
                    if not rightSide:
                        r = m
                    else:
                        l = m+1
                else:
                    if not rightSide:
                        l = m+1
                    else:
                        r = m
            return l if A.get(l) == T else -1

        p = peak(A)
        if A.get(p) == T:
            return p
        ans = bs(A, T, 0, p)
        if ans != -1:
            return ans
        rightSide = True
        ans = bs(A, T, p, A.length()-1)
        return ans


print(Solution().findInMountainArray(3, [1, 2, 3, 4, 5, 3, 1]))
