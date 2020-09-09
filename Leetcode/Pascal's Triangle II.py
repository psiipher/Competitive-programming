'''
https://leetcode.com/problems/pascals-triangle-ii/
'''

def getRow(self, rowIndex: int) -> List[int]:
    ans = [[1], [1,1]]
    for i in range(2, rowIndex+1):
        ans.append([1])
        for j in range(1, i):
            ans[i].append(ans[i-1][j-1] + ans[i-1][j])
        ans[i].append(1)
    return ans[rowIndex]
