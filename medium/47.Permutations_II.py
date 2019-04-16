# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        self.backtracking(nums, result, [])
        return result
    
    def backtracking(self, nums, result, temp):
        if not nums:
            result.append(temp)
            return
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.backtracking(nums[:i]+nums[i+1:], result, temp+[nums[i]])
