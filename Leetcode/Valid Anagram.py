'''
    https://leetcode.com/problems/valid-anagram/
'''

def isAnagram(self, s: str, t: str) -> bool:
    words_s = dict()
    words_t = dict()
    for i in s:
        words_s[i] = words_s.get(i, 0) + 1
    for i in t:
        words_t[i] = words_t.get(i, 0) + 1
    return words_s == words_t
    
