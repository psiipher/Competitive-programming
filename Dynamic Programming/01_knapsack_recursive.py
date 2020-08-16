def main():
    wt = list(map(int, input().split()))
    value = list(map(int, input().split()))
    W = int(input())
    n = len(wt)
    
    ans = knapsack(wt, value, W, n)
    print(ans)
    
def knapsack(wt, value, W, n):
    if n == 0 or W == 0:
        return 0
    
    if wt[n-1] <= W:
        return max(value[n-1] + knapsack(wt, value, W - wt[n-1], n-1),  knapsack(wt, value, W, n-1))
    elif wt[n-1] > W:
        return knapsack(wt, value, W, n-1)
main()
