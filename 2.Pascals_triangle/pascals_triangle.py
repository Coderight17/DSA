#Only the function, need to write the rest of the code like getting input, printing etc to get a completely working one.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = []
        for i in range(numRows):
            row = [0]*(i+1)
            pascals_triangle.append(row)
            for j in range(len(row)):
                if j == 0 or j== i:
                    pascals_triangle[i][j] = 1
                else:
                    pascals_triangle[i][j] = pascals_triangle[i-1][j] + pascals_triangle[i-1][j-1]
        return pascals_triangle   
