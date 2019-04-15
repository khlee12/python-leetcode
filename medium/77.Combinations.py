# 77. Combinations
# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(result, [], 0, k, n)
        return result
    
    def backtracking(self, result, temp, j, k, n):
        if len(temp) == k:
            result.append(temp)
            return
        
        for i in range(j, n):
            self.backtracking(result, temp+[i+1], i+1, k, n)
        
