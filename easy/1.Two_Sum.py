# 1. Two Sum
# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in comp:
                result.append(comp[nums[i]])
                result.append(i)
            else:
                comp[target-nums[i]] = i
        return result
