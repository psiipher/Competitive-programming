'''
https://leetcode.com/problems/search-a-2d-matrix/
'''

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0 or matrix is None or len(matrix[0]) == 0:
        return False
    for i in range(len(matrix)):
        if target <= matrix[i][-1]:
            return target in matrix[i]
