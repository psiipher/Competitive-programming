'''
https://leetcode.com/problems/the-kth-factor-of-n/
'''

def kthFactor(self, n: int, k: int) -> int:
    ans = [1]
    end = (n // 2) + 1
    for i in range(2, end):
        if n % i == 0:
            ans.append(i)
    ans.append(n)
    try:
        return ans[k-1]
    except:
        return -1
    
