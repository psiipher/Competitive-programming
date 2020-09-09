'''
https://leetcode.com/problems/convert-a-number-to-hexadecimal/
'''

def toHex(self, num: int) -> str:
    if 0 <= num < 10:
        return str(num)
    match = {10: 'a', 11: 'b', 12: 'c', 13: 'd',14: 'e',15: 'f'}
    
    if 9 < num < 16:
        return match[num]
    if num < 0:
        num += pow(2,32)
        
    ans = ''
    while num > 0:
        mod = num % 16
        if mod >= 10:
            ans += match[mod]
        else:
            ans += str(mod)
        num = num // 16
    return ans[::-1].lstrip('0')    
