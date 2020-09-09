'''
https://leetcode.com/problems/xor-operation-in-an-array/
'''

def xorOperation(self, n: int, start: int) -> int:
    ans = start
    while n > 1:
        start += 2
        ans = ans ^ start
        n -= 1
    return ans
    
