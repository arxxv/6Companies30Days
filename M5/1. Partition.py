# MEMO
def rec(arr, i, x, su, memo={}):
    if (i == len(arr)-1):
        return abs(su - 2*x)

    key = str(i)+' '+str(x)
    if key in memo:
        return memo[key]
    memo[key] = min(rec(arr, i + 1, x+arr[i], su), rec(arr, i + 1, x, su))
    return memo[key]


def findMin(arr, n):
    su = sum(arr)
    return rec(arr, 0, 0, su)


arr = [1, 25, 66, 42, 43]
print(findMin(arr, len(arr)))
