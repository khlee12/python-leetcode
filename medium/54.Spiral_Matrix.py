# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if matrix is None or not matrix:
            return matrix
        if len(matrix) == 1:
            return matrix[0]

        row_pointer = 0
        col_pointer = 0
        row_start = 0
        col_start = 0
        row_end = len(matrix)
        col_end = len(matrix[0])
        horizontal = True
        reverse = False

        result = []
        while row_start < row_end and col_start < col_end:
            if horizontal and not reverse:

                for col in range(col_start, col_end):
                    result.append(matrix[row_pointer][col])
                horizontal = False
                reverse = False
                row_start += 1
                col_pointer = col_end-1
            elif not horizontal and not reverse:
                for row in range(row_start, row_end):
                    result.append(matrix[row][col_pointer])
                horizontal = True
                reverse = True
                col_end -= 1
                row_pointer = row_end-1
            elif horizontal and reverse:
                for col in range(col_end-1, col_start-1, -1):
                    result.append(matrix[row_pointer][col])
                horizontal = False
                reverse = True
                row_end -= 1
                col_pointer = col_start

            elif not horizontal and reverse:
                for row in range(row_end-1, row_start-1, -1):
                    result.append(matrix[row][col_pointer])
                horizontal = True
                reverse = False
                col_start += 1
                row_pointer = row_start

        return result
