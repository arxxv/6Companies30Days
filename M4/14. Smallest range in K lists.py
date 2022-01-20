import heapq as heap
class Solution:
    def smallestRange(self, nums):
        
        pq = []
        rangeStart,rangeEnd = float("-inf"),float("inf")
        max_number = float("-inf")
        for i in range(len(nums)):
            heap.heappush(pq,(nums[i][0],0,nums[i]))
            max_number = max(max_number,nums[i][0])
            
        while len(pq)==len(nums):
            
            val,listindex,cl = heap.heappop(pq)
            if max_number - val < rangeEnd - rangeStart:
                rangeStart = val
                rangeEnd = max_number
                
            if len(cl) > listindex+1:
                heap.heappush(pq,(cl[listindex+1],listindex+1,cl))
                max_number = max(max_number,cl[listindex+1])
        return [rangeStart,rangeEnd]
    
inp = [[1,3,5,7,9],[0,2,4,6,8],[2,3,5,7,11]]

print(Solution().smallestRange(inp))