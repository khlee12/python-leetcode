# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        self.backtracking(k, n, result, [], 0)
        return result
    
    def backtracking(self, k, target, result, temp, j):
        if target < 0:
            return
        if len(temp) > k:
            return
        
        if target==0 and len(temp) == k:
            result.append(temp)
        for i in range(j, 9):
            self.backtracking(k,target-(i+1), result, temp+[i+1], i+1)
