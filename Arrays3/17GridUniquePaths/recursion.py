class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countpaths(i, j, m,n):
            if i >= m or j >= n:
                return 0
            elif i == m-1 and j == n-1:
                return 1
            else:
                return countpaths(i+1, j, m, n) + countpaths(i, j+1, m, n)
        return countpaths(0, 0, m, n)
#Time limit exceeds in certain cases, only 37/63 test cases pass
