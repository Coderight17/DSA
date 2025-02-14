class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m+n-2
        r = m-1
        result = 1
        for i in range(1,r+1):
            result  = result*(N-r+i)/i
        return int(result)
#Time complexity -> Beats 100%
#Space complexity -> Beats 86.06%
