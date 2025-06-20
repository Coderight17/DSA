class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def issafe(grid,r,c,rows,cols):
            # print(f'({r},{c})->{grid[r][c]}')
            # print(f'({rows},{cols})')
            # print(grid[r][c])
            # print(f'{0<=r},{r < rows},{0 <=c},{c < cols},{grid[r][c] == 1}')
            if 0<=r and r < rows and 0 <=c and c < cols and grid[r][c] == "1":
                return True
            else:
                return False
        def dfs_visit(grid,r,c):
            dirR = [-1,0,0,1]
            dirC = [0,-1,1,0] 
            grid[r][c] = "0"
            for i in range(4):
                if issafe(grid,r+dirR[i], c + dirC[i], len(grid), len(grid[0])):
                    dfs_visit(grid,r+dirR[i], c + dirC[i])
        def dfs(grid):
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    # print(f'({i},{j})')
                    if issafe(grid,i,j,len(grid), len(grid[0])):
                        count = count + 1
                        dfs_visit(grid,i,j)
            return count
        return dfs(grid)
'''
Accepted
49 / 49 testcases passed
Coder174
Coder174
submitted at Jun 20, 2025 14:50

Editorial

Solution
Runtime
274
ms
Beats
27.52%
Analyze Complexity
Memory
20.23
MB
Beats
57.85%

'''
