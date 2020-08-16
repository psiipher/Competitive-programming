'''
https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/
'''

def main():
    n = int(input())
    l = list(map(int, input().split()))[::-1]
    ans = []
    check = l[0]
    ans.append(check)
    for i in range(1,n):
        if l[i] >= check:
            ans.append(l[i])
            check = l[i]
    print(*ans[::-1])
main()
