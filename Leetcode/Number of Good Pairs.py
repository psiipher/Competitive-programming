'''
https://leetcode.com/problems/number-of-good-pairs/
'''

def numIdenticalPairs(self, nums: List[int]) -> int:
    count = dict()
    for i in nums:
        count[i] = count.get(i, 0) + 1
    ans = 0
    for v in count.values():
        ans += v * (v-1) // 2
    return ans
