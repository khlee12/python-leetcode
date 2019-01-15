# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        max_row = len(A)
        max_col = len(A[0])
        
        result = []
        for i in range(max_row):
            each_row = []
            for j in range(max_col-1, -1, -1):
                flipped_number = (-1)*(A[i][j]-1)
                each_row.append(flipped_number)
            result.append(each_row)
        
        return result
