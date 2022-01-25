class Solution:
    def minSwaps(self, grid):
        ans, n = 0, len(grid)
        zs = []
        for i in grid:
            tmp = 0
            for j in range(n-1, -1, -1):
                if i[j] == 0:
                    tmp += 1
                else:
                    break
            zs.append(tmp)

        for i in range(n):
            x = n-i-1
            if zs[i] >= x:
                continue
            for j in range(i+1, n):
                if zs[j] >= x:
                    ans += (j-i)
                    zs[i+1:j+1] = zs[i:j]
                    break
            else:
                return -1

        return ans


print(Solution().minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
