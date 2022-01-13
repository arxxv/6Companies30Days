class Solution:
    def calculateSpan(self, price, n):
        stack = [] 
        stack.append(0)
        ans = [0 for _ in range(n)]
        ans[0] = 1
        for i in range(1, n):
            while(len(stack) > 0 and price[stack[-1]] <= price[i]):
                stack.pop()
            if len(stack) <= 0:
                ans[i] = i + 1 
            else:
                ans[i] = i - stack[-1]
            stack.append(i)
        return ans

print(Solution().calculateSpan([100, 80, 60, 70, 60, 75, 85], 7))