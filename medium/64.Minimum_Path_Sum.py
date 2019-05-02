# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        sumGrid = [[0 for i in range(col)] for j in range(row)]
        sumGrid[0][0] = grid[0][0]
        for i in range(1, row):
            sumGrid[i][0] = sumGrid[i-1][0]+grid[i][0]
        for i in range(1, col):
            sumGrid[0][i] = sumGrid[0][i-1]+grid[0][i]
        for i in range(1, row):
            for j in range(1, col):
                sumGrid[i][j] = min(sumGrid[i][j-1], sumGrid[i-1][j])+grid[i][j]
        
        return sumGrid[-1][-1]
