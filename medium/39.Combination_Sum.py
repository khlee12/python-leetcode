# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracking(candidates, target, result, [], 0)
        return result
    
    def backtracking(self, candidates, target, result, temp, j):
        if target < 0:
            return
        if target == 0:
            result.append(temp)
        for i in range(j, len(candidates)):
            # 注意递归时传入的j参数是i，而不是i+1
            self.backtracking(candidates, target-candidates[i], result, temp+[candidates[i]], i)
