'''
https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/help-jarvis-8a39566e/
'''

def check(no):
    if len(no) == 1:
        print('YES')
        return
    if no[-1] - no[0] != len(no)- 1:
        print('NO')
        return
    else:
        return check(no[:-1])
# Write your code here
def main():
    for _ in range(int(input())):
        n = list(map(int, input()))
        n = sorted(n)
        check(n)
main()
