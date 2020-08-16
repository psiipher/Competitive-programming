def main():
    wt = list(map(int, input().split()))
    value = list(map(int, input().split()))
    W = int(input())
    n = len(wt)
    
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]
    
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= W:
                dp[i][j] = max(value[i-1] + dp[i-1][j - wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    print(dp[n][W])
main()
