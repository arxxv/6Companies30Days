class Solution:
    def orangesRotting(self, grid):
        rotten = []
        fresh = 0
        time = 0
        
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh += 1

        while len(rotten) > 0 and fresh>0:
            time+=1
            
            for r in range(len(rotten)):
                orange = rotten[0]
                del rotten[0]
                
                x, y = orange[0], orange[1]
                for mv in moves:
                    adjx, adjy = x+mv[0],y+mv[1]
                    if adjx < 0 or adjx >= len(grid) or adjy < 0 or adjy >= len(grid[0]) or grid[adjx][adjy] == 0 or grid[adjx][adjy] == 2: continue
                    
                    fresh -= 1
                    grid[adjx][adjy] = 2
                    rotten.append((adjx,adjy))
                    
        
        if fresh > 0: 
            return -1
        return time