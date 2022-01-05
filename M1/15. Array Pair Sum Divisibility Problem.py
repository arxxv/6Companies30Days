class Solution:
    def canArrange(self, arr, k):
        if len(arr)%2 != 0:
            return False
        modarr = [x%k for x in arr]
        modarr.sort()
        z = 0
        for i in range(len(modarr)):
            if modarr[i] == 0: z+=1
            else: break
        
        if z%2!=0: return False
        
        j = len(arr)-1        
        while i < j:
            if (modarr[i] + modarr[j])%k != 0:
                return False
            i+=1
            j-=1
        
        return True 