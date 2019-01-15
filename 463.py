# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or not grid:
            return

        max_row = len(grid)
        max_col = len(grid[0])
        if max_row == 1 and max_col == 1:
            return 4 if grid[0][0] == 1 else 0

        result = 0

        # 计算1的上下左右的0的个数
        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col] == 1:
                    # left index
                    if col == 0 or (col > 0 and grid[row][col-1] == 0):
                        result += 1
                    # right index
                    if col == max_col-1 or (col < max_col-1 and grid[row][col+1] == 0):
                        result += 1
                    # top index
                    if row == 0 or (row > 0 and grid[row-1][col] == 0):
                        result += 1
                    # bottom index
                    if row == max_row-1 or (row < max_row-1 and grid[row+1][col] == 0):
                        result += 1

        return result
