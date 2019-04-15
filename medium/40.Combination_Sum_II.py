# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = []
        self.backtracking(candidates, target, result, [], 0)
        return result
    def backtracking(self, candidates, target, result, temp, j):
        if target < 0:
            return
        if target == 0:
            result.append(temp)
        for i in range(j, len(candidates)):
            if i>j and candidates[i]==candidates[i-1]:
                continue
            self.backtracking(candidates, target-candidates[i], result, temp+[candidates[i]], i+1)
        
