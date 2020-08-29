def logic(arr, target, n):

    dp = [[0 for i in range(target+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(target+1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
                
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]


def main():
    arr = list(map(int, input("Enter the array\n").split()))
    target = int(input("Enter required sum\n"))
    n = len(arr)
       
    print(logic(arr, target, n))

main()
