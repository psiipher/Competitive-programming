def main():
    length = list(map(int, input("Enter length array\n").split()))
    price = list(map(int, input("Enter price array\n").split()))
    l = int(input("Enter total length\n"))
    n = len(length)    
    
    dp = [[0 for i in range(l + 1)] for j in range(n + 1)]
    
    for i in range(n+1):
        for j in range(l+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif length[i-1] <= j:
                dp[i][j] = max(price[i-1] + dp[i][j - length[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    print(dp[n][l])
main()
