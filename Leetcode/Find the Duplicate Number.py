'''
https://leetcode.com/problems/find-the-duplicate-number/
'''

def findDuplicate(self, nums: List[int]) -> int:
    ans = dict()
    for i in nums:
        ans[i] = ans.get(i, 0) + 1
    for k, v in ans.items():
        if v > 1:
            return k
