import sys
class Solution:
    def atoi(self,s):
        s = list(s)
        sign, base, i = 1, 0, 0
        
        while (s[i] == ' '): i += 1
        
        if (s[i] == '-' or s[i] == '+'):
            sign = 1 - 2 * (s[i] == '-')
            i += 1

        while i < len(s) and  s[i] >= '0' and s[i] <= '9':
            if (base > (sys.maxsize // 10) or (base == (sys.maxsize // 10) and  (s[i] - '0') > 7)):
                if (sign == 1):
                    return sys.maxsize
                else:
                    return -(sys.maxsize)
            
            base = 10 * base + (ord(s[i]) - ord('0'))
            i += 1
        
        return base * sign

print(Solution().atoi(input()))
