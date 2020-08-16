'''
https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/no-sharing-capillary-82ed3fe2/
'''

def main():
    for _ in range(int(input())):
        N, p, q, r = list(map(int, input().split()))
        count = 0
        for i in range(2, N+1):
            if i%p == 0 and i%q != 0 and i%r != 0:
                count += 1
            elif i%p != 0 and i%q == 0 and i%r != 0:
                count += 1
            elif i%p != 0 and i%q != 0 and i%r == 0:
                count += 1
        print(count)
main()
