from collections import deque

class Solution:
    def mapper(self, node, parent):
        if not node:
            return
        if node not in self.map:
            self.map[node] = []
            if parent:
                self.map[node].append(parent)
                self.map[parent].append(node)
            self.mapper(node.left, node)
            self.mapper(node.right, node)

    def minTime(self, root, target):
        
        def findtarget(r,t):
            if not r:
                return
            if r.data == t:
                return r
            
            x = findtarget(r.left,t)
            if x: 
                return x
            x = findtarget(r.right,t)
            if x:
                return x
        
        
        target = findtarget(root,target)
        # print(target)
        if not root:
            return
        self.map = {}
        self.mapper(root, None)
        if target not in self.map:
            return None
        
        visited = set()
        q = deque([target])
        ans = -1 
        while q:
            ans+=1
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                for next in self.map[node]:
                    if next in visited:
                        continue
                    visited.add(next)
                    q.append(next)