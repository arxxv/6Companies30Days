from collections import deque

class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        q = deque([root])
        while q:
            sz = len(q)
            p = None
            for i in range(sz):
                # print(q)
                x = q.popleft()
                    
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                
                if p:
                    p.nextRight = x
                p = x
                
            p.nextRight=None
            