class Solution:
    def isWordExist(self, B, w):
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.w = w

        def fun(i, j, k):
            if k == len(self.w):
                return True
            if i < 0 or i >= len(B) or j < 0 or j >= len(B[0]) or self.w[k] != B[i][j]:
                return False

            c = B[i][j]
            B[i][j] = 0
            ans = False
            for di, dj in moves:
                x, y = i+di, j+dj
                if fun(x, y, k+1):
                    ans = True
                    break
            B[i][j] = c
            return ans

        for i in range(len(B)):
            for j in range(len(B[0])):
                if fun(i, j, 0):
                    return True
        return False


n, m = list(map(int, input().split()))
B = []
for _ in range(n):
    tmp = list(input().split())
    B.append(tmp)
w = input().strip()

print(Solution().isWordExist(B, w))
