# 174. Dungeon Game
# https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 1
        m = len(dungeon) # 行
        n = len(dungeon[0]) # 列
        grid = [[sys.maxsize for i in range(n)]for i in range(m)]
        
        grid[-1][-1] = 1 if 1-dungeon[-1][-1]<=0 else 1-dungeon[-1][-1]
        for i in range(m-2, -1, -1):
            # 最后一列
            needed = grid[i+1][-1]-dungeon[i][-1]
            grid[i][-1] = 1 if needed<=0 else needed
        for j in range(n-2, -1, -1):
            # 最后一行
            needed = grid[-1][j+1]-dungeon[-1][j]
            grid[-1][j] = 1 if needed <= 0 else needed
            
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                needed = min(grid[i][j+1]-dungeon[i][j], grid[i+1][j]-dungeon[i][j])
                grid[i][j] = 1 if needed <= 0 else needed
        print(grid)
        return 1 if grid[0][0] <= 0 else grid[0][0]
