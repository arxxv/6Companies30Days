import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        gcd = math.gcd(len(str1), len(str2))
        if str1+str2 != str2+str1:
            return ''        
        return str1[:gcd]

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))
