def main():
    wt = list(map(int, input("Enter weight array\n").split()))
    value = list(map(int, input("Enter value array\n").split()))
    W = int(input("Enter Weight\n"))
    n = len(wt)
    
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]
    
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= j:
                dp[i][j] = max(value[i-1] + dp[i][j - wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    print(dp[n][W])
main()
