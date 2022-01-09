from typing import DefaultDict


class Solution:
    def FirstNonRepeating(self, A):
        t = []
        rp = [0]*26
        a = ord('a')
        ans = ''
        for i in range(len(A)):
            c = A[i]
            if not rp[ord(c)-a]:
                if not c in t:
                    t.append(c)
                else:
                    rp[ord(c)-a]=1
                    t.remove(c)
                    
            if len(t) > 0:
                ans+=t[0]
            else:
                ans+='#'
        return ans



if __name__=='__main__':
    sol = Solution()
    print(sol.FirstNonRepeating('aabc'))
