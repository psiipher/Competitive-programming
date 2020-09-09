'''
https://leetcode.com/problems/valid-parentheses/
'''

def isValid(self, s: str) -> bool:
    if len(s) == 1:
        return False
    if len(s) % 2 != 0:
        return False

    stack = list()
    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack.append(char) 
        elif len(stack) <= 0:
            return False
        elif char == ")" and stack.pop() != "(":
            return False
        elif char == "]" and stack.pop() != "[":
            return False
        elif char == "}" and stack.pop() != "{":
            return False
    if len(stack) == 0:
        return True
    return False
