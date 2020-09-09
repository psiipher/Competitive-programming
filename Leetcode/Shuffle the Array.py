'''
https://leetcode.com/problems/shuffle-the-array/
'''

def shuffle(self, nums: List[int], n: int) -> List[int]:
    left = 0
    right = n
    ans = []
    for i in range(n):
        ans.append(nums[left])
        ans.append(nums[right])
        left += 1
        right += 1
    return ans
