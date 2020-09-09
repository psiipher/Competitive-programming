'''
https://leetcode.com/problems/backspace-string-compare/
'''

def backspaceCompare(self, S: str, T: str) -> bool:
    s, t = [], []
    for ch in S:
        if ch == "#":
            if s != []:
                s.pop()
        else:
            s.append(ch)
    for ch in T:
        if ch == "#":
            if t != []:
                t.pop()
        else:
            t.append(ch)
    return s == t
