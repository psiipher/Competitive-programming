'''
https://leetcode.com/problems/compare-version-numbers/
'''

def compareVersion(self, version1: str, version2: str) -> int:
    ver1 = list(map(int, version1.split(".")))
    ver2 = list(map(int, version2.split(".")))
    l1, l2 = len(ver1), len(ver2)
    
    if l1 > l2:
        ver2 += [0] * (l1 - l2)
    elif l2 > l1:
        ver1 += [0] * (l2 - l1)
        
    for i, j in zip(ver1, ver2):
        if i > j:
            return 1
        elif j > i:
            return -1
    return 0
