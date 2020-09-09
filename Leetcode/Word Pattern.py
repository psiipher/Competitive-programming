'''
https://leetcode.com/problems/word-pattern/
'''

def wordPattern(self, pattern: str, str: str) -> bool:
    if len(pattern) == len(str) == 0:
        return False
    words = str.split()
    if len(words) != len(pattern):
        return False
   
    match = OrderedDict()
    for i in range(len(pattern)):
        if pattern[i] in match:
            continue
        elif words[i] in match.values():
            continue
        else:
            match[pattern[i]] = words[i]
    
    for i in range(len(pattern)):
        if pattern[i] not in match:
            return False
        elif words[i] == match[pattern[i]]:
            continue
        else:
            return False
    return True
