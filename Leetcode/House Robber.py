'''
https://leetcode.com/problems/house-robber/
'''

def rob(self, nums: List[int]) -> int:
    if (len(nums)) == 0:
        return 0
    elif (len(nums)) == 1:
        return nums[0]

    res = []
    res.append(nums[0])
    res.append(max(nums[0],nums[1]))
    for i in range(2,len(nums)):
        val = max(res[i-1], res[i-2]+nums[i])
        res.append(val)
    return res[-1]
