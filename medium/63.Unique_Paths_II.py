# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        col = len(obstacleGrid[0])
        row = len(obstacleGrid)
        pathGrid = [([0]*col) for line in range(row)]
        if obstacleGrid[0][0] == 1:
            return 0
        pathGrid[0][0] = 1
        for i in range(1,col):
            pathGrid[0][i] = (1-obstacleGrid[0][i])*pathGrid[0][i-1]
        for i in range(1,row):
            pathGrid[i][0] = (1-obstacleGrid[i][0])*pathGrid[i-1][0]
            
        for i in range(1, row):
            for j in range(1, col):
                pathGrid[i][j] = (1-obstacleGrid[i][j])*pathGrid[i-1][j] + (1-obstacleGrid[i][j])*pathGrid[i][j-1]
        return pathGrid[-1][-1]            
