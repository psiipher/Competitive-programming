'''
https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/
'''

def main():
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        no = list(map(int, input().split()))
        diff = k - min(no)
        print(diff) if diff >= 0 else print(0)
main()
