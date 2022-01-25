class Solution:
    def shipWithinDays(self, w, d):
        def check(m):
            l = 0
            ans = 1
            for i in w:
                l += i
                if l > m:
                    ans += 1
                    l = i
                    if l > m:
                        return False

            if ans <= d:
                return True
            else:
                return False

        l = 1
        r = sum(w)

        while l <= r:
            m = l+(r-l)//2
            if check(m):
                r = m-1
            else:
                l = m+1

        return l
