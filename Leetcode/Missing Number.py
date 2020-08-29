'''
https://leetcode.com/problems/missing-number/
'''

def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    expected = (n * (n+1)) // 2
    actual = sum(nums)
    return expected - actual
