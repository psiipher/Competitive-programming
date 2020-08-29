'''
https://leetcode.com/problems/pascals-triangle/
'''

def generate(self, numRows: int) -> List[List[int]]:
    ret = [[i for i in range(1, j+1)] for j in range(1, numRows+1)]
    for i in range(1, numRows+1):
        for j in range(i):
            if j == 0 or j == len(ret[i-1])-1:
                ret[i-1][j] = 1
            elif i>=2:
                ret[i-1][j] = ret[i-2][j-1] + ret[i-2][j]
                
    return ret
