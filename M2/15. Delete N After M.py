class Solution:
    def skipMdeleteN(self, h, M, N):
        t = h
        c = M-1
        d = N
        while t:
            if c != 0:
                t = t.next
                c-=1
                continue
            
            x = t
            while t:
                if d != 0:
                    d-=1
                    t = t.next
                    if t: x.next = t.next
                    else: x.next = t
                    continue
                
                t = t.next
                # x.next = t
                d = N
                c = M-1
                break
        
        return h