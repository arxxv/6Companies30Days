class ans:
    def spirallyTraverse(self, mat, r, c): 
        ans = []
        if r == 0:
            return ans
        if c == 1:
            for i in range(r):
                ans.append(mat[i][0])
            return ans
        if r == 1:
            return mat[0]
        
        top, bottom, left, right = 0, r-1, 0, c-1
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                ans.append(mat[top][i])
            top+=1
            for i in range(top, bottom+1):
                ans.append(mat[i][right])
            right-=1
            if top <= bottom:
                for i in range(right, left-1, -1):
                    ans.append(mat[bottom][i])
                bottom-=1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(mat[i][left])
                left+=1
        return ans
                
