import math


def missingNumber(s):

    def val(s, i, l):
        if(i + l > len(s)):
            return -1
        value = 0
        for j in range(l):
            c = (ord(s[i + j]) - ord('0'))
            if(c < 0 or c > 9):
                return -1
            value *= 10
            value += c
        return value

    for l in range(1, 7):
        n = val(s, 0, l)
        if(n == -1):
            break
        ans = -1
        fail = False
        i = l
        while(i != len(s)):
            if((ans == -1) and (val(s, i, 1 + int(math.log10(n + 2))) == n + 2)):
                ans = n + 1
                n += 2

            elif((val(s, i, 1 + int(math.log10(n + 1))) == n + 1)):
                n += 1
            else:
                fail = True
                break
            i += 1 + int(math.log10(n))

        if(not fail):
            return ans

    return -1


for _ in range(int(input())):
    print(missingNumber((input())))
