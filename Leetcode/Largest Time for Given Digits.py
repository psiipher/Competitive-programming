'''
https://leetcode.com/problems/largest-time-for-given-digits/
'''

def largestTimeFromDigits(self, A: List[int]) -> str:
    time = -1
    from itertools import permutations
    
    k = sorted(list(permutations(A)), reverse=True)
    for h1, h2, m1, m2 in k:
        hour = h1 * 10 + h2
        minute = m1 * 10 + m2
        if hour < 24 and minute < 60:
            return f"{h1}{h2}:{m1}{m2}"
    
    return ""
