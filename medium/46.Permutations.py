# 46. Permutations
# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, result, [], 0)
        return result
    
    def backtracking(self, nums, result, temp, j):
        if len(nums) == len(temp):
            result.append(temp)
        for i in range(0, len(nums)):
            if nums[i] in temp:
                continue
            self.backtracking(nums, result, temp+[nums[i]], i+1)
