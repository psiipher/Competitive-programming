def main():
    wt = list(map(int, input().split()))
    value = list(map(int, input().split()))
    W = int(input())
    n = len(wt)
    
    dp = [[-1 for i in range(W+1)] for j in range(n+1)]
    ans = knapsack(wt, value, W, n, dp)
    print(ans)
    
def knapsack(wt, value, W, n, dp):

    if n == 0 or W == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
        
    if wt[n-1] <= W:
        dp[n][W] =  max(value[n-1] + knapsack(wt, value, W - wt[n-1], n-1, dp),  knapsack(wt, value, W, n-1, dp))
        return dp[n][W]
        
    elif wt[n-1] > W:
        dp[n][W] = knapsack(wt, value, W, n-1, dp)
        return dp[n][W]
main()
