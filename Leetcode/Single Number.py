'''
https://leetcode.com/problems/single-number/
'''

def singleNumber(self, nums: List[int]) -> int:
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans
