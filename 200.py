#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:12:55 2018

@author: khlee

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class Solution:
    def __init__(self):
        self = None
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if (grid is None or not grid):
            return 0
        
        numIslands = 0
        
        row_num = len(grid)
        col_num = len(grid[0])
        for i in range(row_num):
            for j in range(col_num):
                if (grid[i][j] == '1'):
                    numIslands += 1
                    self.dfs(grid, i, j)
        return numIslands
        
    def dfs(self, grid, row, col):
        row_num = len(grid)
        col_num = len(grid[0])
        grid[row][col] = '0'
        
        if (row+1 < row_num and grid[row+1][col] == '1'):
            self.dfs(grid, row+1, col)
        if (row-1 > -1 and grid[row-1][col] == '1'):
            self.dfs(grid, row-1, col)
        if (col+1 < col_num and grid[row][col+1] == '1'):
            self.dfs(grid, row, col+1)
        if (col-1 > -1 and grid[row][col-1] == '1'):
            self.dfs(grid, row, col-1)
        
solution = Solution()

arr1 = None     
'''
1 1 0 0
1 1 1 0
0 0 0 0
0 0 0 1
'''
arr2 = [['1','1','0','0'],['1','1','1','0'],['0','0','0','0'],['0','0','0','1']]
arr3 = [['0']]
arr4 = []
'''
1 1 0 1
0 1 1 0
0 0 0 0
1 1 1 1
'''
arr5 = [['1','1','0','1'],['0','1','1','0'], ['0','0','0','0'], ['1','1','1','1']]
print(solution.numIslands(arr1))
print(solution.numIslands(arr2))
print(solution.numIslands(arr3))
print(solution.numIslands(arr4))
print(solution.numIslands(arr5))
