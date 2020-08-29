def logic(arr, n):
    target = sum(arr)
    
    if target % 2 != 0:
        return False
    else:
        target = target // 2
        dp = [[False for i in range(target+1)] for j in range(n+1)]
        
        for i in range(n+1):
            for j in range(target+1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
                    
                elif arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]


def main():
    arr = list(map(int, input("Enter the array\n").split()))
    n = len(arr)
       
    print(logic(arr, n))

main()
