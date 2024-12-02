#This is the optimal approach where the time complexity is O(2*m*n) and the space complexity is O(1) as we use only one variable.We follow the following steps:
'''
1)We use the extra space in the better solution within the matrix itself in the first row and column. But the problem arises at matrix[0][0] where we need to 
  use the cell for marking both the first row and column. Thus, we use it to mark the first row and use an extra variable, col0 to mark the first column.
2)We then traverse through the matrix once, marking the 0s in the appropriate places(in first row & col and also in col0n if reqd)
3) Then, while making the cells 0s, we first only deal with matrix[1][1] to matrix[m-1][n-1](the matrix excluding the first row and columns). In these cells, we 
    make the entry 0 if either the corresponding row or columns is marked 0.
4) Now, we mark the first row 0 if matrix[0][0] is 0(as matrix[0][0] is the marker for the first row).
5)Now, we mark the first column as 0 if col0 is 0(as col0 is the marker for the first column).
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if col0 == 0:
            for  i in range(len(matrix)):
                matrix[i][0] = 0
