#User function Template for python3

class Solution:
    
    def dfs(self,graph,visited,stack,K,v):
        visited[v] = 1
        for k in range(K):
            if graph[v][k] == 1 and visited[k] == 0:
                self.dfs(graph,visited,stack,K,k)
        stack.append(v)
        
        
        
    def findOrder(self,dic, N, K):
        graph = [[0 for i in range(K)] for j in range(K)]
        stack  = []
        
        for i in range(len(dic)-1):
            temp = dic[i]
            temp1 = dic[i+1]
            j = 0
            k = 0
            while j< len(temp) and k<len(temp1) and temp[j]==temp1[k] :
                j+=1
                k+=1
            if j<len(temp) and k<len(temp1):
                graph[ord(temp[j]) - ord('a')][ord(temp1[k]) - ord('a')]  = 1
            
            
        visited = [0]*K
        for i in range(K):
            if visited[i] == 0:
                self.dfs(graph,visited,stack,K,i)
                
        stack = stack[::-1]
        
        string = ''
        for i in range(len(stack)):
            string += chr(stack[i]+97)
            
        return string
        