'''
https://leetcode.com/problems/target-sum/
'''

def findTargetSumWays(self, nums: List[int], S: int) -> int:
    n = len(nums)
    total = sum(nums)
    if S > total:
        return 0
    
    
    if (S + total) % 2 != 0:
        return 0
    target = (S + total) // 2

    dp = [[0 for i in range(target+1)] for j in range(n+1)]

    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(target+1):
            if nums[i-1] <= target:
                dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]
