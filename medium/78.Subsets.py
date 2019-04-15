# 78. Subsets
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回朔法
        result = []
        self.backtracking(result, [], nums, 0)
        return result
    
    def backtracking(self, res, temp, nums, j):
        res.append(temp)
        for i in range(j, len(nums)):
            # temp.append(nums[j])
            self.backtracking(res, temp+[nums[i]], nums, i+1)
            # del temp[-1]
