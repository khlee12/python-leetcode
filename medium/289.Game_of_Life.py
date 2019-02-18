# 289. Game of Life
# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        # in-place状态变换题
        # 比如活角色会在某个条件下死，死角色会在某个条件下复活
        # 用两个二进制bit，第二个bit表示prev_status，第一个bit表示next_status
        # 用prev_status来计算next_status
        # 遍历计算完之后，用 >> 1计算来保留next_status
        # https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
        
        # 状态变换：
        # 01 -> 01: when live < 2 
        # 01 -> 11: when live == 2 or live == 3 **
        # 01 -> 01: when live > 3 
        # 00 -> 10: lives == 3 **
        def getLives(board, row, col, max_row, max_col):
            lives = 0
            
            for i in range(max(row-1, 0), min(row+2, max_row)):
                for j in range(max(col-1, 0), min(col+2, max_col)):
                    if i == row and j == col:
                        continue
                    lives += board[i][j] & 1
            return lives
            
        max_row = len(board)
        max_col = len(board[0])
        for i in range(max_row):
            for j in range(max_col):
                prev_state = board[i][j] & 1
                lives = getLives(board, i, j, max_row, max_col)
                # print(lives)
                if board[i][j] == 1 and lives == 2 or board[i][j] == 1 and lives == 3:
                    board[i][j] = 3
                elif board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        
        for i in range(max_row):
            for j in range(max_col):
                board[i][j] >>= 1
