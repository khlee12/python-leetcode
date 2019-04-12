# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # in grid[m][n], the number of paths = grid[m-1][n] + grid[m][n-1]
        grid = [([0]*(n+1)) for line in range(m+1)]
        grid[1][1] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[-1][-1]
    
        # https://leetcode.com/problems/unique-paths/discuss/23234/Accpeted-simple-Python-DP-solution.
        # 也可以全初始化为1
        # aux = [[1 for x in range(n)] for x in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         aux[i][j] = aux[i][j-1]+aux[i-1][j]
        # return aux[-1][-1]
