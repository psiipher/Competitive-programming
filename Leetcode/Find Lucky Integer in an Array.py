'''
https://leetcode.com/problems/find-lucky-integer-in-an-array/
'''

def findLucky(self, arr: List[int]) -> int:
    freq = Counter(arr)
    no = set(arr)
    max = -1
    for i in no:
        if i == freq[i] and i > max:
            max = i
    return max
