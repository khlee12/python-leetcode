# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        # IMPORTANT, sort!
        nums = sorted(nums)
        self.backtracking(nums, result, [], 0)
        return result
    
    def backtracking(self, nums, result, temp, j):
        result.append(temp)
        for i in range(j, len(nums)):
            if i > j and nums[i]==nums[i-1]:
                continue
            self.backtracking(nums, result, temp+[nums[i]], i+1)
