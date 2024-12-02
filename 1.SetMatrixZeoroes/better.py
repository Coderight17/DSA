#This one is better than the brute force approach as it takes only O(mn)*2 time complexity as we traverse the matrix twice, once to
#mark and once to change the entries, but it uses extra space to  mark the rows and columns as 0 ones. It uses O(m+n) extra space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = [1]*len(matrix)
        cols = [1]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0
        for i in range(len(rows)):
             for j in range(len(cols)):
                if rows[i] == 0 or cols[j] == 0:
                    matrix[i][j] = 0
