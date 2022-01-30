class Solution:
    def divide(self, A, B):
        pos = not ((A < 0) ^ (B < 0))
        A, B = abs(A), abs(B)
        res = 0
        while A >= B:
            temp, i = B, 1
            while A >= temp:
                A -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not pos:
            res = -res
        return min(max(-2147483648, res), 2147483647)
