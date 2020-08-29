'''
https://practice.geeksforgeeks.org/problems/minimum-sum-partition/0
'''

def main():
    arr = list(map(int, input("Enter array\n").split()))
    n = len(arr)
    target = sum(arr)
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
                
    i = (target//2)
    possible = 0
    while i > 0:
        if dp[n][i]:
            possible = i
            break
        i -= 1
    
    ans = target-(2 * possible)
    print(ans)
        
main()
