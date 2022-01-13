def sumHelper(root, x, ans):
    if not root:
        return 0
    left = sumHelper(root.left, x, ans) 
    right = sumHelper(root.right, x, ans) 
    sum = left + right + root.data 
    if (sum == x): 
        ans[0] += 1
    return sum

def countSubtreesWithSumX(root, x):
    if not root:
        return 0
    ans = [0]
    left = sumHelper(root.left, x, ans) 
    right = sumHelper(root.right, x, ans) 
    if ((left + right + root.data) == x): 
        ans[0] += 1
    return ans[0]