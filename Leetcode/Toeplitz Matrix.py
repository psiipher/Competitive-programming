'''
https://leetcode.com/problems/toeplitz-matrix/
'''

def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    for i in range(len(matrix)-1, 0, -1):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == matrix[i-1][j-1]:
                continue
            else:
                return False
    return True
