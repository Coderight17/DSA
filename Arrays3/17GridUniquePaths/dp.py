class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countpaths(i, j, m, n, dp):
            if i >= m or j>= n:
                return 0
            elif i == m-1 and j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            else:
                dp[i][j] = countpaths(i+1, j, m, n, dp) + countpaths(i, j+1, m, n, dp)
                return dp[i][j]
        dp = [[-1 for i in range(n+1)] for i in range(m+1)]
        # print(dp)
        nums = countpaths(0,0,m,n,dp)
        if m == 1 and n ==1:
            return nums
        return dp[0][0]
    #Time complexity -> beats 100%
    #Space complexity -> Beats 24.19%
