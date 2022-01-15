class Solution:
    def minSteps(self, D):
        steps = 0
        i = 1
        D = abs(D)
        while steps < D:
            steps += i
            i+=1
        
        if steps == D:
            return i-1
        
        diff = steps - D
        while diff % 2 != 0:
            steps += i
            i+=1
            diff = steps - D
        
        
        return i-1
        

            
if __name__ == '__main__':
    print(Solution().minSteps(int(input())))