'''
https://leetcode.com/problems/coin-change/
'''

# 1-D array

def coinChange(self, coins: List[int], amount: int) -> int:
    if len(coins) == 0:
        return -1
    INT_MAX = float('inf')
    n = len(coins)
    
    dp = [INT_MAX] * (amount+1)
    dp[0] = 0
    
    for i in range(1, n+1):
        for j in range( amount+1):
            if coins[i-1] <= j:
                dp[j] = min(dp[j-coins[i-1]] +1, dp[j])
                
    if dp[-1] == INT_MAX:
        return -1
    else:
        return dp[-1]
        
# 2-D array

def coinChange(self, coins: List[int], amount: int) -> int:
    if len(coins) == 0:
        return -1
    INT_MAX = float('inf')
    n = len(coins)
    
    dp = [[0 for i in range(amount+1)] for j in range(n+1)]
    
    for j in range(amount+1):
        dp[0][j] = INT_MAX-1
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(1, amount+1):
        if j % coins[0] == 0:
            dp[1][j] = j / coins[0]
        else:
            dp[1][j] = INT_MAX-1
        
    for i in range(2, n+1):
        for j in range(1, amount+1):
            if coins[i-1] <= j:
                dp[i][j] = min(dp[i][j-coins[i-1]] +1, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
                
    if dp[-1][-1] == INT_MAX-1:
        return -1
    else:
        return int(dp[n][amount])
