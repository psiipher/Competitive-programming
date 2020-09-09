'''
https://leetcode.com/problems/repeated-substring-pattern/
'''

def repeatedSubstringPattern(self, s: str) -> bool:
    temp = ''
    for i in range(len(s)//2):
        temp += s[i]
        if len(s) % len(temp) != 0:
            continue
        else:
            if temp * (len(s) // len(temp)) == s:
                return True
    return False
